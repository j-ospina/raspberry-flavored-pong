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
from LCD_Constants import C_LCD_MAX_X, C_LCD_MIN_X, C_LCD_MAX_Y, C_LCD_MIN_Y
from JoyStick_Class import C_MID_VAL
from __future__ import annotations
import random
import time

C_X_IDX             =  0
C_Y_IDX             =  1
C_ZERO              =  0
C_TOP_COLLISION     =  2
C_RIGHT_COLLISION   =  1
C_NO_COLLISION      =  0
C_LEFT_COLLISION    = -1
C_BOTTOM_COLLISION  = -2
C_WIGGLE_ROOM       =  2
C_ARENA_WALL_WIDTH  =  1

#############################################################################################
# BEGIN - Class Definitions
#############################################################################################
class PongData():
    def __init__(self, q1, q2) -> None:
        self._player1     = Player("One")
        self._player2     = Player("Two")
        self._balls       = [PongBall]
        self.mNumBalls    = C_ZERO
        self.mArenaRight  = C_LCD_MIN_X - 1
        self.mArenaLeft   = C_LCD_MAX_X - 1
        self._q1          = q1
        self._q2          = q2
        
    # Creates N balls of random color (Initial call)
    def mCreateBalls(self, colors: list, N: int) -> None:
        for i in range(N):
            startXVel = 0
            startYVel = 0
            color = colors[random.randint(0, len(colors) - 1)]
            startX = random.randint(-4, 4)

            while startYVel == 0:
                startYVel = random.randint(-4, 4)

            # Set the spawn positions at least 20 pixels from the wall.
            ball = PongBall(color, (random.randint(20, 220), random.randint(20, 300)))
            self._balls.append(ball)
            self.mChangeBallVelocity(i, (startXVel, startYVel))

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
            if self._balls[ballNum].mAlive:
                self.mNumBalls -= 1
                self._balls[ballNum].mAlive = False

    # Adjusts a ball's velocity
    def mChangeBallVelocity(self, ballNum: int, newVelocity: tuple) -> None:
        self._balls[ballNum].mChangeVelocity(newVelocity)

    # The minkowski algorithm is a fast way of detecting collisions and
    # and the side they occured on.
    # c code example of a call to this Algorithm:
    # Minkowski = MinkowskiAlgorithm(((BALL_SIZE +  (PADDLE_LEN / 3)) >> 1) + WIGGLE_ROOM,
    #                                ((BALL_SIZE + PADDLE_WID) >> 1) + WIGGLE_ROOM,
    #                                 Self.balls[Ball_Index].currentCenterX - Self.players[BOTTOM].currentCenter + PADDLE_LEN_D2 - (PADDLE_LEN / 6),
    #                                 Self.balls[Ball_Index].currentCenterY - BOTTOM_PLAYER_CENTER_Y);
    def _mMinkowski(self, w: int, h: int, dx: int, dy: int) -> int:
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


    def _mReverseBallOnCollision(self, ballNum: int, side: int) -> None:
        xy       = self._balls[ballNum].mGetPosition()
        velocity = self._balls[ballNum].mGetVelocity()
        if side == C_TOP_COLLISION or side == C_BOTTOM_COLLISION:
            self.mChangeBallVelocity(ballNum, (velocity[C_X_IDX], velocity[C_Y_IDX] * - 1))

        elif side == C_RIGHT_COLLISION or side == C_LEFT_COLLISION:
            self.mChangeBallVelocity(ballNum, (velocity[C_X_IDX] * -1, velocity[C_Y_IDX]))

    
    # c code example of a call to this Algorithm:
    # Minkowski = MinkowskiAlgorithm(((BALL_SIZE +  (PADDLE_LEN / 3)) >> 1) + WIGGLE_ROOM,
    #                                ((BALL_SIZE + PADDLE_WID) >> 1) + WIGGLE_ROOM,
    #                                 Self.balls[Ball_Index].currentCenterX - Self.players[BOTTOM].currentCenter + PADDLE_LEN_D2 - (PADDLE_LEN / 6),
    #                                 Self.balls[Ball_Index].currentCenterY - BOTTOM_PLAYER_CENTER_Y);
    def _mCheckBallColliders(self, ballNum: int) -> None:
        for i in range(ballNum + 1, self.mNumBalls):
            minkowski = self._mMinkowski(
                w  = self._balls[ballNum].mGetRadius() * 2 + self._balls[i].mGetRadius() * 2,
                h  = self._balls[ballNum].mGetRadius() * 2 + self._balls[i].mGetRadius() * 2,
                dx = self._balls[ballNum]._pos.x - self._balls[i]._pos.x,
                dy = self._balls[ballNum]._pos.y - self._balls[i]._pos.y
            )
            if minkowski != C_NO_COLLISION:
                #print("Collision" + str(ballNum) + ":" + str(minkowski))
                self._mReverseBallOnCollision(ballNum, minkowski)
                self._mReverseBallOnCollision(i,       minkowski)
            
        p1XY = self._player1.mGetLoc()
        p1X  = p1XY[C_X_IDX]
        p1Y  = p1XY[C_Y_IDX]
        p2XY = self._player2.mGetLoc()
        p2X  = p2XY[C_X_IDX]
        p2Y  = p2XY[C_Y_IDX]
        # Check P1 paddle
        minkowski = self._mMinkowski(
            w  = self._balls[ballNum].mGetRadius() * 2 + self._player1.WIDTH + C_WIGGLE_ROOM,
            h  = self._balls[ballNum].mGetRadius() * 2 + self._player1.HEIGHT,
            dx = self._balls[ballNum].mPos.x - p1X,
            dy = self._balls[ballNum].mPos.y - p1Y
        )

        if minkowski != C_NO_COLLISION:
            self._mReverseBallOnCollision(ballNum, minkowski)

        # Check P2 paddle
        minkowski = self._mMinkowski(
            w  = self._balls[ballNum].mGetRadius() * 2 + self._player2.WIDTH + C_WIGGLE_ROOM,
            h  = self._balls[ballNum].mGetRadius() * 2 + self._player2.HEIGHT,
            dx = self._balls[ballNum].mPos.x - p2X,
            dy = self._balls[ballNum].mPos.y - p2Y
        )

        if minkowski != C_NO_COLLISION:
            self._mReverseBallOnCollision(ballNum, minkowski)

        # Check Right side of the arena.
        minkowski = self._mMinkowski(
            w  = self._balls[ballNum].mGetRadius() * 2 + C_ARENA_WALL_WIDTH + C_WIGGLE_ROOM,
            h  = self._balls[ballNum].mGetRadius() * 2 + C_LCD_MAX_Y,
            dx = self._balls[ballNum].mPos.x - self.mArenaRight,
            dy = self._balls[ballNum].mPos.Y - (C_LCD_MAX_Y >> 1)
        )

        if minkowski != C_NO_COLLISION:
            self._mReverseBallOnCollision(ballNum, minkowski)

        # Check Right side of the arena.
        minkowski = self._mMinkowski(
            w  = self._balls[ballNum].mGetRadius() * 2 + C_ARENA_WALL_WIDTH + C_WIGGLE_ROOM,
            h  = self._balls[ballNum].mGetRadius() * 2 + C_LCD_MAX_Y,
            dx = self._balls[ballNum].mPos.x - self.mArenaLeft,
            dy = self._balls[ballNum].mPos.Y - (C_LCD_MAX_Y >> 1)
        )

        if minkowski != C_NO_COLLISION:
            self._mReverseBallOnCollision(ballNum, minkowski)

    # Map the ADC values to number of pixels the paddle should move.
    def _mNormalizeADC(self, val: int) -> int:
        if val <= 127 or val >= 896:
            return 5

        elif 127 < val <= 254 or 896 > val >= 769:
            return 4

        elif 254 < val <= 381 or 769 > val > 642:
            return 3
            
        elif 381 < val or 642 > val:
            return 0

    def mUpdatePlayerPos(self) -> None:
        p1 = self._q1.get()
        p2 = self._q2.get()
        mag1 = p1[C_X_IDX]
        mag2 = p2[C_X_IDX]
        # mag1 <= 511
        if mag1 <= C_MID_VAL:
            moveDir1 = "left"
        
        # mag1 > 511
        else:
            moveDir1 = "right"

        # mag2 <= 511
        if mag2 <= C_MID_VAL:
            moveDir2 = "left"
        
        # mag1 > 511
        else:
            moveDir2 = "right"
            
        mag1 = self._mNormalizeADC(mag1)
        self._player1.mMovePlayer(moveDir1, mag1)

        mag2 = self._mNormalizeADC(mag2)
        self._player2.mMovePlayer(moveDir2, mag2)
#############################################################################################
# END - Class Definitions
#############################################################################################