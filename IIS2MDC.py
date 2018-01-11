#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""IIS2MDC: High-accuracy, ultra-low-power, 3-axis digital output magnetometer"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["STMicroelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

from IIS2MDC_constants import *

# name:        IIS2MDC
# description: High-accuracy, ultra-low-power, 3-axis digital output magnetometer
# manuf:       STMicroelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/iis2mdc.pdf
# date:        2018-01-11


# Derive from this class and implement read and write
class IIS2MDC_Base:
	"""High-accuracy, ultra-low-power, 3-axis digital output magnetometer"""
	# Register OFFSET_X
	# 8.1
	#       These registers comprise a 16-bit register and represent X hard-iron offset in order to compensate 
	#       environmental effects (data in two’s complement). These values act on the magnetic output data value 
	#       in order to delete the environmental offset. 
	
	
	def setOFFSET_X(self, val):
		"""Set register OFFSET_X"""
		self.write(REG.OFFSET_X, val, 16)
	
	def getOFFSET_X(self):
		"""Get register OFFSET_X"""
		return self.read(REG.OFFSET_X, 16)
	
	# Bits OFFSET_X
	# Register OFFSET_Y
	# 8.2
	#       These registers comprise a 16-bit register and represent Y hard-iron offset in order to compensate 
	#       environmental effects (data in two’s complement). These values act on the magnetic output data value 
	#       in order to delete the environmental offset. 
	
	
	def setOFFSET_Y(self, val):
		"""Set register OFFSET_Y"""
		self.write(REG.OFFSET_Y, val, 16)
	
	def getOFFSET_Y(self):
		"""Get register OFFSET_Y"""
		return self.read(REG.OFFSET_Y, 16)
	
	# Bits OFFSET_Y
	# Register OFFSET_Z_
	# 8.3
	#       These registers comprise a 16-bit register and represent Z hard-iron offset in order to compensate 
	#       environmental effects (data in two’s complement). These values act on the magnetic output data value 
	#       in order to delete the environmental offset. 
	
	
	def setOFFSET_Z_(self, val):
		"""Set register OFFSET_Z_"""
		self.write(REG.OFFSET_Z_, val, 16)
	
	def getOFFSET_Z_(self):
		"""Get register OFFSET_Z_"""
		return self.read(REG.OFFSET_Z_, 16)
	
	# Bits OFFSET_Z_
	# Register WHO_AM_I
	# 8.4
	#       The identification register is used to identify the device. 
	
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits WHO_AM_I
	# Register CFG_REG_A
	# 8.5
	#       The configuration register is used to configure the output data rate and the measurement configuration. 
	
	
	def setCFG_REG_A(self, val):
		"""Set register CFG_REG_A"""
		self.write(REG.CFG_REG_A, val, 8)
	
	def getCFG_REG_A(self):
		"""Get register CFG_REG_A"""
		return self.read(REG.CFG_REG_A, 8)
	
	# Bits COMP_TEMP_EN
	# 1.   For proper operation, this bit must be set to '1'. 
	# Bits REBOOT
	# Bits SOFT_RST
	# When this bit is set, the configuration registers and user registers are reset. 
	#           Flash registers keep their values. 
	
	# Bits LP
	# Enables low-power mode. 
	# Bits ODR
	# Output data rate configuration (see Table 25: Output data rate configuration). 
	# Bits MD
	# These bits select the mode of operation of the device (see Table 26: Mode of operation). 
	# Register CFG_REG_B
	# 8.6 
	
	def setCFG_REG_B(self, val):
		"""Set register CFG_REG_B"""
		self.write(REG.CFG_REG_B, val, 8)
	
	def getCFG_REG_B(self):
		"""Get register CFG_REG_B"""
		return self.read(REG.CFG_REG_B, 8)
	
	# Bits reserved_0
	# Bits OFF_CANC_ONE_SHOT
	# Enables offset cancellation in single measurement mode. The OFF_CANC bit must be set to 1 when enabling 
	#           offset cancellation in single measurement mode. 
	
	# Bits INT_on_DataOFF
	# If ‘1’, the interrupt block recognition checks data after the hard-iron correction to discover 
	#         the interrupt. 
	
	# Bits Set_FREQ
	# Selects the frequency of the set pulse. 
	# Bits OFF_CANC
	# Enables offset cancellation. 
	# Bits LPF
	# Enables low-pass filter (see Table 29). 
	# Register CFG_REG_C
	# 8.7 
	
	def setCFG_REG_C(self, val):
		"""Set register CFG_REG_C"""
		self.write(REG.CFG_REG_C, val, 8)
	
	def getCFG_REG_C(self):
		"""Get register CFG_REG_C"""
		return self.read(REG.CFG_REG_C, 8)
	
	# Bits reserved_0
	# Bits INT_on_PIN
	# If '1', the INTERRUPT signal (INT bit in INT_SOURCE_REG (64h)) is driven
	#           on the INT/DRDY pin. The INT/DRDY pin is configured in push-pull output mode. 
	
	# Bits I2C_DIS
	# If ‘1’, the I2C interface is inhibited. Only the SPI interface can be used. 
	# Bits BDU
	# If enabled, reading of incorrect data is avoided when the user reads asynchro­ nously. 
	#           In fact if the read request arrives during an update of the output data, a latch is possible, 
	#           reading incoherent high and low parts of the same register. Only one part is updated and the other 
	#           one remains old. 
	
	# Bits BLE
	# If ‘1’, an inversion of the low and high parts of the data occurs. 
	# Bits reserved_1
	# This bit must be set to ‘0’ for the correct operation of the device. 
	# Bits Self_test
	# If ‘1’, the self-test is enabled. 
	# Bits DRDY_on_PIN
	# If '1', the data-ready signal (Zyxda bit in STATUS_REG (67h)) is driven on the INT/DRDY pin. 
	#           The INT/DRDY pin is configured in push-pull output mode. 
	
	# Register INT_CTRL_REG
	# 8.8
	#       The interrupt control register is used to enable and to configure the interrupt recognition. 
	
	
	def setINT_CTRL_REG(self, val):
		"""Set register INT_CTRL_REG"""
		self.write(REG.INT_CTRL_REG, val, 8)
	
	def getINT_CTRL_REG(self):
		"""Get register INT_CTRL_REG"""
		return self.read(REG.INT_CTRL_REG, 8)
	
	# Bits XIEN
	# Bits YIEN
	# Bits ZIEN
	# Bits reserved_0
	# This bit must be set to ‘0’ for the correct operation of the device. 
	# Bits IEA
	# Controls the polarity of the INT bit (INT_SOURCE_REG (64h)) when an interrupt occurs. 
	#           If IEA = 0, then INT = 0 signals an interrupt. If IEA = 1, then INT = 1 signals an interrupt. 
	
	# Bits IEL
	# Controls whether the INT bit (INT_SOURCE_REG (64h)) is latched or pulsed.
	#           If IEL = 0, then INT is pulsed. If IEL = 1, then INT is latched.
	#           Once latched, INT remains in the same state until INT_SOURCE_REG (64h) is read. 
	
	# Bits IEN
	# Interrupt enable. When set, enables the interrupt generation. The INT bit is in INT_SOURCE_REG (64h). 
	# Register INT_SOURCE_REG
	# 8.9
	#       When interrupt latched is selected, reading this register resets all the bits in this register. 
	
	
	def setINT_SOURCE_REG(self, val):
		"""Set register INT_SOURCE_REG"""
		self.write(REG.INT_SOURCE_REG, val, 8)
	
	def getINT_SOURCE_REG(self):
		"""Get register INT_SOURCE_REG"""
		return self.read(REG.INT_SOURCE_REG, 8)
	
	# Bits P_TH_S_X
	# X-axis value exceeds the threshold positive side 
	# Bits P_TH_S_Y
	# Y-axis value exceeds the threshold positive side 
	# Bits P_TH_S_Z
	# Z-axis value exceeds the threshold positive side 
	# Bits N_TH_S_X
	# X-axis value exceeds the threshold negative side 
	# Bits N_TH_S_Y
	# Y-axis value exceeds the threshold negative side  
	# Bits N_TH_S_Z
	# Z-axis value exceeds the threshold negative side 
	# Bits MROI
	# MROI flag generation is alway enabled.This flag is reset by reading
	#           INT_SOURCE_REG (64h). 
	
	# Bits INT
	# This bit signals when the interrupt event occurs. 
	# Register INT_THS_L_REG
	# 8.10-11
	#       These registers set the threshold value for the output to generate the interrupt (INT bit in
	#       INT_SOURCE_REG (64h)). This threshold is common to all three (axes) output values and is 
	#       unsigned unipolar. The threshold value is correlated to the current gain and it is unsigned 
	#       because the threshold is considered as an absolute value, but crossing the threshold is detected 
	#       for both positive and negative sides. 
	
	
	def setINT_THS_L_REG(self, val):
		"""Set register INT_THS_L_REG"""
		self.write(REG.INT_THS_L_REG, val, 16)
	
	def getINT_THS_L_REG(self):
		"""Get register INT_THS_L_REG"""
		return self.read(REG.INT_THS_L_REG, 16)
	
	# Bits INT_THS_L_REG
	# Register STATUS_REG
	# 8.12
	#       The status register is an 8-bit read-only register. This register is used to indicate device status. 
	
	
	def setSTATUS_REG(self, val):
		"""Set register STATUS_REG"""
		self.write(REG.STATUS_REG, val, 8)
	
	def getSTATUS_REG(self):
		"""Get register STATUS_REG"""
		return self.read(REG.STATUS_REG, 8)
	
	# Bits Zyxor
	# X-, Y- and Z-axis data overrun. 
	# Bits zor
	# Z-axis data overrun. 
	# Bits yor
	# Y-axis data overrun. 
	# Bits xor_
	# X-axis data overrun. 
	# Bits Zyxda
	# X-, Y- and Z-axis new data available. 
	# Bits zda
	# Z-axis new data available. 
	# Bits yda
	# Y-axis new data available. 
	# Bits xda
	# X-axis new data available. 
	# Register OUTX
	# 8.13
	#       The data output X registers are two 8-bit registers, data output X MSB register (69h) and output X LSB register (68h).
	#       The output data represents the raw magnetic data only if OFFSET_X_REG is equal to zero, otherwise hard-iron calibration is included.
	#       The value of the magnetic field is expressed in two’s complement. This register contains the
	#       X component of the magnetic data. 
	
	
	def setOUTX(self, val):
		"""Set register OUTX"""
		self.write(REG.OUTX, val, 16)
	
	def getOUTX(self):
		"""Get register OUTX"""
		return self.read(REG.OUTX, 16)
	
	# Bits OUTX
	# Register OUTY
	# 8.14
	#       The data output Y registers are two 8-bit registers, data output Y MSB register (6Bh) and output Y LSB register (6Ah).
	#       The output data represents the raw magnetic data only if OFFSET_Y_REG is equal to zero, otherwise hard-iron calibration is included.
	#       The value of the magnetic field is expressed in two’s complement. This register contains the
	#       Y component of the magnetic data. 
	
	
	def setOUTY(self, val):
		"""Set register OUTY"""
		self.write(REG.OUTY, val, 16)
	
	def getOUTY(self):
		"""Get register OUTY"""
		return self.read(REG.OUTY, 16)
	
	# Bits OUTY
	# Register OUTZ
	# 8.15
	#       The data output Z registers are two 8-bit registers, data output Z MSB register (6Bh) and output Z LSB register (6Ah).
	#       The output data represents the raw magnetic data only if OFFSET_Z_REG is equal to zero, otherwise hard-iron calibration is included.
	#       The value of the magnetic field is expressed in two’s complement. This register contains the
	#       Z component of the magnetic data. 
	
	
	def setOUTZ(self, val):
		"""Set register OUTZ"""
		self.write(REG.OUTZ, val, 16)
	
	def getOUTZ(self):
		"""Get register OUTZ"""
		return self.read(REG.OUTZ, 16)
	
	# Bits OUTZ
