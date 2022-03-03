import random
import time

import serial


arduino = serial.Serial(port="COM4", baudrate=9600, timeout=.1)


def get_angle(delta_angle):
    print(delta_angle)
    arduino.write(str(delta_angle).encode('UTF-8'))
    print(f" пришло - {arduino.readline().decode('UTF-8')}")
