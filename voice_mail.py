import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib
from tkinter import *                                 # For creating GUI
import PIL                                            # For image processing
from PIL import ImageTk
from PIL import Image
import datetime
import wikipedia
import webbrowser
import os
import random
from tkinter import filedialog
import email
import imaplib
from gtts import gTTS
import pyglet
import  time
unm = "maildid"                        # Login credentials of our email id
pwd = "apppassword"
import pyttsx3
from email.message import EmailMessage
r = sr.Recognizer()

engine = pyttsx3.init()                                 # Defining an engine for text to speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(str):                                         # Function for text to speech
    print(str)
    engine.say(str)
    engine.runAndWait()
def listening():
    text = ''
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            audio=r.listen(source)
            try:
                print("converting....")
                text=r.recognize_google(audio)
                print(text)
                return text
            except:
                print("You are not audible, try again:")
def listen():                                           # function for speech to text
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak Now:"
        speak(str)
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "Sorry could not recognize what you said"
            speak(str)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        wishes = "Good Morning"
    elif hour >= 12 and hour < 18:
        wishes = "Good Afternoon"
    else:
        wishes = "Good Evening"

    speak(wishes)
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('brightworldprojects@gmail.com', 'jfxgpwqsngvbmygc')
    email = EmailMessage()
    email['From'] = 'brightworldprojects@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
def sendmail():                                         # Function to send email
    speak('To Whom you want to send email')
    email_list = {
        'Derisha': 'sweetlinderisha@gmail.com',
        'derisha': 'sweetlinderisha@gmail.com',
    }
    name = listen()
    receiver = email_list[name]
    # email-id of the name
    print(receiver)
    speak('What is the subject of your email?')
    subject = listen()
    speak('Tell me the text in your email')
    message = listen()
    # Send email
    send_email(receiver, subject, message)
    speak('Your email is sent successfully !!')

def main():
    str = "Welcome to voice controlled email service"
    speak(str)
    while (1):
        str = "What do you want to do?"
        speak(str)

        str = "Speak SEND to Send email    Speak READ to Read Inbox   Speak EXIT to Exit"
        speak(str)

        ch = listen()

        if (ch == 'send' or ch == 'send email' or ch == 'send mail'):
            str = "You have chosen to send an email"
            speak(str)
            sendmail()
        else:
            str = "Invalid choice, you said:"
            speak(str)
            speak(ch)
wishMe()
GUI= Tk()
GUI.title("Voice_Based_Mail_Service")                           # Title of the page of size 626*375
GUI.geometry("626x375")


# importing jpf file stored in download folder

img= ImageTk.PhotoImage(Image.open("voice1.jpg"))
label = Label(image=img)
label.pack()

print("GUI EXECUTED")


# creating button with some customization

button = Button(GUI, text="TOUCH", padx=100, pady=100 ,command=main)
button.place(x= 272, y= 139)       # giving the location of the button
GUI.mainloop()                    # infinte loop used to run the application



