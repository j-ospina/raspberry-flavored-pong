#############################################################################################
#      Author: Austin Harrison
#        Date: 29APR2022
# Description: This file contains a class that will allow for interfacing with the a joystick
#              via a MCP3008 ADC.
#############################################################################################

from MCP3008_Class import MCP3008ADC
#from gpiozero import OutputDevice
import spidev
#import time

C_DEAD_ZONE_CORRECTION  = 25
C_10_BIT_MIN            = 0x000
C_10_BIT_MAX            = 0x3FF

#############################################################################################
# BEGIN - Class Definitions
#############################################################################################
class JoySticks(MCP3008ADC):
    def __init__(self):
        # Call the ADC Constructor
        super().__init__()
        # Set private values 
        self._minVal        = C_10_BIT_MIN      # 0
        self._midVal        = C_10_BIT_MAX >> 1 # Integer divide by 2
        self._maxVal        = C_10_BIT_MAX      # 1023 (Max Value of 10 bits)
        self._lowerDeadZone = self._midVal - C_DEAD_ZONE_CORRECTION # 25 chosen arbitrarily, can be refined
        self._upperDeadZone = self._midVal + C_DEAD_ZONE_CORRECTION # 25 chosen arbitrarily, can be refined
        # Instantiate a SPI object
        self.mSPI           = spidev.SpiDev()
        self.mSPI.open(0, 1) # Pick Chip Select 1
        self.mSPI.max_speed_hz = 1_000_000 # Spec says ~1.35 MHz (increase this once on PCB)
        self.mSPI.mode = 0b00 # Phase and Polarity are sample on rising edge and clk rests low.

    # To be called after and only after self.mSetDataChx() where x can be [0, 7]
    def _mDataTransfer(self):
        wWord  =  self.getDataWord()
        wByte2 = (wWord >> 8) & 0xFF
        wByte1 =  wWord & 0xFF
        wByte0 =  self.dummyByte
        return self.mSPI.xfer([wByte2, wByte1, wByte0])

    # Add this to the read mReadJoyx functions if there is drift.
    def _mAdjustForDrift(self, xVal, yVal):
        if self._lowerDeadZone < xVal < self._upperDeadZone:
            xVal = self._midVal

        if self._lowerDeadZone < yVal < self._upperDeadZone:
            yVal = self._midVal

        return xVal, yVal

    def mReadJoy0(self):
        # Setup to read X-axis
        self.setDataCh0()
        # Get the word to write
        valueX = self._mDataTransfer()
        valueX = valueX[1] << 8 | valueX[2]
        #time.sleep(0.1)
        # Setup to read X-axis
        self.setDataCh1()
        # Get the word to write
        valueY = self._mDataTransfer()
        valueY = valueY[1] << 8 | valueY[2]
        #time.sleep(0.1)
        #return self._mAdjustForDrift(valueX, valueY)
        return valueX, valueY

    def mReadJoy1(self):
        # Setup to read X-axis
        self.setDataCh2()
        # Get the word to write
        valueX = self._mDataTransfer()
        valueX = valueX[1] << 8 | valueX[2]
        #time.sleep(0.1)
        # Setup to read X-axis
        self.setDataCh3()
        # Get the word to write
        valueY = self._mDataTransfer()
        valueY = valueY[1] << 8 | valueY[2]
        #time.sleep(0.1)
        #return self._mAdjustForDrift(valueX, valueY)
        return valueX, valueY

    # Call this on exit to close the Hardware SPI interface.
    def mShutdown(self):
        self.mSPI.close()


#############################################################################################
# END - Class Definitions
#############################################################################################