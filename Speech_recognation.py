import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile("") as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="ru-RU")
        print("Вы сказали : {}".format(text))
    except:
        print("Извините я не понял что вы сказали")