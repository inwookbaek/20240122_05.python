import speech_recognition as sr
from pydub import AudioSegment
from playsound import playsound
import os

# 1. 마이크객체
r = sr.Recognizer()
with sr.Microphone() as source:
    print("아무말이나 해 보삼!!")
    audio = r.listen(source)

# 2. WAV 파일로 저장
filename_wav = './stt_result.wav'
with open(filename_wav, 'wb') as f:
    f.write(audio.get_wav_data())

# 3. WAV 파일을 MP3로 변환
filename_mp3 = './stt_result.mp3'
sound = AudioSegment.from_wav(filename_wav)
sound.export(filename_mp3, format="mp3")

# 4. MP3 파일 재생
playsound(filename_mp3)

# 5. 파일 삭제
os.remove(filename_wav)
os.remove(filename_mp3)
