#############################################################################################
#      Author: Austin Harrison
#        Date: 30APR2022
# Description: This file contains a class that draws the ball(s) on the LCD.
#              Radius == 3 pixes
#############################################################################################

C_X_IDX        = 0
C_Y_IDX        = 1

#############################################################################################
# BEGIN - Class Definitions
#############################################################################################
# This Class is for all intents and purposes a Struct. Pass a tuple in form (x, y) to it's 
# constructor
class _ballPosition():
    def __init__(self, Position_tuple):
        self.x = Position_tuple[C_X_IDX]
        self.y = Position_tuple[C_Y_IDX]

    def mUpdatePosition(self, Position_tuple):
        self.x = Position_tuple[C_X_IDX]
        self.y = Position_tuple[C_Y_IDX]

# The ballColor argument needs to be a 16 bit value in the 565 RGB format
# The initial Coordinates argument needs to be a tuple in format (x, y)
# The ball looks like this where 0 is a pixel:
# TODO: Draw balls like this instead of 2x2 square
#   00
#  0000
# 000000
# 000000
#  0000
#   00
class PongBall():
    def __init__(self, ballColor, initCoordinates):
        self._pos           = _ballPosition(initCoordinates)
        self.mPos           = self._pos
        self._radius        = 2                 # Update to 3 later
        self.mColor         = ballColor
        self._mVelocity     = (0, 0)            # default to not moving
        self.mAlive         = True

    # Updates the position based upon current velocity
    def mUpdatePosition(self):
        newX = self._pos.x + self._mVelocity[C_X_IDX]
        newY = self._pos.y + self._mVelocity[C_Y_IDX]
        self._pos.mUpdatePosition((newX, newY))

    # Returns a tuple in format (xPosition, yPosition)
    def mGetPosition(self):
        return (self._pos.x, self._pos.y)

    # This member function expects a tuple in form: (xVelocity, yVelocity)
    def mChangeVelocity(self, newVelocity):
        self._mVelocity = newVelocity

    # This member function returns a tuple of the x and y velocitys
    def mGetVelocity(self):
        return self._mVelocity

    # Returns the radius value
    def mGetRadius(self):
        return self._radius

#############################################################################################
# END - Class Definitions
#############################################################################################