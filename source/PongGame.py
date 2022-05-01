#############################################################################################
#      Author: Austin Harrison
#        Date: 30APR2022
# Description: This Class is the Top Level Game Abstraction
#############################################################################################

from LCD_Class import waveShareDisplay
from LCD_Constants import *
from JoyStick_Class import JoySticks
from PongBall_Class import PongBall
from threading import Thread, Semaphore
import queue
import time
import random

#############################################################################################
# BEGIN - Class Definitions
#############################################################################################
class Pong():
    def __init__(self):
        self._lcd           = waveShareDisplay()
        self._joystick      = JoySticks()
        self._balls         = []
        self._spiSem        = Semaphore()
        self._q             = queue.Queue()
        self.mExitRequest   = False

    # This method spawns balls
    def mCreateBall(self, color, location):
        self._balls.append(PongBall(color,location))

    # Deletes the selected ball object
    def mKillBall(self, ballNum):
        if self._balls != [] and ballNum < len(self._balls):
            self._balls[ballNum].mAlive = False

    # Adjusts a ball's velocity
    def mChangeBallVelocity(self, ballNum, newVelocity):
        self._balls[ballNum].mChangeVelocity(newVelocity)

    # Creates N balls of random color
    def mCreatBalls(self, colors, N):
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
            self._lcd.mSetPixel(xy[0],     xy[1],     color)
            self._lcd.mSetPixel(xy[0] + 1, xy[1],     color)
            self._lcd.mSetPixel(xy[0],     xy[1] - 1, color)
            self._lcd.mSetPixel(xy[0] + 1, xy[1] - 1, color)

    # Erases the ball
    def _mEraseBall(self, ballNum):
        if self._balls[ballNum].mAlive:
            xy = self._balls[ballNum].mGetPosition()
            self._lcd.mClearPixel(xy[0],     xy[1]    )
            self._lcd.mClearPixel(xy[0] + 1, xy[1]    )
            self._lcd.mClearPixel(xy[0],     xy[1] - 1)
            self._lcd.mClearPixel(xy[0] + 1, xy[1] - 1)

    # For now this member function reverses the direction of the ball when
    # it hits the edge of the screen
    def _mCheckBallOutOfBounds(self, ballNum):
        if self._balls != []:
            if self._balls[ballNum].mAlive:
                xy       = self._balls[ballNum].mGetPosition()
                velocity = self._balls[ballNum].mGetVelocity()
                xBound = abs(velocity[0])
                yBound = abs(velocity[1])
                # Check x coordinates
                # Add one so we know when the ball is at or below 0
                # Subtract two so we know when the ball is greater than or at 239
                if (xy[0] < self._lcd.mX_min + 1 + xBound) or (xy[0] > self._lcd.mX_max - 2 - xBound):
                    self.mChangeBallVelocity(ballNum, (velocity[0] * -1, velocity[1]))
        
                if (xy[1] < self._lcd.mY_min + 1 + yBound) or (xy[1] > self._lcd.mY_max - 2 - yBound):
                    self.mChangeBallVelocity(ballNum, (velocity[0], velocity[1] * -1))

    def _mBallThreads(self, ballNum):
        while(1):
            if not self._balls[ballNum].mAlive or self.mExitRequest == True:
                #temp = self._balls[ballNum]
                #self._balls.pop(ballNum)
                #del temp
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
        while(1):
            if self.mExitRequest == False:
                self._spiSem.acquire()
                x0, y0 = self._joystick.mReadJoy0()
                self._q.put((x0, y0))
                self._spiSem.release()
                time.sleep(0.05)
            
            else:
                return

    def _mPrintJoyData(self):
        while(1):
            if self.mExitRequest == False:
                data = self._q.get()
                print("X Data is:" + str(data[0]))
                print("y Data is:" + str(data[1]))
                time.sleep(1)

            else:
                return

    def mInit(self):
        self._lcd.mInitialize()
        self._lcd.mClearScreen()

    def mRunGame(self):
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