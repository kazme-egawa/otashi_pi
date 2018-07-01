# coding: utf-8

import serial

ser = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 2)

ser.write(chr(0x12)) # 0x12
ser.write(chr(0x53)) # 0x53
ser.write(chr(0x01)) # 0x00 or 01
ser.write("新しいものづくりがわかるメディア\r")
ser.write(chr(0x12)) # 0x12
ser.write(chr(0x53)) # 0x53
ser.write(chr(0x00)) # 0x00 or 01

ser.write(chr(0x1C)) # 0x1C
ser.write(chr(0x57)) # 0x57
ser.write(chr(0x01)) # 0x00 or 01
ser.write(chr(0x1B)) # 0x1B
ser.write(chr(0x6C)) # 0x6C
ser.write(chr(0x0C)) # 0x00 - 0x2F
ser.write("fabcross\r")
ser.write(chr(0x1C)) # 0x1C
ser.write(chr(0x57)) # 0x57
ser.write(chr(0x00)) # 0x00 or 01

ser.write("\r");  # Line Feed

ser.write(chr(0x1B)) # 0x1B
ser.write(chr(0x6C)) # 0x6C
ser.write(chr(0x28)) # 0x00 - 0x2F
ser.write("担:01\r")

ser.write("-----------------------------\r")
ser.write("大きい声　　　　　　　　数量 1\r\r\r")

ser.write(chr(0x1B)) # 0x1B
ser.write(chr(0x57)) # 0x57
ser.write(chr(0x01)) # 0x00 or 01
ser.write("内容\r\r\r\r\r\r")
ser.write(chr(0x1B)) # 0x1B
ser.write(chr(0x57)) # 0x57
ser.write(chr(0x00)) # 0x00 or 01


ser.write("（内うるさい度 ）\r")

ser.write(chr(0x1B)) # 0x1B
ser.write(chr(0x68)) # 0x68
ser.write(chr(0x00)) # 0x00 or 01 or 02 or 03
ser.write(chr(0x12)) # 0x12
ser.write(chr(0x53)) # 0x53
ser.write(chr(0x01)) # 0x00 or 01
ser.write(chr(0x1B)) # 0x1B
ser.write(chr(0x6C)) # 0x6C
ser.write(chr(0x20)) # 0x00 - 0x2F
ser.write("レシート No.012\r")
ser.write(chr(0x1B)) # 0x1B
ser.write(chr(0x68)) # 0x68
ser.write(chr(0x01)) # 0x00 or 01 or 02 or 03
ser.write(chr(0x12)) # 0x12
ser.write(chr(0x53)) # 0x53
ser.write(chr(0x00)) # 0x00 or 01

ser.write("-----------------------------\r")

ser.write(chr(0x1B)) # 0x1B
ser.write(chr(0x6C)) # 0x6C
ser.write(chr(0x08)) # 0x00 - 0x2F
ser.write("》》》 記事見てね！《《《\r")

ser.write(chr(0x1B)) # 0x1B
ser.write(chr(0x4A)) # 0x4A
ser.write(chr(0x10)) # 0xXX
ser.write("記事はこちら！！\r")

ser.write(chr(0x1B)) # 0x1B
ser.write(chr(0x68)) # 0x68
ser.write(chr(0x00)) # 0x00 or 01 or 02 or 03
ser.write("\rhttps://fabcross.jp/list/series/sorepi/\r\r")
ser.write(chr(0x1B)) # 0x1B
ser.write(chr(0x68)) # 0x68
ser.write(chr(0x01)) # 0x00 or 01 or 02 or 03

ser.write("[それ、ラズパイでつくれるよ]\rで検索！\r")
ser.write("\r\r");  # Line Feed

# QRcode Print
ser.write(chr(0x1D))
ser.write(chr(0x79))
ser.write(chr(0x01))
ser.write(chr(0x1D))
ser.write(chr(0x78))
ser.write(chr(0x4C))
ser.write(chr(0x27))
ser.write("https://fabcross.jp/list/series/sorepi/")   # DATA
ser.write("\r\r\r\r\r\r");  # Line Feed

ser.close()
