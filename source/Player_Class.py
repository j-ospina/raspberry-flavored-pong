#############################################################################################
#      Author: Austin Harrison
#        Date: 01MAY2022
# Description: This file defines the player and associated paddle.
#############################################################################################

from LCD_Constants import *

class paddle():
    def __init__(self, xLoc, yLoc):
        self.xLoc = xLoc
        self.yLoc = yLoc        

# The constructor expects a string argument "one" or "two"
class Player(paddle):
    def __init__(self, playerNum):
        if playerNum.lower() == "one":
            self._player    = 1
            super().__init__(C_LCD_MAX_X >> 1, C_LCD_MAX_Y - 4)
        
        elif playerNum.lower() == "two":
            self._player    = 2
            super().__init__(C_LCD_MAX_X >> 1, C_LCD_MIN_Y + 4)

        else:
            raise Exception("Player improperly initialized {}".format(playerNum))
