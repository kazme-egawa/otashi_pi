# coding: utf-8

import serial

ser = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 2)

ser.write("新しいものづくりがわかるメディア\r")
ser.write("fabcross\r")
ser.write("担:01\r")
ser.write("-------------------------\r")
ser.write("大きい声　　　　　　　　数量 1\r\r\r")
ser.write("内容\r\r\r\r\r\r")
ser.write("（内うるさい度 ）\r")
ser.write("レシート No.012\r")
ser.write("-------------------------\r")
ser.write("》》》記事見てね！《《《\r")
ser.write("記事はこちら！！\r")
ser.write("https://fabcross.jp/list/series/sorepi/\r")
ser.write("[それ、ラズパイでつくれるよ]で検索！\r")

# QRcode Print
ser.write(chr(0x1D))
ser.write(chr(0x79))
ser.write(chr(0x01))
ser.write(chr(0x1D))
ser.write(chr(0x78))
ser.write(chr(0x4C))
ser.write(chr(0x27))
ser.write("https://fabcross.jp/list/series/sorepi/")   # DATA
ser.write("\r\r\r\r\r\r");  # Line Feed x 6

ser.close()
