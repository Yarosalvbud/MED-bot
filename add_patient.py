import cv2
import numpy as np
import os


class add_patient:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.Face_Images = os.path.join(os.getcwd(), "Face_Images")

    def reg_new_people(self):
        Face_ID = -1
        pev_person_name = ""
        y_ID = []
        x_train = []
        for root, dirs, files in os.walk(self.Face_Images):
            for file in files:
                if file.endswith("jpeg") or file.endswith("jpg") or file.endswith("png"):
                    path = os.path.join(root, file)
                    person_name = file.split('.')[0]
                    path = path[41:]

                    if pev_person_name != person_name:
                        Face_ID = Face_ID + 1
                        pev_person_name = person_name
                    Gery_Image = cv2.imread(path)
                    Gery_Image = cv2.cvtColor(Gery_Image, cv2.COLOR_BGR2GRAY)
                    Gery_Image = cv2.resize(Gery_Image, (800, 800), interpolation=cv2.INTER_LANCZOS4)
                    Final_Image = np.array(Gery_Image, "uint8")
                    faces = self.face_cascade.detectMultiScale(Final_Image, scaleFactor=1.5, minNeighbors=5)

                    for (x, y, w, h) in faces:
                        roi = Final_Image[y:y + h, x:x + w]
                        x_train.append(roi)
                        y_ID.append(Face_ID)
        self.recognizer.train(x_train, np.array(y_ID))
        self.recognizer.save("face-trainner.yml")

