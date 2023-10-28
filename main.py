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
unm = "allenjeriel20@gmail.com"                        # Login credentials of our email id
pwd = "cnhcsvzsilyxneqs"
import pyttsx3
from email.message import EmailMessage
from email.header import decode_header
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
    server.login('allenjeriel20@gmail.com', 'cnhcsvzsilyxneqs')
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
        'Derisa': 'kurushnishanth1@gmail.com',
        'Nisanth': 'kurushnishanth1@gmail.com',
        'Nishanth': 'kurushnishanth1@gmail.com',
        'Nishant': 'kurushnishanth1@gmail.com',
        'nikita': 'kurushnishanth1@gmail.com',
        'James': 'kurushnishanth1@gmail.com',
        'james': 'kurushnishanth1@gmail.com',
        'doremon': 'kurushnishanth1@gmail.com'
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
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.starttls()
    # server.login('brightworldprojects@gmail.com', 'jfxgpwqsngvbmygc')
    # email = EmailMessage()
    # email['From'] = 'brightworldprojects@gmail.com'
    # email['To'] = receiver
    # email['Subject'] = subject
    # email.set_content(message)
    # server.send_message(email)

    # rec = "kurushnishanth1@gmail.com"
    #
    #
    # str = "Please speak the body of your email"
    # speak(str)
    # msg = listen()
    #
    # str = "You have spoken the message"
    # speak(str)
    # speak(msg)
    #
    # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server.login(unm, pwd)
    # server.sendmail(unm, rec, msg)
    # server.quit()
    #
    # str = "The email has been Sent"
    # speak(str)
#Dictionary of Emails

def readmail():                                         # Function for Reading email from Inbox

    server = e.connect("imap.gmail.com", unm, pwd)
    server.listids()

    str = "Please say the Serial Number of the email you wanna read starting from latest"
    speak(str)

    a = listen()
    if( a == "Tu"):
        a = "2"

    b = int(a) - 1

    email = server.mail(server.listids()[b])

    str = "The email is from: "
    speak(str)
    speak(email.from_addr)
    str = "The subject of the email is:"
    speak(str)
    speak(email.title)
    str = "The body of email is :"
    speak(str)
    speak(email.body)
def readmail1():
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)  # this is host and port area.... ssl security
    unm = ('brightworldprojects@gmail.com')  # username
    psw = ('jfxgpwqsngvbmygc')  # password
    mail.login(unm, psw)  # login
    stat, total = mail.select('Inbox')  # total number of mails in inbox
    print("Number of mails in your inbox :" + str(total))
    tts = gTTS(text="Total mails are :" + str(total), lang='en')  # voice out
    ttsname = ("total.mp3")  # Example: path -> C:\Users\Sandeep\Desktop> just change with your desktop directory. Don't use my directory.
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
def clean(text):
    """
    clean text for creating a folder
    """
    return "".join(c if c.isalnum() else "_" for c in text)

def getLatestMails():
    """
    Get latest mails from folders in mailbox (Defaults to 3 Inbox mails)
    """
    mailBoxTarget = "INBOX"
    speak(
        "Choose the folder name to get the latest mails. Say 1 for Inbox. Say 2 for Sent Mailbox. Say 3 for Drafts. Say 4 for important mails")
    cmb = listen()
    if cmb == "1" or cmb.lower() == "one":
        mailBoxTarget = "INBOX"
        speak("Inbox selected.")
    elif cmb == "2" or cmb.lower() == "two" or cmb.lower() == "tu":
        mailBoxTarget = '"[Gmail]/Sent Mail"'
        speak("Sent Mailbox selected.")
    elif cmb == "3" or cmb.lower() == "three":
        mailBoxTarget = '"[Gmail]/Drafts"'
        speak("Drafts selected.")
    elif cmb == "4" or cmb.lower() == "four":
        mailBoxTarget = '"[Gmail]/Important"'
        speak("Important Mails selected.")
    # elif cmb == "5" or cmb.lower() == "five":
    #     mailBoxTarget = '"[Gmail]/Spam"'
    #     speak("Spam selected.")
    # elif cmb == "6" or cmb.lower() == "six":
    #     mailBoxTarget = '"[Gmail]/Starred"'
    #     speak("Starred Mails selected.")
    # elif cmb == "7" or cmb.lower() == "seven":
    #     mailBoxTarget = '"[Gmail]/Bin"'
    #     speak("Bin selected.")
    else:
        speak("Wrong choice. Hence, default option Inbox wil be selected.")
    #
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(unm, pwd)

    status, messages = imap.select(mailBoxTarget)

    messages = int(messages[0])

    if messages == 0:
        speak("Selected MailBox is empty.")
        return None
    elif messages == 1:
        N = 1  # number of top emails to fetch
    elif messages == 2:
        N = 2  # number of top emails to fetch
    else:
        N = 3  # number of top emails to fetch

    msgCount = 1
    for i in range(messages, messages - N, -1):
        speak(f"Message {msgCount}:")
        res, msg = imap.fetch(str(i), "(RFC822)")  # fetch the email message by ID
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])  # parse a bytes email into a message object

                subject, encoding = decode_header(msg["Subject"])[0]  # decode the email subject
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding)  # if it's a bytes, decode to str

                From, encoding = decode_header(msg.get("From"))[0]  # decode email sender
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                speak("Subject: " + subject)
                FromArr = From.split()
                FromName = " ".join(namechar for namechar in FromArr[0:-1])
                speak("From: " + FromName)
                speak("Sender mail: " + FromArr[-1])
                speak("The mail says or contains the following:")

                # MULTIPART
                if msg.is_multipart():
                    for part in msg.walk():  # iterate over email parts
                        content_type = part.get_content_type()  # extract content type of email
                        content_disposition = str(
                            part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()  # get the email body
                        except:
                            pass

                        # PLAIN TEXT MAIL
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            speak("Do you want to listen to the text content of the mail ? Please say YES or NO.")
                            talkMSG1 = listen()
                            if "yes" in talkMSG1.lower():
                                speak("The mail body contains the following:")
                                speak(body)
                            else:
                                speak("You chose NO")
                # NOT MULTIPART
                else:
                    content_type = msg.get_content_type()  # extract content type of email
                    body = msg.get_payload(decode=True).decode()  # get the email body
                    if content_type == "text/plain":
                        speak("Do you want to listen to the text content of the mail ? Please say YES or NO.")
                        talkMSG2 = listen()
                        if "yes" in talkMSG2.lower():
                            speak("The mail body contains the following:")
                            speak(body)
                        else:
                            speak("You chose NO")

                speak(f"\nEnd of message {msgCount}:")
                msgCount += 1
                print("=" * 100)
    imap.close()
    imap.logout()
def main():
    str = "Welcome to voice controlled email service"
    speak(str)
    while (1):
        str = "What do you want to do?"
        speak(str)

        str = "Speak SEND to Send email    Speak READ to Read Inbox  Speak latest to lates Inbox  Speak EXIT to Exit"
        speak(str)

        ch = listen()

        if (ch == 'send' or ch == 'send email' or ch == 'send mail'):
            str = "You have chosen to send an email"
            speak(str)
            sendmail()

        elif (ch == 'read' or ch == 'read email' or ch == 'read mail' ):
            str = "You have chosen to read email"
            speak(str)
            readmail1()
        elif (ch == 'latest' or ch == 'latest email' or ch == 'latest mail'or ch == 'laytest' ):
            getLatestMails()
        elif (ch == 'youtube' or ch == 'YouTube'):
            webbrowser.open('youtube.com')
        elif (ch == 'google' or ch == 'Google'):
            webbrowser.open('google.com')
        elif (ch == 'play music' or ch == 'music'):
            music_dir = filedialog.askdirectory()
            songs = os.listdir(music_dir)
            # for i in range(len(songs)):
            #     print(str(songs[i])+' ',end=' \n ')
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs))]))
        elif (ch == 'exit' or ch == 'EXIT'):
            str = "You have chosen to exit, bye bye"
            speak(str)
            exit(1)

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

button = Button(GUI, text="TOUCH", padx=40, pady=50 ,command=main)
button.place(x= 272, y= 139)       # giving the location of the button

GUI.mainloop()                    # infinte loop used to run the application



