#位置模式命令
#地址 + 0xFD + 方向 + 速度+ 加速度 + 脉冲数 + 相对/绝对模式标志(00表示相对位置模式，01绝对位置模式) + 多机同步标志 + 校验字节
#01 FD 01 05 DC 00 00 00 7D 00 00 00 6B
def lifting_up(RPM, acc, distance):
    #direction:5-ccw-01
    
    #待调试参数pulse，通过调试pulse的取值，得出具体的上升距离和pulse的关系
    pulse = 100000

    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)
    pulse_str = "{:08X}".format(pulse)
    
    motor_5 = "05" + "FD" + "01" + RPM_str + \
                       acc_str + pulse_str + "00006B"#相对位置模式00不启用多机同步00
    
    #把十六进制字符串转换为二进制数据
    motor_5_hex = binascii.unhexlify(motor_5)
    
    #send command
    ser.write(motor_5_hex)
        
    #发送多机同步命令，所有电机同时动作
    print("升降平台上升中...")

def lifting_down(RPM, acc, distance):
    #direction:5-cw-00
    
    #待调试参数pulse，通过调试pulse的取值，得出具体的上升距离和pulse的关系
    pulse = 100000

    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)
    pulse_str = "{:08X}".format(pulse)
    
    motor_5 = "05" + "FD" + "00" + RPM_str + \
                       acc_str + pulse_str + "00006B"#相对位置模式00不启用多机同步00
    
    #把十六进制字符串转换为二进制数据
    motor_5_hex = binascii.unhexlify(motor_5)
    
    #send command
    ser.write(motor_5_hex)
        
    #发送多机同步命令，所有电机同时动作
    print("升降平台下降中...")


def claw_forward(RPM, acc, distance):
    #假设cw是前伸，需要具体调试
    #direction:6-cw-00
    
    #待调试参数pulse，通过调试pulse的取值，得出具体的上升距离和pulse的关系
    pulse = 100000

    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)
    pulse_str = "{:08X}".format(pulse)
    
    motor_6 = "06" + "FD" + "00" + RPM_str + \
                       acc_str + pulse_str + "00006B"#相对位置模式00不启用多机同步00
    
    #把十六进制字符串转换为二进制数据
    motor_6_hex = binascii.unhexlify(motor_6)
    
    #send command
    ser.write(motor_6_hex)
        
    #发送多机同步命令，所有电机同时动作
    print("爪子前伸中...")


def claw_backwards(RPM, acc, distance):
    #direction:6-ccw-01
    
    #待调试参数pulse，通过调试pulse的取值，得出具体的上升距离和pulse的关系
    pulse = 100000

    RPM_str = "{:04X}".format(RPM)
    acc_str = "{:02X}".format(acc)
    pulse_str = "{:08X}".format(pulse)
    
    motor_6 = "06" + "FD" + "01" + RPM_str + \
                       acc_str + pulse_str + "00006B"#相对位置模式00不启用多机同步00
    
    #把十六进制字符串转换为二进制数据
    motor_6_hex = binascii.unhexlify(motor_6)
    
    #send command
    ser.write(motor_6_hex)
        
    #发送多机同步命令，所有电机同时动作
    print("爪子前伸中...")
