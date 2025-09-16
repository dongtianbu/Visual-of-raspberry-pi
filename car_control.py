# -*- coding: utf-8 -*-
import serial
import binascii
import time

#adress(01) mode(F6-speed) rotation_direction(01-CCW) RPM(05DC) acclerate(0A) mul_syn(00) check_bit(6B) 

#01 F6 01 05 DC 0A 00 6B
#unhexlify 将十六进制字符串转换为二进制数据
#hex_bytes = binascii.unhexlify("01F601000F01006B")

ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=1)
#mini-uart
#ser = serial.Serial("/dev/ttyS0",115200)



def move_forward(RPM, acc):
    #direction:1-cw-00 2-ccw-01 3-cw-00 4-ccw-01
    
    #字节化多机同步命令
    mul_syn_hex = binascii.unhexlify("00FF666B")

    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)

    motor = [None] * 4
    motor_hex_temp = None
    motor_hex = []

    #命令字符串拼接
    for i in range(0, 4):
        if i == 0 or i == 2:
            motor[i] = "0" + str(i + 1) + "F6" + "00" + \
                       RPM_str + acc_str + "016B"
        else:
            motor[i] = "0" + str(i + 1) + "F6" + "01" + \
            RPM_str + acc_str + "016B"

    #把十六进制字符串转换为二进制数据
    for j in range(0, 4):
        motor_hex_temp = binascii.unhexlify(motor[j])
        motor_hex.append(motor_hex_temp)
    
    #依次发送每个电机的完整命令
    for k in range(0, 4):
        ser.write(motor_hex[k]) 
        time.sleep(0.001)  # 适当延时，确保数据发送完成

    #发送多机同步命令，所有电机同时动作
    ser.write(mul_syn_hex)
    print(binascii.hexlify(ser.read(8)))
    print("前进中...")

def move_backwards(RPM, acc):
    #direction:1-ccw-01 2-cw-00 3-ccw-01 4-cw-00
    
    #字节化多机同步命令
    mul_syn_hex = binascii.unhexlify("00FF666B")

    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)
    
    motor = [None] * 4
    motor_hex = [None] * 4
    
    #命令字符串拼接
    for i in range(0, 4):
        if i == 0 or i == 2:
            motor[i] = "0" + str(i + 1) + "F6" + "01" + \
                       RPM_str + acc_str + "016B"
        else:
            motor[i] = "0" + str(i + 1) + "F6" + "00" + \
            RPM_str + acc_str + "016B"

    #把十六进制字符串转换为二进制数据
    for j in range(0, 4):
        motor_hex[j] = binascii.unhexlify(motor[j])
    
    #send command
    for k in range(0, 4):
        ser.write(motor_hex[k])
        time.sleep(0.001)

    #发送多机同步命令，所有电机同时动作
    ser.write(mul_syn_hex)
    print("后退中...")


def turn_left_speed(RPM, acc):
    #direction:1-ccw-01 2-ccw-01 3-ccw-01 4-ccw-01
    
    #字节化多机同步命令
    mul_syn_hex = binascii.unhexlify("00FF666B")

    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)
    
    motor = [None] * 4
    motor_hex = [None] * 4

    #命令字符串拼接
    for i in range(0, 4):
        motor[i] = "0" + str(i + 1) + "F6" + "01" + \
                       RPM_str + acc_str + "016B"
  
    #把十六进制字符串转换为二进制数据
    for j in range(0, 4):
        motor_hex[j] = binascii.unhexlify(motor[j])
    
    #fa
    for k in range(0, 4):
        ser.write(motor_hex[k])

    #发送多机同步命令，所有电机同时动作
    ser.write(mul_syn_hex)
    print("左转中...")

def turn_right_speed(RPM, acc):
    #direction:1-cw-00 2-cw-00 3-cw-00 4-cw-00
    
    #字节化多机同步命令
    mul_syn_hex = binascii.unhexlify("00FF666B")

    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)
    

    
    motor = [None] * 4
    motor_hex = [None] * 4
    
    #命令字符串拼接
    for i in range(0, 4):
        motor[i] = "0" + str(i + 1) + "F6" + "00" + \
                       RPM_str + acc_str + "016B"
  
    #把十六进制字符串转换为二进制数据
    for j in range(0, 4):
        motor_hex[j] = binascii.unhexlify(motor[j])
    
    #send command
    for k in range(0, 4):
        ser.write(motor_hex[k])
    #发送多机同步命令，所有电机同时动作
    ser.write(mul_syn_hex)
    print("右转中...")

def move_left(RPM, acc):
    #direction:1-ccw-01 2-ccw-01 3-cw-00 4-cw-00
    
    #字节化多机同步命令
    mul_syn_hex = binascii.unhexlify("00FF666B")

    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)
    
    motor = [None] * 4
    motor_hex = [None] * 4
    
    #命令字符串拼接
    for i in range(0, 4):
        if i == 0 or i == 1:
            motor[i] = "0" + str(i + 1) + "F6" + "01" + \
                       RPM_str + acc_str + "016B"
        else:
            motor[i] = "0" + str(i + 1) + "F6" + "00" + \
            RPM_str + acc_str + "016B"

    #把十六进制字符串转换为二进制数据
    for j in range(0, 4):
        motor_hex[j] = binascii.unhexlify(motor[j])
    
    #send command
    for k in range(0, 4):
        ser.write(motor_hex[k])

    #发送多机同步命令，所有电机同时动作
    ser.write(mul_syn_hex)
    print("向左平移中...")

    
def move_right(RPM, acc):
    #direction:1-cw-00 2-cw-00 3-ccw-01 4-ccw-01
    
    #字节化多机同步命令
    mul_syn_hex = binascii.unhexlify("00FF666B")

    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)
    
    motor = [None] * 4
    motor_hex = [None] * 4

    #命令字符串拼接
    for i in range(0, 4):
        if i == 2 or i == 3:
            motor[i] = "0" + str(i + 1) + "F6" + "01" + \
                       RPM_str + acc_str + "016B"
        else:
            motor[i] = "0" + str(i + 1) + "F6" + "00" + \
            RPM_str + acc_str + "016B"

    #把十六进制字符串转换为二进制数据
    for j in range(0, 4):
        motor_hex[j] = binascii.unhexlify(motor[j])
    
    #send command
    for k in range(0, 4):
        ser.write(motor_hex[k])
        
    #发送多机同步命令，所有电机同时动作
    ser.write(mul_syn_hex)
    print("向右平移中...")


#位置模式命令
#地址 + 0xFD + 方向 + 速度+ 加速度 + 脉冲数 + 相对/绝对模式标志(00表示相对位置模式，01绝对位置模式) + 多机同步标志 + 校验字节
#01 FD 01 05 DC 00 00 00 7D 00 00 00 6B
def turn_left_position(RPM, acc):
    #direction:1-ccw-01 2-ccw-01 3-ccw-01 4-ccw-01
    
    #待调试参数pulse，通过调试出pulse的取值，得出何时为小车转90度
    pulse = 100000

    #字节化多机同步命令
    mul_syn_hex = binascii.unhexlify("00FFFD6B")

    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)
    pulse_str = "{:08X}".format(pulse)
    
    motor_1 = "01FD01" + RPM_str + acc_str + pulse_str + "017D6B"
    
    motor = [None] * 4
    motor_hex = [None] * 4

    #命令字符串拼接
    for i in range(0, 4):
        motor[i] = "0" + str(i + 1) + "FD" + "01" + RPM_str + \
                       acc_str + pulse_str + "00016B"#相对位置模式00启用多机同步01


    #把十六进制字符串转换为二进制数据
    for j in range(0, 4):
        motor_hex[j] = binascii.unhexlify(motor[j])
    
    #send command
    for k in range(0, 4):
        ser.write(motor_hex[k])
        
    #发送多机同步命令，所有电机同时动作
    ser.write(mul_syn_hex)
    print("左转90度中...")

def turn_right_position(RPM, acc):
    #direction:1-cw-00 2-cw-00 3-cw-00 4-cw-00
    
    #待调试参数pulse，通过调试出pulse的取值，得出何时为小车转90度
    pulse = 100000

    #字节化多机同步命令
    mul_syn_hex = binascii.unhexlify("00FFFD6B")

    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)
    pulse_str = "{:08X}".format(pulse)
    
    motor_1 = "01FD01" + RPM_str + acc_str + pulse_str + "017D6B"
    
    motor = [None] * 4
    motor_hex = [None] * 4
    
    #命令字符串拼接
    for i in range(0, 4):
        motor[i] = "0" + str(i + 1) + "FD" + "00" + RPM_str + \
                       acc_str + pulse_str + "00016B"#相对位置模式00启用多机同步01


    #把十六进制字符串转换为二进制数据
    for j in range(0, 4):
        motor_hex[j] = binascii.unhexlify(motor[j])
    
    #send command
    for k in range(0, 4):
        ser.write(motor_hex[k])
        
    #发送多机同步命令，所有电机同时动作
    ser.write(mul_syn_hex)
    print("右转90度中...")
    
#停止所有电机
def motor_stop():
    #停止命令
    stop_hex = binascii.unhexlify("00FE98006B")
    ser.write(stop_hex)
    print("所有电机已停止！")
