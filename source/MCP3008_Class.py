#############################################################################################
#      Author: Austin Harrison
#        Date: 29APR2022
# Description: This file contains a class that will allow for interfacing with the MCP3008 
#              ADC.
#############################################################################################

#############################################################################################
# BEGIN - Constants
#############################################################################################
C_START_BIT_POS         = 8
C_SINGLE_nDIFF_POS      = 7
C_D2_POS                = 6
C_D1_POS                = 5
C_D0_POS                = 4
C_ZERO_WORD             = 0x0000
C_DUMMY_BYTE            = 0xA5
C_START_BIT             = 0x0001 << C_START_BIT_POS
C_SINGLE_nDIFF_BIT      = 0x0001 << C_SINGLE_nDIFF_POS
C_D2_BIT                = 0x0001 << C_D2_POS
C_D1_BIT                = 0x0001 << C_D1_POS
C_D0_BIT                = 0x0001 << C_D0_POS

#############################################################################################
# END - Constants
#############################################################################################

#############################################################################################
# BEGIN - Class Definitions
#############################################################################################
class MCP3008ADC():
    def __init__(self) -> None:
        self._startBit          = C_START_BIT
        self._singlenDiffBit    = C_SINGLE_nDIFF_BIT
        self._d2Bit             = C_D2_BIT
        self._d1Bit             = C_D1_BIT
        self._d0Bit             = C_D0_BIT
        self._dWord             = C_ZERO_WORD
        self.dummyByte          = C_DUMMY_BYTE

    # Gets the data word. Call this after a setter, otherwise it will be zero
    def getDataWord(self) -> int:
        dWord = self._dWord
        # Reset to zero such that nothing happens unless we explicitly
        # set a data channel with a member function below.
        self._dWord = C_ZERO_WORD
        return dWord

    def setDataCh0(self) -> None:
        # Set the Start bit to 1, the mode to single ended and clear the data bits such that
        # D2-D0 == 0b000
        self._dWord = (self._startBit | self._singlenDiffBit) & ~(self._d2Bit | self._d1Bit | self._d0Bit)

    def setDataCh1(self) -> None:
        # Set the Start bit to 1, the mode to single ended and clear the data bits such that
        # D2-D0 == 0b001
        self._dWord = (self._startBit | self._singlenDiffBit | self._d0Bit) & ~(self._d2Bit | self._d1Bit)

    def setDataCh2(self) -> None:
        # Set the Start bit to 1, the mode to single ended and clear the data bits such that
        # D2-D0 == 0b010
        self._dWord = (self._startBit | self._singlenDiffBit | self._d1Bit) & ~(self._d2Bit | self._d0Bit)

    def setDataCh3(self) -> None:
        # Set the Start bit to 1, the mode to single ended and clear the data bits such that
        # D2-D0 == 0b011
        self._dWord = (self._startBit | self._singlenDiffBit | self._d1Bit | self._d0Bit) & ~(self._d2Bit)

    def setDataCh4(self) -> None:
        # Set the Start bit to 1, the mode to single ended and clear the data bits such that
        # D2-D0 == 0b100
        self._dWord = (self._startBit | self._singlenDiffBit | self._d2Bit) & ~(self._d1Bit | self._d0Bit)

    def setDataCh5(self) -> None:
        # Set the Start bit to 1, the mode to single ended and clear the data bits such that
        # D2-D0 == 0b101
        self._dWord = (self._startBit | self._singlenDiffBit | self._d2Bit | self._d0Bit) & ~(self._d1Bit)

    def setDataCh6(self) -> None:
        # Set the Start bit to 1, the mode to single ended and clear the data bits such that
        # D2-D0 == 0b110
        self._dWord = (self._startBit | self._singlenDiffBit | self._d2Bit | self._d1Bit) & ~(self._d0Bit)

    def setDataCh7(self) -> None:
        # Set the Start bit to 1, the mode to single ended and clear the data bits such that
        # D2-D0 == 0b111
        self._dWord = (self._startBit | self._singlenDiffBit | self._d2Bit | self._d1Bit | self._d0Bit)

#############################################################################################
# END - Class Definitions
#############################################################################################