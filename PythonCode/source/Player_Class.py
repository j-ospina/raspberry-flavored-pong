#############################################################################################
#      Author: Austin Harrison
#        Date: 01MAY2022
# Description: This file defines the player and associated paddle.
#############################################################################################

from LCD_Constants import *
from source.PongBall_Class import C_X_IDX, C_Y_IDX

# The constructor expects the 2 arguments, the initial x location and
# the initial Y location.
class paddle():
    def __init__(self, xLoc: int, yLoc: int) -> None:
        self.xLoc   = xLoc
        self.yLoc   = yLoc
        self.prevX  = xLoc
        self.prevY  = yLoc
        self.WIDTH  = 40
        self.HEIGHT = 3        

# The constructor expects a string argument "one" or "two"
class Player(paddle):
    def __init__(self, playerNum: str) -> None:
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


    # Moves the player-paddle left or right by amount dX
    def mMovePlayer(self, LeftOrRight: str, dX: int) -> None:
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
            newLoc = self.xLoc

        self.xLoc = newLoc

    # Returns current location in tuple formatted (x, y)
    def mGetLoc(self) -> tuple:
        return (self.xLoc, self.yLoc)

    # Returns previous location in a tuple formatted (x, y)
    def mGetPrevLoc(self) -> tuple:
        return (self.prevX, self.prevY)

    # Takes in a tuple argument formatted (x, y)
    def mUpdatePrevLoc(self, newLoc) -> tuple:
        self.prevX = newLoc[C_X_IDX]
        self.prevY = newLoc[C_Y_IDX]