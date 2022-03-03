import math


delta_angle = 0

def delta():
    global delta_angle
    part = delta_angle / 340
    distance = 50  # distance between the camera and a face (might change)
    # camera_angle = 26.57  # deg (arc-tan(1/2))
    delta_length = (distance // 2) * part
    delta_angle = round(math.atan(delta_length / distance) * 180) // 2
    return delta_angle




