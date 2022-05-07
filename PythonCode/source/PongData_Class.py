#############################################################################################
#      Author: Austin Harrison
#        Date: 06MAY2022
# Description: This Class is an abstraction of the game data. Note that the __future__ library
#              allows for annotations such as declaring a list of a certain type as seen in
#              class member _balls
#############################################################################################

from Player_Class import Player
from PongBall_Class import PongBall
from PongGame_Class import C_MAX_BALLS
from __future__ import annotations
import random
import time

C_ZERO              =  0

#############################################################################################
# BEGIN - Class Definitions
#############################################################################################
class PongData():
    def __init__(self) -> None:
        self._player1   = Player("One")
        self._player2   = Player("Two")
        self._balls     = [PongBall]
        self.mNumBalls  = C_ZERO

    
    # This method spawns balls that were killed. This should be used within
    # the ball creation thread.
    def mSpawnBall(self, location: tuple) -> None:
        if self.mNumBalls < C_MAX_BALLS:
            newBallMade = False
            while not newBallMade:
                ballNum = random.randint(C_ZERO, C_MAX_BALLS - 1)
                if not self._balls[ballNum].mAlive:
                    newVelY = C_ZERO
                    while newVelY == C_ZERO:
                        newVelY = random.randint(-4, 4)
                        time.sleep(0.01)

                    newVelX = random.randint(-4, 4)
                    self._balls[ballNum].mUpdatePosition(location)
                    self._balls[ballNum].mChangeVelocity((newVelX, newVelY))
                    self._balls[ballNum].mAlive = True
                    newBallMade = True
                
                else:
                    time.sleep(0.01)

            self.mNumBalls += 1

    # Kills the selected ball object
    def mKillBall(self, ballNum: int) -> None:
        if self._balls != [] and ballNum < C_MAX_BALLS:
            self.mNumBalls -= 1
            self._balls[ballNum].mAlive = False

#############################################################################################
# END - Class Definitions
#############################################################################################