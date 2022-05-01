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

C_MAX_BALLS = 3
C_X_IDX     = 0
C_Y_IDX     = 1
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

    def mErasePaddle(self, player):
        p = player.mGetLoc()
        start = p[C_X_IDX] - (player.WIDTH >> 1)
        end   = p[C_X_IDX] + (player.WIDTH >> 1)
        self._spiSem.acquire()
        # TODO: Change this to draw to a page rather than 1 pixel at a time.
        for i in range(start, end):
            self._lcd.mSetPixel(i , p[C_Y_IDX], C_COLOR_BLACK)
            
        self._spiSem.release()

    def mDrawPaddle(self, player):
        p = player.mGetLoc()
        start = p[C_X_IDX] - (player.WIDTH >> 1)
        end   = p[C_X_IDX] + (player.WIDTH >> 1)
        self._spiSem.acquire()
        # TODO: Change this to draw to a page rather than 1 pixel at a time.
        for i in range(start, end):
            self._lcd.mSetPixel(i , p[C_Y_IDX], player.color)

        self._spiSem.release()

    # This method spawns balls
    def mCreateBall(self, color, location):
        self._balls.append(PongBall(color,location))

    # Deletes the selected ball object
    def mKillBall(self, ballNum):
        if self._balls != [] and ballNum < len(self._balls):
            self._balls[ballNum].mAlive = False
            self._mEraseBall(ballNum)

    # Adjusts a ball's velocity
    def mChangeBallVelocity(self, ballNum, newVelocity):
        self._balls[ballNum].mChangeVelocity(newVelocity)

    # Creates N balls of random color
    def mCreateBalls(self, colors, N):
        for i in range(N):
            startX = 0
            startY = 0
            color = colors[random.randint(0, len(colors) - 1)]
            while startX == 0:
                startX = random.randint(-3, 3)

            while startY == 0:
                startY = random.randint(-3, 3)

            self.mCreateBall(color, (100, 100))
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
            self._lcd.mSetPixel(xy[C_X_IDX],     xy[C_Y_IDX],     color)
            self._lcd.mSetPixel(xy[C_X_IDX] + 1, xy[C_Y_IDX],     color)
            self._lcd.mSetPixel(xy[C_X_IDX],     xy[C_Y_IDX] - 1, color)
            self._lcd.mSetPixel(xy[C_X_IDX] + 1, xy[C_Y_IDX] - 1, color)

    # Erases the ball
    def _mEraseBall(self, ballNum):
        if self._balls[ballNum].mAlive:
            xy = self._balls[ballNum].mGetPosition()
            self._lcd.mClearPixel(xy[C_X_IDX],     xy[C_Y_IDX]    )
            self._lcd.mClearPixel(xy[C_X_IDX] + 1, xy[C_Y_IDX]    )
            self._lcd.mClearPixel(xy[C_X_IDX],     xy[C_Y_IDX] - 1)
            self._lcd.mClearPixel(xy[C_X_IDX] + 1, xy[C_Y_IDX] - 1)

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
                self._mDrawBall(ballNum)
                self._spiSem.release()

            time.sleep(0.001)
        

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
                self.mErasePaddle(self._player1)
                self.mErasePaddle(self._player2)
                self.mUpdatePlayerPos()
                self.mDrawPaddle(self._player1)
                self.mDrawPaddle(self._player2)
                time.sleep(0.1)

            else:
                return

    def mInit(self):
        self._lcd.mInitialize()
        self._lcd.mClearScreen()

    def mRunGame(self):
        playerThread = Thread(target = self._mPlayerThread)
        dataThread = Thread(target = self._mPrintJoyData)
        joyThread = Thread(target = self._mJoyStickThread)
        ballThreads = []
        for i in range(len(self._balls)):
            ballThread = Thread(target = self._mBallThreads, args = (i,))
            ballThreads.append(ballThread)
            
        for thread in ballThreads:
            thread.start()

        joyThread.start()
        dataThread.start()
        playerThread.start()

        try:
            while(True):
                time.sleep(0.5)

        except KeyboardInterrupt:
            self.mExitRequest = True
            joyThread.join()
            for thread in ballThreads:
                thread.join()

            dataThread.join()
            self._lcd.mClearScreen()
            self._lcd.mShutdown()
            self._joystick.mShutdown()
        
#############################################################################################
# END - Class Definitions  
#############################################################################################