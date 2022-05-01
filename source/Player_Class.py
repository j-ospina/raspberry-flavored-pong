#############################################################################################
#      Author: Austin Harrison
#        Date: 01MAY2022
# Description: This file defines the player and associated paddle.
#############################################################################################

from LCD_Constants import *

class paddle():
    def __init__(self, xLoc, yLoc):
        self.xLoc   = xLoc
        self.yLoc   = yLoc
        self.WIDTH  = 30
        self.HEIGHT = 3        

# The constructor expects a string argument "one" or "two"
class Player(paddle):
    def __init__(self, playerNum):
        if playerNum.lower() == "one":
            self._player    = 1
            self.color      = C_COLOR_BLUE
            super().__init__(C_LCD_MAX_X >> 1, C_LCD_MAX_Y - 4)
        
        elif playerNum.lower() == "two":
            self._player    = 2
            self.color      = C_COLOR_RED
            super().__init__(C_LCD_MAX_X >> 1, C_LCD_MIN_Y + 4)

        else:
            raise Exception("Player improperly initialized {}".format(playerNum))

    def mMovePlayer(self, LeftOrRight, dX):
        if LeftOrRight.lower() == "left":
            delta = self.xLoc - (self.WIDTH >> 1) - dX
            if delta < C_LCD_MIN_X:
                newLoc = self.WIDTH >> 1

            else:
                newLoc = self.xLoc - dX

        elif LeftOrRight.lower() == "right":
            delta = self.xLoc + (self.WIDTH >> 1) + dX
            if delta > C_LCD_MAX_X - 1:
                newLoc = C_LCD_MAX_X - (self.WIDTH >> 1) - 1

            else:
                newLoc = self.xLoc + dX

        else:
            raise Exception("left nor right chosen")

        self.xLoc = newLoc

    def mGetLoc(self):
        return (self.xLoc, self.yLoc)