# coding: utf-8

# Thermal Printer Shield for Raspberry Pi3
# Model:AS-289R2 & AS-289R
# Python source code
# NADA ELECTRONICS, LTD.
# http://www.nada.co.jp
# By. Takehiro Yamaguchi

import serial

ser = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 2)

# Text Print
ser.write("Thermal Printer Shield\r");
ser.write("Text Printing.\r");
ser.write("\r\r");  # Line Feed x 2

# QRcode Print
ser.write(chr(29))  # 0x1D
ser.write(chr(120)) # 0x78
ser.write(chr(76))  # 0x4C
ser.write(chr(4 ))  # 0x04
ser.write("TEST")   # DATA
ser.write("\r\r\r\r\r\r");  # Line Feed x 6

ser.close()
