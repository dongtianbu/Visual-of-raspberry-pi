# -*- coding: utf-8 -*-
import serial
import binascii
import time

#adress(01) mode(F6-speed) rotation_direction(01-CCW) RPM(05DC) acclerate(0A) mul_syn(00) check_bit(6B) 

#01 F6 01 05 DC 0A 00 6B

hex_bytes = binascii.unhexlify("01F601000F01006B")

ser = serial.Serial("/dev/ttyAMA0",115200)
#mini-uart
#ser = serial.Serial("/dev/ttyS0",115200)

print("serial test start ...")
ser.write(hex_bytes)
time.sleep(1)
rec_buffer = [None] * 4 
for i in list(range(0, 4)):
    rec_buffer[i] = ser.read()

print(rec_buffer)
print("serial send complete!")


def move_forward(RPM, acc):
    #direction:1-cw-00 2-ccw-01 3-cw-00 4-ccw-01
    
    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)
    
    motor_1 = "01F600" + RPM_str + acc_str + "016B"
    
    motor = [None] * 4
    
    #initialize
    for i in range(0, 4):
        if i == 0 or i == 2:
            motor[i] = "0" + str(i + 1) + "F6" + "00" + \
                       RPM_str + acc_str + "016B"
        else:
            motor[i] = "0" + str(i + 1) + "F6" + "01" + \
            RPM_str + acc_str + "016B"

    #hexlify
    for j in range(0, 4):
        motor_hex = binascii.hexlify(motor(j))
    
    #send command
    for k in range(0, 4):
        ser.write(motor[k])
    
    hex_bytes = binascii.unhexlify("01F601000F01006B")