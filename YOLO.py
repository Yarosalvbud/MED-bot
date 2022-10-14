import torch
import cv2
import numpy
import torchvision
import yaml
import tqdm

model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)
model.classes = [0]

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    results = model(frame)
    cv2.imshow('YOLO', numpy.squeeze(results.render()))

    if cv2.waitKey(10) & 0xff == ord('q'):
        break


