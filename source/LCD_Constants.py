#############################################################################################
#      Author: Austin Harrison
#        Date: 27APR2022
# Description: This file contains the constants needed to use the waveshare 2-inch LCD IPS.
#############################################################################################

#############################################################################################
# BEGIN - Constants
#############################################################################################
C_PIN_CS0                   = 16        # TODO: Figure out if this is doing anything at all
C_PIN_BL                    = 23
C_PIN_RST                   = 24
C_PIN_DC                    = 25
C_LCD_DEV_NUM               = 0
C_LCD_PORT_NUM              = 0
C_LCD_MIN_X                 = 0
C_LCD_MAX_X                 = 240
C_LCD_MIN_Y                 = 0
C_LCD_MAX_Y                 = 320
C_ZERO_BYTE                 = 0x00
C_CMD_SWRESET               = 0x01
C_CMD_MEM_DAT_ACCESS_CTL    = 0x36
C_CMD_INTERFACE_PIXEL_FMT   = 0x3A
C_CMD_WR_MEM_CONTINUE       = 0x3C
C_CMD_DISPLAY_INVERSION     = 0x21
C_CMD_COL_ADDR_SET          = 0x2A
C_CMD_ROW_ADDR_SET          = 0x2B
C_CMD_MEM_WRITE             = 0x2C
C_CMD_RAM_CTL               = 0xB0
C_CMD_PORCH_CTL             = 0xB2
C_CMD_GATE_CTL              = 0xB7
C_CMD_VCOM_SETTING          = 0xBB
C_CMD_LCM_CTL               = 0xC0
C_CMD_VDV_VRH_CMD_EN        = 0xC2
C_CMD_VRH_SET               = 0xC3
C_CMD_VDV_SETTING           = 0xC4
C_CMD_FR_CTL_2              = 0xC6
C_CMD_PWR_CTL_1             = 0xD0
C_CMD_POS_V_GAMMA_CTL       = 0xE0
C_CMD_NEG_V_GAMMA_CTL       = 0xE1
C_CMD_SLEEP_OUT             = 0x11
C_CMD_NORMAL_DISP_MODE      = 0x13
C_CMD_DISPLAY_ON            = 0x29

C_DATA_8BIT_DB_16BIT_PIXEL  = 0x05   

# COLORS
C_COLOR_PURPLE              = 0x685A
C_COLOR_PINK                = 0xF85A
C_COLOR_LIGHT_GREEN         = 0x1EB0
C_COLOR_LIGHT_BLUE          = 0x8EFE
C_COLOR_RED                 = 0xF800
C_COLOR_BLUE                = 0x001F
C_COLOR_ORANGE              = 0xFAC0
C_COLOR_YELLOW              = 0xFEC0
C_COLOR_GREEN               = 0x07E0
C_COLOR_INDIGO              = 0x4810
C_COLOR_VIOLET              = 0x881F

#############################################################################################
# END - Constants
#############################################################################################