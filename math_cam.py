import math

distance = 50
delta_angle = 0

def delta():
    global delta_angle
    global distance
    part = delta_angle / 340
    delta_length = (distance // 2) * part
    delta_angle = round(math.atan(delta_length / distance) * 180)
    return delta_angle