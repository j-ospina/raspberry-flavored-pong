#############################################################################################
#      Author: Austin Harrison
#        Date: 27APR2022
# Description: This file contains a class that will allow for interfacing with the waveshare
#              2-inch IPS LCD screen.
#############################################################################################

from LCD_Constants import *
from gpiozero import OutputDevice
import spidev
import time

#############################################################################################
# BEGIN - Class Definitions
#############################################################################################
class waveShareDisplay():
    def __init__(self):
        self.mX_min     = 0
        self.mY_min     = 0
        self.mWidth     = 240 # pixels wide
        self.mHeight    = 320 # pixels high
        self.mX_max     = 240
        self.mY_max     = 320
        self._dc        = OutputDevice(pin = C_PIN_DC,  active_high = True, initial_value = True) # Data not Command
        self._bl        = OutputDevice(pin = C_PIN_BL,  active_high = True, initial_value = True)
        self._nRst      = OutputDevice(pin = C_PIN_RST, active_high = False, initial_value = False)
        self._cs0       = OutputDevice(pin = C_PIN_CS0, active_high = False, initial_value = False)
        self.mSPI_if    = spidev.SpiDev()
        self.mSPI_if.open(0, 0)
        self.mSPI_if.max_speed_hz = 20_000_000
        self.mSPI_if.mode = 0b00
        

    # This private member function sets the Data not Command pin to command mode
    def _mEnterCmdMode(self):
        self._cs0.on()
        self._dc.off()

    # This private member function sets the Data not Command pin to data mode
    def _mEnterDataMode(self):
        self._cs0.on()
        self._dc.on()

    # This member function turns off the back light
    def mTurnOffBackLight(self):
        self._bl.off()

    # This member function turns on the back light    
    def mTurnOnBackLight(self):
        self._bl.on()

    # This performs a hardware reset for 200ms. 400ms total
    def mReset(self):
        self._nRst.on()
        time.sleep(0.2)
        self._nRst.off()
        time.sleep(0.2)

    # This member function performs a command write. It expects commands formatted in bytes.
    def mWriteCMD(self, cmd):
        self._mEnterCmdMode()
        self.mSPI_if.writebytes([cmd])

    # This member function performs a data write. It expects bytes of data.
    def mWriteData(self, data):
        self._mEnterDataMode()
        self.mSPI_if.writebytes([data])
        self._cs0.off()

    # This member function closes the spi module
    def mShutdown(self):
        self.mTurnOffBackLight()
        self.mSPI_if.close()
        self._dc.close()
        self._bl.close()
        self._nRst.close()

    def mInitialize(self):
        self.mReset()
        
        self.mWriteCMD(C_CMD_MEM_DAT_ACCESS_CTL)
        self.mWriteData(0xA0)

        # Set pixel format to use an 8 bit data bus for the 16 bit pixel values
        self.mWriteCMD(C_CMD_INTERFACE_PIXEL_FMT)
        self.mWriteData(C_DATA_8BIT_DB_16BIT_PIXEL)
        
        # Invert the Display? (Probs remove this)
        self.mWriteCMD(C_CMD_DISPLAY_INVERSION)
        # Set column Address and write 4 bytes
        self.mWriteCMD(C_CMD_COL_ADDR_SET)
        self.mWriteData(C_ZERO_BYTE)
        self.mWriteData(0x01)
        self.mWriteData(C_ZERO_BYTE) # TODO: Figure out what these hardcoded values are
        self.mWriteData(0x3F)
        # Set row address and write 4 bytes
        self.mWriteCMD(C_CMD_ROW_ADDR_SET)
        self.mWriteData(C_ZERO_BYTE)
        self.mWriteData(C_ZERO_BYTE)
        self.mWriteData(C_ZERO_BYTE)
        self.mWriteData(0xEF)
        # TODO: What is Porch Control?
        self.mWriteCMD(C_CMD_PORCH_CTL)
        self.mWriteData(0x0C)
        self.mWriteData(0x0C)
        self.mWriteData(C_ZERO_BYTE)
        self.mWriteData(0x33)
        self.mWriteData(0x33)
        # TODO: What is Gate control?
        self.mWriteCMD(C_CMD_GATE_CTL)
        self.mWriteData(0x35)

        # TODO: What is VCOM setting?
        self.mWriteCMD(C_CMD_VCOM_SETTING)
        self.mWriteData(0x1F)
        # TODO: What is LCM Control
        self.mWriteCMD(C_CMD_LCM_CTL)
        self.mWriteData(0x2C)

        # TODO: Find out what VDV and VRH is.
        self.mWriteCMD(C_CMD_VDV_VRH_CMD_EN)
        self.mWriteData(0x01)
        # TODO: What is VRH?
        self.mWriteCMD(C_CMD_VRH_SET)
        self.mWriteData(0x12)
        # TODO: What is VDV
        self.mWriteCMD(C_CMD_VDV_SETTING)
        self.mWriteData(0x20)
        # TODO: What is FR_CTL_2?
        self.mWriteCMD(C_CMD_FR_CTL_2)
        self.mWriteData(0x0F)
        # TODO: What is Power Control 1?
        self.mWriteCMD(C_CMD_PWR_CTL_1)
        self.mWriteData(0xA4)
        self.mWriteData(0xA1)
        
        # TODO: What is Gamma Control? (Pos and Neg)
        self.mWriteCMD(C_CMD_POS_V_GAMMA_CTL)
        self.mWriteData(0xD0)
        self.mWriteData(0x08)
        self.mWriteData(0x11)
        self.mWriteData(0x08)
        self.mWriteData(0x0C)
        self.mWriteData(0x15)
        self.mWriteData(0x39)
        self.mWriteData(0x33)
        self.mWriteData(0x50)
        self.mWriteData(0x36)
        self.mWriteData(0x13)
        self.mWriteData(0x14)
        self.mWriteData(0x29)
        self.mWriteData(0x2D)
        self.mWriteCMD(C_CMD_NEG_V_GAMMA_CTL)
        self.mWriteData(0xD0)
        self.mWriteData(0x08)
        self.mWriteData(0x10)
        self.mWriteData(0x08)
        self.mWriteData(0x06)
        self.mWriteData(0x06)
        self.mWriteData(0x39)
        self.mWriteData(0x44)
        self.mWriteData(0x51)
        self.mWriteData(0x0B)
        self.mWriteData(0x16)
        self.mWriteData(0x14)
        self.mWriteData(0x2F)
        self.mWriteData(0x31)

        self.mWriteCMD(C_CMD_DISPLAY_INVERSION)
        self.mWriteCMD(C_CMD_SLEEP_OUT)
        time.sleep(0.5)
        self.mWriteCMD(C_CMD_DISPLAY_ON)
        self.mTurnOnBackLight()
        # End of mInitialize

    # Call this before Drawing to the LCD
    def mSetDrawWindow(self, bX, eX, bY, eY):
        # Set X - coordinates
        self.mWriteCMD(C_CMD_COL_ADDR_SET)
        self.mWriteData(bY >> 8)
        self.mWriteData((bY & 0xFF))
        self.mWriteData(eY >> 8)
        self.mWriteData((eY & 0xFF))

        # Set Y - coordinates
        self.mWriteCMD(C_CMD_ROW_ADDR_SET)
        self.mWriteData(bX >> 8)
        self.mWriteData((bX & 0xFF))
        self.mWriteData(eX >> 8)
        self.mWriteData((eX & 0xFF))

        # Write to memory
        self.mWriteCMD(C_CMD_MEM_WRITE)

    def mSetCursor(self, xPos, yPos):
        self.mWriteCMD(C_CMD_COL_ADDR_SET)
        self.mWriteData(yPos >> 8)
        self.mWriteData(yPos)
        self.mWriteData(yPos >> 8)
        self.mWriteData(yPos)
        
        self.mWriteCMD(C_CMD_ROW_ADDR_SET)
        self.mWriteData(xPos >> 8)
        self.mWriteData(xPos)
        self.mWriteData(xPos >> 8)
        self.mWriteData(xPos)

        # Enable Writes to memory
        self.mWriteCMD(C_CMD_MEM_WRITE)

    def mClearScreen(self):
        _buffer = [0x00]*(self.mWidth * self.mHeight * 2)
        self.mSetDrawWindow(0, self.mWidth-1, 0, self.mHeight-1)
        self._mEnterDataMode()
        for i in range(0,len(_buffer),4096):
            self.mSPI_if.writebytes(_buffer[i:i+4096])
            
        self._cs0.off()

    def mSetPixel(self, xPos, yPos, color):
        _buffer = [(color>>8) & 0xFF, color & 0xFF]
        self.mSetCursor(xPos, yPos)
        self._mEnterDataMode()
        for i in range(0, len(_buffer), 2):
            self.mSPI_if.writebytes(_buffer[i:i+2])
        
        self._cs0.off()

    def mClearPixel(self, xPos, yPos):
        self.mSetPixel(xPos, yPos, 0x00)

    def mDrawLine(self, axis, start, end):
        if axis == 'X' or axis == 'x':
            for i in range(end - start):
                self.mSetPixel(start + i, 15, C_COLOR_PINK)
    
        elif axis == 'Y' or axis == 'y':
            for i in range(end - start):
                self.mSetPixel(15, start + i, C_COLOR_PINK)

        else:
            print("Bad axis argument.")


#############################################################################################
# END - Class Definitions
#############################################################################################