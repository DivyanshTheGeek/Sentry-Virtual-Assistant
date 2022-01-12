# pyttsx3 is a python library that helps us to convert text into speech.
import pyttsx3
import datetime  # datetime is a python library to access current date and time
import speech_recognition as sr  # Google API Client Library for Python
# Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia
import wikipedia
# The webbrowser module provides a high-level interface to allow displaying web-based documents to users
import webbrowser
import os  # The python OS module provides functions to use operating system dependant functionalities
import smtplib  # smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP
# The sys module provides various functions and variables that are used to manipulate different parts of the Python runtime environment
import sys
# sapi5 is a Microsoft developed speech API that helps in synthesis and recognition of voice
engine = pyttsx3.init('sapi5')
# getting details of current voice from the system
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def talk(audio):
    # This function takes a string as an input and converts it into audio as output
    engine.say(audio)
    engine.runAndWait()


def wishAndIntroduce():
    # This function lets Sentry wish you based on the time and introduce itself
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Hello, Good Morning")
        talk("Hello, Good Morning")
    elif hour >= 12 and hour < 16:
        print("Hello, Good afternoon")
        talk("Hello, Good afternoon")
    else:
        print("Hello, Good evening")
        talk("Hello, Good evening")
    print("I am your virtual assistant Sentry. How can I help you?")
    talk("I am your virtual assistant Sentry. How can I help you?")


def takeCommand():
    # This function takes input from microphone and returns a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:  # In case the voice is not understood by the program
        print(e)
        print("Say that again please....")
        talk("Say that again please....")
        return "None"
    return query


def sendEmail(receiverEmailAddress, emailContent):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email_address', 'your_password') # your_email_address means the Email address of the sender and your_password means the password of the sender's Email account
    server.sendmail('your_email_address',
                    receiverEmailAddress, emailContent)
    server.close()


def quit_assistant(query):
    if 'quit' in query:
        print("Quitting....Thanks for your time!")
        talk("Quitting....Thanks for your time")
        sys.exit()
    elif 'turn off' in query:
        print("Turning off....Thanks for your time!")
        talk("Turning off....Thanks for your time")
        sys.exit()


def assistant_tasks(query):
    # Logic to execute tasks based on query
    desktop_apps_path = {'telegramPath': "C:\\Users\\divya\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe",
                         'chromePath': "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                         'codePath': "C:\\Users\\divya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
                         'wordPath': "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"}
    websites_address = {'youtube': 'youtube.com', 'google': 'www.google.co.in', 'college website': 'skit.org.in',
                        'weather': 'https://www.google.com/search?q=weather'}
    if 'wikipedia' in query:
        talk('Searching Wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        talk("According to Wikipedia")
        print(results)
        talk(results)
    elif 'open telegram' in query:
        os.startfile(desktop_apps_path.get('telegramPath'))
    elif 'open chrome' in query:
        os.startfile(desktop_apps_path.get('chromePath'))
    elif ('open' and 'code') in query:
        os.startfile(desktop_apps_path.get('codePath'))
    elif ('open' and 'word') in query:
        os.startfile(desktop_apps_path.get('wordPath'))
    elif 'open youtube' in query:
        webbrowser.open(websites_address.get('youtube'))
    elif 'open google' in query:
        webbrowser.open(websites_address.get('google'))
    elif 'college website' in query:
        webbrowser.open(websites_address.get('college website'))
    elif 'weather' in query:
        webbrowser.open(websites_address.get('weather'))
    elif ('search' and 'on google') in query:
        query = query.replace("on google", "")
        query = query.replace("search", "")
        webbrowser.open("https://www.google.com/search?q=" + query)
    elif ('search' and 'on youtube') in query:
        query = query.replace("on youtube", "")
        query = query.replace("search", "")
        webbrowser.open(
            "https://www.youtube.com/results?search_query=" + query)
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        talk(f"It is {strTime}")
    elif ('date today' in query or 'today\'s date' in query):
        strDate = datetime.date.today()
        print(strDate)
        talk(f"Today's date is {strDate}")
    elif ('send' and 'email') in query:
        try:
            talk("Who do you want to email?")
            receiverEmailAddress = input()
            talk("What do you want to send?")
            emailContent = takeCommand()
            sendEmail(receiverEmailAddress, emailContent)
            print("The E-mail has been sent!")
            talk("The email has been sent!")
        except Exception as e:
            print(e)
            talk("Sorry, The email could not be sent due to an error!")
    elif ('how are you' in query or 'how you doing' in query):
        talk("I am splendid, Thank you for asking. I hope you're doing well too. What can I do for you?")
    elif ("what's your name" in query or "what is your name" in query):
        print("I am Sentry, your personal assistant!")
        talk("I am Sentry, your personal assistant!")
    elif ("i love you" in query):
        talk("It is hard to understand. I like to be away from such complicated matters")
    elif ('you can do' in query or 'can you do' in query):
        print("I can open applications on your desktop or I can search anything for you on Google or Youtube.\nI can fetch results from wikipedia or I can even send an E-mail to someone on your behalf.")
        talk("I can open applications on your desktop or I can search anything for you on Google or Youtube.\nI can fetch results from wikipedia or I can even send an E-mail to someone on your behalf.")
    else:
        pass


if __name__ == "__main__":  # The program starts executing from here
    wishAndIntroduce()
    while True:
        query = takeCommand().lower()
        if ('quit' in query or 'turn off' in query):
            quit_assistant(query)
        else:
            assistant_tasks(query)
