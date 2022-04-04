import cv2
import math_cam
#import arduino
import datetime


class Face_detection:
    now_time = datetime.datetime.now().second
    face_cascade_db = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    face_cascade_ff = cv2.CascadeClassifier("haarcascade_profileface.xml")
    cap = cv2.VideoCapture(0)
    delta_x = 0
    delta_y = 0

    def find_face(self):
        count_res = datetime.datetime.now().second
        while True:
            success, img = self.cap.read()
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade_db.detectMultiScale(img_gray, 1.1, 19)

            if len(faces) != 0:
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    self.delta_x = x + w // 2 - 320
                    self.delta_y = -(y + h // 2 - 240)
                    math_cam.delta_angle = self.delta_x
                    if (datetime.datetime.now().second - self.now_time) % 1.5 == 0 and datetime.datetime.now().second != count_res:
                        count_res = datetime.datetime.now().second
                        #arduino.get_angle(math_cam.delta())
                        #arduino.get_santimetr()

            else:
                face_f = self.face_cascade_ff.detectMultiScale(img_gray, 1.1, 19)
                if len(face_f) == 0:
                    f_f = cv2.flip(img_gray, 1)
                    face_ff = self.face_cascade_ff.detectMultiScale(f_f, 1.1, 19)
                    for (x, y, w, h) in face_ff:
                        cv2.rectangle(img, (x + w, y), (x, y + h), (0, 255, 0), 2)
                        self.delta_x = x + w // 2 - 320
                        self.delta_y = -(y + h // 2 - 240)
                        math_cam.delta_angle = self.delta_x
                        if (
                                datetime.datetime.now().second - self.now_time) % 1.5 == 0 and datetime.datetime.now().second != count_res:
                            count_res = datetime.datetime.now().second
                            # arduino.get_angle(math_cam.delta())
                            # arduino.get_santimetr()
                else:
                    for (x, y, w, h) in face_f:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        self.delta_x = x + w // 2 - 320
                        self.delta_y = -(y + h // 2 - 240)
                        math_cam.delta_angle = self.delta_x
                        if (datetime.datetime.now().second - self.now_time) % 1.5 == 0 and datetime.datetime.now().second != count_res:
                            count_res = datetime.datetime.now().second
                            #arduino.get_angle(math_cam.delta())
                            #arduino.get_santimetr()


            cv2.imshow('rez', img)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()


face = Face_detection()
face.find_face()