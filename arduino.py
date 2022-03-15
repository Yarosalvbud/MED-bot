import random
import time
import math_cam
import serial

arduino = serial.Serial(port="COM6", baudrate=115200, timeout=.1)


def get_angle(delta_angle):
    print(delta_angle)
    arduino.write(str(delta_angle).encode('UTF-8'))


def get_santimetr():
    math_cam.distance = int(arduino.readline().decode('UTF-8'))
    if math_cam.distance == 0:
        math_cam.distance = 50
    print(f"take - {math_cam.distance}")
