#############################################################################################
#      Author: Austin Harrison
#        Date: 30APR2022
# Description: This Class is the Top Level Game Abstraction
#############################################################################################

from LCD_Class import waveShareDisplay
from LCD_Constants import *
from JoyStick_Class import JoySticks
from Player_Class import Player
from threading import Thread, Semaphore
import queue
import time

C_MAX_BALLS         =  7
C_X_IDX             =  0
C_Y_IDX             =  1
C_TOP_COLLISION     =  2
C_RIGHT_COLLISION   =  1
C_NO_COLLISION      =  0
C_LEFT_COLLISION    = -1
C_BOTTOM_COLLISION  = -2
C_WIGGLE_ROOM       =  2

#############################################################################################
# BEGIN - Class Definitions
#############################################################################################
class Pong():
    def __init__(self) -> None:
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

    

    # This could be optimized probably.
    # This member function erases the left side of the paddle if moving right
    # and vice versa.
    def mErasePaddle(self, player: Player) -> None:
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

    def mDrawPaddle(self, player: Player) -> None:
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

            self._spiSem.acquire()
            # TODO: Change this to draw to a page rather than 1 pixel at a time.
            for i in range(startPixel, endPixel):
                self._lcd.mSetPixel(i , p[C_Y_IDX], player.color)

            self._spiSem.release()
        
        # Update the previous location to current location.
        player.mUpdatePrevLoc(p)

    # Draws the paddle for the first time.
    def _mDrawPaddleInitial(self, player: Player) -> None:
        xy = player.mGetLoc()
        startPixel = xy[C_X_IDX] - (player.WIDTH >> 1)
        endPixel   = xy[C_X_IDX] + (player.WIDTH >> 1)
        self._spiSem.acquire()
        for i in range(startPixel, endPixel):
            self._lcd.mSetPixel(i, xy[C_Y_IDX], player.color)

        self._spiSem.release()
   
    # Moves the ball
    def _mMoveBall(self, ballNum: int) -> None:
        if self._balls != [] and ballNum < len(self._balls):
            self._balls[ballNum].mUpdatePosition(None)

        else:
            print("No balls exist")

    # Draws the ball
    # TODO: Change the balls shape.
    def _mDrawBall(self, ballNum: int) -> None:
        if ballNum < len(self._balls):
            if self._balls[ballNum].mAlive:
                xy    = self._balls[ballNum].mGetPosition()
                color = self._balls[ballNum].mColor
                for i in range(self._balls[ballNum].mGetRadius()*2):
                    for j in range(self._balls[ballNum].mGetRadius()*2):
                        self._lcd.mSetPixel(xy[C_X_IDX] + i, xy[C_Y_IDX] + j, color)

    # Erases the ball
    def _mEraseBall(self, ballNum: int) -> None:
        if ballNum < len(self._balls):
            if self._balls[ballNum].mAlive:
                xy    = self._balls[ballNum].mGetPosition()
                color = C_COLOR_BLACK
                for i in range(self._balls[ballNum].mGetRadius()*2):
                    for j in range(self._balls[ballNum].mGetRadius()*2):
                        self._lcd.mSetPixel(xy[C_X_IDX] + i, xy[C_Y_IDX] + j, color)

    # For now this member function reverses the direction of the ball when
    # it hits the edge of the screen
    def _mCheckBallOutOfBounds(self, ballNum: int) -> None:
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
                #    self.mChangeBallVelocity(ballNum, (velocity[C_X_IDX], velocity[C_Y_IDX] * -1))
                    self.mKillBall(ballNum)

    


    def _mBallThreads(self, ballNum: int) -> None:
        while(True):
            if self.mExitRequest == True:
                return 

            else:
                if self._balls[ballNum].mAlive:
                    self._spiSem.acquire()
                    self._mEraseBall(ballNum)
                    self._mMoveBall(ballNum)
                    self._mCheckBallOutOfBounds(ballNum)
                    self._mCheckBallColliders(ballNum)
                    self._mDrawBall(ballNum)
                    self._spiSem.release()
                
            time.sleep(0.0001)
        

    def _mJoyStickThread(self) -> None:
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

    def _mPrintJoyData(self) -> None:
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

    def _mPlayerThread(self) -> None:
        self._mDrawPaddleInitial(self._player1)
        self._mDrawPaddleInitial(self._player2)
        while(True):
            if self.mExitRequest == False:
                self.mUpdatePlayerPos()
                self.mErasePaddle(self._player1)
                self.mDrawPaddle(self._player1)
                self.mErasePaddle(self._player2)
                self.mDrawPaddle(self._player2)
                time.sleep(0.0001)

            else:
                return

    def _mBallSpawnThread(self) -> None:
        while not self.mExitRequest:
            time.sleep(3)
            if self.mNumBalls < len(self._balls):
                self.mCreateBall(location = (120, 160))

    

    def mInit(self) -> None:
        self._lcd.mInitialize()
        self._lcd.mClearScreen()

    def mRunGame(self) -> None:
        #dataThread = Thread(target = self._mPrintJoyData)
        spawnThread = Thread(target = self._mBallSpawnThread)
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
        spawnThread.start()

        try:
            while True:
                time.sleep(0.2)

        except KeyboardInterrupt:
            self.mExitRequest = True
            joyThread.join()
            for thread in ballThreads:
                thread.join()

            #dataThread.join()
            spawnThread.join()
            playerThread.join()
            self._lcd.mClearScreen()
            self._lcd.mShutdown()
            self._joystick.mShutdown()
        
#############################################################################################
# END - Class Definitions  
#############################################################################################