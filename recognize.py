from os import remove
import speech_recognition as sr
from pydub import AudioSegment

def Recognizer(mp3_file):
    #convert to wav
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export("1.wav", format="wav")

    r = sr.Recognizer()
    with sr.AudioFile("1.wav") as source:
        #r.adjust_for_ambient_noise(source)
        audio_data = r.record(source)#,offset=8,duration=10)
        recognize=r.recognize_google(audio_data,language = 'vi-IN', show_all = True )
        print(recognize)

    remove("1.wav")

mp3_file='12.wav'

Recognizer(mp3_file)