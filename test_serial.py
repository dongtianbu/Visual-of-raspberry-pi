# -*- coding: utf-8 -*-
import serial
import binascii
import time

#adress(01) mode(F6-speed) rotation_direction(01-CCW) RPM(05DC) acclerate(0A) mul_syn(00) check_bit(6B) 

#01 F6 01 05 DC 0A 00 6B




hex_bytes = binascii.unhexlify("01F601000F01006B")

ser = serial.Serial("/dev/ttyAMA0",115200)
#ser = serial.Serial("/dev/ttyS0",115200)

print("serial test start ...")
ser.write(hex_bytes)
time.sleep(1)
rec_buffer = [None] * 4 
for i in list(range(0, 4)):
    rec_buffer[i] = ser.read()

print(rec_buffer)
print("serial send complete!")

