import smtplib
import speech_recognition as sr
import pyttsx3
from sys import exit
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.pause_threshold = 1
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
     pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('miniprojectcsbs@gmail.com', 'Miniproject@cs&bs')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'blue': 'sanjaysundar60@gmail.com',
    'black': 'mohammedriyaz2124@gmail.com',
    'yellow': 'gowthamneymar97@gmail.com',
    'white': 'itsmhmdali@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Your email has been sent')
    print('Your email has been sent')
    talk('Do you want to send more email?')
    print('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    if 'no' in send_more:
        talk('Thank you for using E mail bot')
        print('Thank you for using E mail bot')
        exit(0)


talk('Hi I am E mail bot, your email assistant')
print('Hi I am E mail bot, your email assistant')
get_email_info()
