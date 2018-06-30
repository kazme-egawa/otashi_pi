# coding: utf-8

import serial

ser = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 2)

# Text Print
ser.write("Thermal Printer Shield\r");
ser.write("Text Printing.\r");
ser.write("\r\r");  # Line Feed x 2

# QRcode Print
ser.write(chr(0x1D))  # 0x1D
ser.write(chr(0x78)) # 0x78
ser.write(chr(0x4C))  # 0x4C
ser.write(chr(0x04))  # 0x04
ser.write("TEST")   # DATA
ser.write("\r\r\r\r\r\r");  # Line Feed x 6

ser.close()
