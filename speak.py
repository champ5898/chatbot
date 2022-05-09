# from win32com.client import Dispatch
# from gtts import gTTS
# import os
# import speech_recognition as sr
import pyttsx3
# def speak(str):
    

#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(str)


# def tts(txt):
#     output=gTTS(text=txt, lang='en', slow=False)
#     output.save("voice.mp3")

def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()
if __name__ == "__main__":
    # speak("You are the best")
    SpeakText("hey there")