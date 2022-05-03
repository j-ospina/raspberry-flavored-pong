#############################################################################################
#      Author: Austin Harrison
#        Date: 30APR2022
# Description: This Class is the Top Level Game Abstraction
#############################################################################################

from LCD_Class import waveShareDisplay
from LCD_Constants import *
from JoyStick_Class import JoySticks
from PongBall_Class import PongBall
from Player_Class import Player
from threading import Thread, Semaphore
import queue
import time
import random

C_MAX_BALLS         =  3
C_X_IDX             =  0
C_Y_IDX             =  1
C_TOP_COLLISION     =  2
C_RIGHT_COLLISION   =  1
C_NO_COLLISION      =  0
C_LEFT_COLLISION    = -1
C_BOTTOM_COLLISION  = -2

#############################################################################################
# BEGIN - Class Definitions
#############################################################################################
class Pong():
    def __init__(self):
        self._lcd           = waveShareDisplay()
        self._joystick      = JoySticks()
        self._balls         = []
        self._spiSem        = Semaphore()
        self._q1            = queue.Queue()
        self._q2            = queue.Queue()
        self._player1       = Player("One")
        self._player2       = Player("Two")
        self.mExitRequest   = False
        self.mNumBalls      = 0

    def mNormalizeADC(self, val):
        if val <= 127:
            return 0

        elif 127 < val <= 254:
            return 1

        elif 254 < val <= 381:
            return 2

        elif 381 < val <= 511:
            return 3

    def mUpdatePlayerPos(self):
        p1 = self._q1.get()
        p2 = self._q2.get()
        mag1 = p1[C_X_IDX]
        mag2 = p2[C_X_IDX]
        # mag1 <= 511
        if mag1 <= self._joystick.mGetMidVal():
            moveDir1 = "Left"
        
        # mag1 > 511
        else:
            mag1 -= 511
            moveDir1 = "Right"

        # mag2 <= 511
        if mag2 <= self._joystick.mGetMidVal():
            moveDir2 = "Left"
        
        # mag1 > 511
        else:
            mag2 -= 511
            moveDir2 = "Right"

        mag1 = self.mNormalizeADC(mag1)
        mag2 = self.mNormalizeADC(mag2)
        self._player1.mMovePlayer(moveDir1, mag1)
        self._player2.mMovePlayer(moveDir2, mag2)

    # This could be optimized probably.
    # This member function erases the left side of the paddle if moving right
    # and vice versa.
    def mErasePaddle(self, player):
        p     = player.mGetLoc()
        pPrev = player.mGetPrevLoc()
        x     = p[C_X_IDX]
        xPrev = pPrev[C_X_IDX]
        if x != xPrev:
            if x > xPrev:
                deltaX     = x - xPrev
                # Moving Right
                # Start pixel for erasure on the left end should be the
                # previous x minus half the width
                startPixel = xPrev - (player.WIDTH >> 1)
                # The end pixel would be the left end of the paddle plus
                # the delta (x - xPrev) for Erasure
                endPixel   = xPrev - (player.WIDTH >> 1) + deltaX
                
            # xPrev > x
            else:
                deltaX     = xPrev - x
                # Moving Left
                # Start pixel would be the right end of the paddle of the
                # Previous position minus the dX for Erasure
                startPixel = xPrev + (player.WIDTH >> 1) - deltaX
                # The end pixel would be the left end of the paddle of the 
                # previous position
                endPixel   = xPrev + (player.WIDTH >> 1)

            # Update the previous location to current location.
            self._spiSem.acquire()
            # TODO: Change this to draw to a page rather than 1 pixel at a time.
            for i in range(startPixel, endPixel):
                self._lcd.mSetPixel(i , p[C_Y_IDX], C_COLOR_BLACK)

            self._spiSem.release()

    def mDrawPaddle(self, player):
        p     = player.mGetLoc()
        pPrev = player.mGetPrevLoc()
        x     = p[C_X_IDX]
        xPrev = pPrev[C_X_IDX]
        if x != xPrev:
            if x > xPrev:
                deltaX     = x - xPrev
                # Moving Right
                # Start pixel would be the right end of the paddle of the 
                # previous position
                startPixel = xPrev + (player.WIDTH >> 1)
                # The end pixel would be the right end of the paddle plus
                # the delta (x - xPrev)
                endPixel   = xPrev + (player.WIDTH >> 1) + deltaX
                
            # xPrev > x
            else:
                deltaX     = xPrev - x
                # Moving Left
                # Start pixel would be the left end of the paddle of the
                # Previous position minus the dX
                startPixel = xPrev - (player.WIDTH >> 1) - deltaX
                # The end pixel would be the left end of the paddle of the 
                # previous position
                endPixel   = xPrev - (player.WIDTH >> 1)

            # Update the previous location to current location.
            player.mUpdatePrevLoc(p)
            self._spiSem.acquire()
            # TODO: Change this to draw to a page rather than 1 pixel at a time.
            for i in range(startPixel, endPixel):
                self._lcd.mSetPixel(i , p[C_Y_IDX], player.color)

            self._spiSem.release()


    # This method spawns balls
    def mCreateBall(self, color, location):
        self._balls.append(PongBall(color,location))
        self.mNumBalls += 1

    # Deletes the selected ball object
    def mKillBall(self, ballNum):
        if self._balls != [] and ballNum < len(self._balls):
            self._balls[ballNum].mAlive = False
            self._mEraseBall(ballNum)
            self.mNumBalls -= 1

    # Adjusts a ball's velocity
    def mChangeBallVelocity(self, ballNum, newVelocity):
        self._balls[ballNum].mChangeVelocity(newVelocity)

    # Creates N balls of random color
    def mCreateBalls(self, colors, N):
        for i in range(N):
            startX = 0
            startY = 0
            color = colors[random.randint(0, len(colors) - 1)]
            startX = random.randint(-3, 3)

            if startX == 0:
                while startY == 0:
                    startY = random.randint(-3, 3)

            else:
                startY = random.randint(-3, 3)

            if startY > 0:
                startY += 2

            elif startY < 0:
                startY -= 2

            if startX > 0:
                startX += 2

            elif startX < 0:
                startX -= 2
                
            self.mCreateBall(color, (random.randint(20, 220), random.randint(20, 300)))
            self.mChangeBallVelocity(i, (startX, startY))

    # Moves the ball
    def _mMoveBall(self, ballNum):
        if self._balls != [] and ballNum < len(self._balls):
            self._balls[ballNum].mUpdatePosition()

        else:
            print("No balls exist")

    # Draws the ball
    # TODO: Change the balls shape.
    def _mDrawBall(self, ballNum):
        if self._balls[ballNum].mAlive:
            xy    = self._balls[ballNum].mGetPosition()
            color = self._balls[ballNum].mColor
            for i in range(self._balls[ballNum].mGetRadius()*2):
                for j in range(self._balls[ballNum].mGetRadius()*2):
                    self._lcd.mSetPixel(xy[C_X_IDX] + i, xy[C_Y_IDX] + j, color)

           # self._lcd.mSetPixel(xy[C_X_IDX],     xy[C_Y_IDX],     color)
           # self._lcd.mSetPixel(xy[C_X_IDX] + 1, xy[C_Y_IDX],     color)
           # self._lcd.mSetPixel(xy[C_X_IDX],     xy[C_Y_IDX] - 1, color)
           # self._lcd.mSetPixel(xy[C_X_IDX] + 1, xy[C_Y_IDX] - 1, color)

    # Erases the ball
    def _mEraseBall(self, ballNum):
        if self._balls[ballNum].mAlive:
            xy    = self._balls[ballNum].mGetPosition()
            color = C_COLOR_BLACK
            for i in range(self._balls[ballNum].mGetRadius()*2):
                for j in range(self._balls[ballNum].mGetRadius()*2):
                    self._lcd.mSetPixel(xy[C_X_IDX] + i, xy[C_Y_IDX] + j, color)

    # For now this member function reverses the direction of the ball when
    # it hits the edge of the screen
    def _mCheckBallOutOfBounds(self, ballNum):
        if self._balls != []:
            if self._balls[ballNum].mAlive:
                xy       = self._balls[ballNum].mGetPosition()
                velocity = self._balls[ballNum].mGetVelocity()
                xBound = abs(velocity[C_X_IDX])
                yBound = abs(velocity[C_Y_IDX])
                # Check x coordinates
                # Add one so we know when the ball is at or below 0
                # Subtract two so we know when the ball is greater than or at 239
                if (xy[C_X_IDX] < self._lcd.mX_min + 1 + xBound) or (xy[C_X_IDX] > self._lcd.mX_max - 2 - xBound):
                    self.mChangeBallVelocity(ballNum, (velocity[C_X_IDX] * -1, velocity[C_Y_IDX]))
        
                if (xy[C_Y_IDX] < self._lcd.mY_min + 1 + yBound) or (xy[C_Y_IDX] > self._lcd.mY_max - 2 - yBound):
                    self.mChangeBallVelocity(ballNum, (velocity[C_X_IDX], velocity[C_Y_IDX] * -1))

    def _mReverseBallOnCollision(self, ballNum, side):
        xy       = self._balls[ballNum].mGetPosition()
        velocity = self._balls[ballNum].mGetVelocity()
        if side == C_TOP_COLLISION or side == C_BOTTOM_COLLISION:
            self.mChangeBallVelocity(ballNum, (velocity[C_X_IDX], velocity[C_Y_IDX] * - 1))

        elif side == C_RIGHT_COLLISION or side == C_LEFT_COLLISION:
            self.mChangeBallVelocity(ballNum, (velocity[C_X_IDX] * -1, velocity[C_Y_IDX]))

    '''
    c code example of a call to this Algorithm:
    Minkowski = MinkowskiAlgorithm(((BALL_SIZE +  (PADDLE_LEN / 3)) >> 1) + WIGGLE_ROOM,
                                   ((BALL_SIZE + PADDLE_WID) >> 1) + WIGGLE_ROOM,
                                    Self.balls[Ball_Index].currentCenterX - Self.players[BOTTOM].currentCenter + PADDLE_LEN_D2 - (PADDLE_LEN / 6),
                                    Self.balls[Ball_Index].currentCenterY - BOTTOM_PLAYER_CENTER_Y);
    '''
    def _mCheckBallColliders(self, ballNum):
        for i in range(ballNum + 1, self.mNumBalls):
            minkowski = self._mMinkowski(
                w  = self._balls[ballNum].mGetRadius() * 2 + self._balls[i].mGetRadius() * 2,
                h  = self._balls[ballNum].mGetRadius() * 2 + self._balls[i].mGetRadius() * 2,
                dx = self._balls[ballNum]._pos.x - self._balls[i]._pos.x,
                dy = self._balls[ballNum]._pos.y - self._balls[i]._pos.y
            )
            if minkowski != C_NO_COLLISION:
                print("Collision" + str(ballNum) + ":" + str(minkowski))
                self._mReverseBallOnCollision(ballNum, minkowski)
                self._mReverseBallOnCollision(i,       minkowski)
                break

    def _mBallThreads(self, ballNum):
        while(True):
            if not self._balls[ballNum].mAlive:
                temp = self._balls[ballNum]
                self._balls.pop(ballNum)
                del temp
                
            elif self.mExitRequest == True:
                return 

            else:
                self._spiSem.acquire()
                self._mEraseBall(ballNum)
                self._mMoveBall(ballNum)
                self._mCheckBallOutOfBounds(ballNum)
                self._mCheckBallColliders(ballNum)
                self._mDrawBall(ballNum)
                self._spiSem.release()

            time.sleep(0.0001)
        

    def _mJoyStickThread(self):
        while(True):
            if self.mExitRequest == False:
                self._spiSem.acquire()
                x0, y0 = self._joystick.mReadJoy0()
                self._q1.put((x0, y0))
                x1, y1 = self._joystick.mReadJoy1()
                self._q2.put((x1, y1))
                self._spiSem.release()
                time.sleep(0.05)
            
            else:
                return

    def _mPrintJoyData(self):
        while(True):
            if self.mExitRequest == False:
                data = self._q1.get()
                print("X1 Data is:" + str(data[C_X_IDX]))
                print("y1 Data is:" + str(data[C_Y_IDX]))
                data = self._q2.get()
                print("X2 Data is:" + str(data[C_X_IDX]))
                print("y2 Data is:" + str(data[C_Y_IDX]))
                time.sleep(1)

            else:
                return

    def _mPlayerThread(self):
        while(True):
            if self.mExitRequest == False:
                self.mUpdatePlayerPos()
                self.mErasePaddle(self._player1)
                self.mDrawPaddle(self._player1)
                self.mErasePaddle(self._player2)
                self.mDrawPaddle(self._player2)
                time.sleep(0.01)

            else:
                return

    # The minkowski algorithm is a fast way of detecting collisions and
    # and the side they occured on.
    '''
    c code example of a call to this Algorithm:
    Minkowski = MinkowskiAlgorithm(((BALL_SIZE +  (PADDLE_LEN / 3)) >> 1) + WIGGLE_ROOM,
                                   ((BALL_SIZE + PADDLE_WID) >> 1) + WIGGLE_ROOM,
                                    Self.balls[Ball_Index].currentCenterX - Self.players[BOTTOM].currentCenter + PADDLE_LEN_D2 - (PADDLE_LEN / 6),
                                    Self.balls[Ball_Index].currentCenterY - BOTTOM_PLAYER_CENTER_Y);
    '''
    def _mMinkowski(self, w, h, dx, dy):
        if abs(dx) <= w and abs(dy) <= h:
            wy = w*dy
            hx = h*dx
            if  wy > hx:
                if wy > -hx:
                    # On the Top
                    return C_TOP_COLLISION

                else:
                    # On the Left
                    return C_LEFT_COLLISION
            
            else:
                if wy > -hx:
                    # On the right
                    return C_RIGHT_COLLISION

                else:
                    # On the bottom
                    return C_BOTTOM_COLLISION

        else:
            return C_NO_COLLISION

    def mInit(self):
        self._lcd.mInitialize()
        self._lcd.mClearScreen()

    def mRunGame(self):
        #dataThread = Thread(target = self._mPrintJoyData)
        joyThread = Thread(target = self._mJoyStickThread)
        playerThread = Thread(target = self._mPlayerThread)
        ballThreads = []
        for i in range(len(self._balls)):
            ballThread = Thread(target = self._mBallThreads, args = (i,))
            ballThreads.append(ballThread)
            
        for thread in ballThreads:
            thread.start()

        joyThread.start()
        #dataThread.start()
        playerThread.start()

        try:
            while(True):
                time.sleep(0.5)

        except KeyboardInterrupt:
            self.mExitRequest = True
            joyThread.join()
            for thread in ballThreads:
                thread.join()

            #dataThread.join()
            playerThread.join()
            self._lcd.mClearScreen()
            self._lcd.mShutdown()
            self._joystick.mShutdown()
        
#############################################################################################
# END - Class Definitions  
#############################################################################################