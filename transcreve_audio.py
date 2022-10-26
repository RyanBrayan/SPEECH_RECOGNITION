from email.mime import audio
from fileinput import filename
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import recebe_audio
import sys


def cria_audio(frase):
    tts = gTTS(frase,lang='pt-br')
    #Salva o arquivo de audio
    tts.save('hello.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('hello.mp3')
    
    

frase = recebe_audio.ouvir_microfone()
cria_audio(frase)