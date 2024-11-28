from tkinter import*
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess

root= Tk()
root.geometry('500x500')
root.config(bg = "#F2CCC3")
engine = pyttsx3.init()

# Set the voice and speaking rate
engine.setProperty('voice', 'english')
engine.setProperty('rate', 150)

# Speak the text
engine.say("Hello")

# Run and wait for completion
engine.runAndWait()
label_heading= Label(root,text= "Welcome To Your Desktop Assistant",fg="black", font=("Arial",30,"bold"),bg = "#F2CCC3")
label_heading.place(relx=0.5, rely=0.1,anchor=CENTER)

begin=pyttsx3.init()

def speak(speak_data):
    begin.say(speak_data)
    begin.runAndWait()


def r_audio():
    speech_recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recogniser.listen(source)
        voice_data= ''
        try:
            voice_data= speech_recogniser.recognise_google(audio, language ='en-in')
        except sr.UnknownValueError:
            print("I could not understand , Please Repeat that you said.")
    print(voice_data)


def respond_to_user(voice_data):
    if 'name' in voice_data:
        speak("My name is Amulya")
        print("My name is Amulya")
    if 'time' in voice_data:
        speak("Current Time is")
        now= datetime.now()
        current_time= now.strftime('%H:%M:%S')
        speak(current_time)
        print(current_time)
    if 'search' in voice_data:
        speak("Opening Microsoft Edge")
        print("Opening Microsoft Edge")
        webbrowser.get().open("https://www.bing.com/")
    if 'video' in voice_data:
        speak("Opening Youtube")
        print("Opening Youtube")
        webbrowser.get().open("https://www.bing.com/")
    if 'text editor' in voice_data:
        speak("Opening Note Pad")
        print("Opening Note Pad")
        subprocess.Popen("Notepad.exe")
    if 'Play' in voice_data:
        speak("Opening Game")
        print("Opening Game")
        subprocess.Popen("Roblox Player.exe")
    


button_open= Button(root,text="Start",command= r_audio)
button_open.place(relx=0.5,rely=0.95 , anchor= CENTER)

root.mainloop()