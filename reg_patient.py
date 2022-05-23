import time

import cv2
import pyttsx3
import speech_recognition as sr


class reg_patient:
    def __init__(self):
        self.labels = ['Yaroslav']
        self.engine = pyttsx3.init()

    def start_work(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("face-trainner.yml")

        count_time = 0
        access = 0
        face_cascade_db = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        cap = cv2.VideoCapture(0)

        while access != 1:
            success, img = cap.read()
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)

            for (x, y, w, h) in faces:
                roi_gray = img_gray[y:y + h, x:x + w]
                id_, conf = recognizer.predict(roi_gray)
                if conf >= 80 and count_time <= 50:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = self.labels[id_]
                    cv2.putText(img, name, (x, y), font, 1, (0, 0, 255), 2)
                    self.engine.say('Доступ разрешён, начинаем приём')
                    exit()
                else:
                    self.make_photo_to_db()
                    self.engine.say('Успешная регистрация, начинаем приём')
                    exit()

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                count_time += 1

            cv2.imshow('rez', img)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def make_photo_to_db(self):
        engine = pyttsx3.init()
        engine.say('Давайте сделаем ваши снимки и зарегестрируем вас')
        engine.say(
            'Скажите ваше имя, затем оставляйте лицо фронтально перед камерой в течение 20 секунд немного поворачивая голову')
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
        query = r.recognize_google(audio, language="ru-RU")
        self.labels.append(query)
        cap = cv2.VideoCapture(0)
        for i in range(5):
            ret, img = cap.read()
            cv2.imwrite(f"Face_Images/{self.labels[-1]}{i}.png", img)
            time.sleep(2)
        cap.release()
