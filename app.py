#############################################################################################
#      Author: Austin Harrison
#        Date: 01MAY2022
# Description: This file instantiates the Pong Game and runs it.
#############################################################################################
from sre_constants import FAILURE, SUCCESS
import sys
sys.path.insert(0, './source')
from source.LCD_Constants import *
from source.PongGame import Pong
import subprocess as sp

# Leave this until diagrams are created and uploaded to git.
# GPIO11 - SPICLK
# GPIO10 - SPI MOSI
# GPIO9  - SPI MISO
# GPIO8  - SPI CE0
# GPIO7  - SPI CE1

FAILURE         = -1
SUCCESS         =  0
C_MAX_BALLS     =  7

def main():
    # Turn on hardware SPI
    sp.run(["sudo", "dtparam", "spi=on"])
    
    myColors = [
        C_COLOR_PINK,       C_COLOR_LIGHT_GREEN,    C_COLOR_PURPLE, 
        C_COLOR_LIGHT_BLUE, C_COLOR_BLUE,           C_COLOR_GREEN, 
        C_COLOR_INDIGO,     C_COLOR_ORANGE,         C_COLOR_RED, 
        C_COLOR_VIOLET,     C_COLOR_YELLOW
    ]

    # Instantiate the clas
    pong = Pong()
    # Create C_MAX_BALLS balls with random velocities
    pong.mCreateBalls(myColors, C_MAX_BALLS)

    #TODO: Fix ball start location logic such that the velocity does not get negated if it starts to
    #      close to the wall.
    # Initialize the LCD and the ADC
    pong.mInit()
    # Main Game loop (Runs on threads with semaphores and a Queue for inter-process communication).
    pong.mRunGame()

    # Turn off Hardware spi
    sp.run(["sudo", "dtparam", "spi=off"])
    sys.exit(SUCCESS)

if __name__ == "__main__":
    main()