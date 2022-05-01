#############################################################################################
#      Author: Austin Harrison
#        Date: 01MAY2022
# Description: This file instantiates the Pong Game and runs it.
#############################################################################################
import time
import sys
sys.path.insert(0, './source')
from source.LCD_Constants import *
from source.LCD_Class import waveShareDisplay
from source.JoyStick_Class import JoySticks
from source.PongGame import Pong
import random
import subprocess as sp

# GPIO11 - SPICLK
# GPIO10 - SPI MOSI
# GPIO9  - SPI MISO
# GPIO8  - SPI CE0
# GPIO7  - SPI CE1

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
    # Create 5 balls with random velocities
    pong.mCreatBalls(myColors, 5)

    #TODO: Fix ball start location logic such that the velocity does not get negated if it starts to
    #      close to the wall.
    # Initialize the LCD and the ADC
    pong.mInit()
    # Main Game loop (Runs on threads with semaphores and a Queue for inter-process communication).
    pong.mRunGame()

    # Turn off Hardware spi
    sp.run(["sudo", "dtparam", "spi=off"])


if __name__ == "__main__":
    main()