import speech_recognition as sr
from playsound import playsound
import os

# 1. 마이크객체
r = sr.Recognizer()
with sr.Microphone() as source:
    print("아무말이나 해 보삼!!")
    audio = r.listen(source)

# 2. mp3 파일을 저장
filename = './stt_tts/stt_result.mp3'
with open(filename, 'wb') as f:
    f.write(audio.get_wav_data())

playsound(filename)
os.remove(filename)
