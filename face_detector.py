import cv2
import math_cam
import datetime

class Face_detection:
    now_time = datetime.datetime.now().second
    face_cascade_db = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(1)
    delta_x = 0
    delta_y = 0

    def find_face(self):
        while True:
            success, img = self.cap.read()
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade_db.detectMultiScale(img_gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # print(f'Face relative to the center {x + w // 2}, {y + h // 2}')
                # print(f'Max {x + w}, {y + h}')
                self.delta_x = x + w // 2 - 320
                self.delta_y = -(y + h // 2 - 240)
                math_cam.delta_angle = self.delta_x
                print(math_cam.delta())

                #if (datetime.datetime.now().second - self.now_time) % 2 == 0:
                 #   arduino.get_angle(math_cam.delta())
            cv2.imshow('rez', img)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

face = Face_detection()
face.find_face()
