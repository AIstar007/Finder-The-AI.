import datetime
import speech_recognition as sr
import wikipedia
import pyttsx3
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Finder, please tell me how can I help you")


def textCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("listening")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        question = r.recognize_google(audio, language='en-in')
       # question = r.recognize_google(audio, language='en-in')
        print(f"User said: {question}\n")

    except Exception as e:
        # print(e)
        print("Say that again please")
        speak("please say that again")
        return "none"
    return question

    # Send Email function


def sendEmail(to, content):  # First you have to enable "Less secure Apps"

    # Create a SMTP object for connection with server
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()  # to identify itself when connecting to another email server to start the process of sending an email

    # TLS connection required by gmail
    server.starttls()  # to turn an existing insecure connection into a secure one

    server.login(input("Enter your Email : "), input(
        "Enter your Password : "))  # Your Email and Password

    server.sendmail(input("Enter sender Email : "),
                    to, content)  # Sender Email

    server.close()  # Close the server

wish()

while True:
    question = textCommand().lower()
    if 'wikipedia' in question:
        speak("Searching Wikipedia...")
        question = question.replace("wikipedia", "")
        results = wikipedia.summary(question, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in question:
        webbrowser.open("youtube.com")
    elif 'open google' in question:
        webbrowser.open("google.com")
    elif 'my name' in question:
        speak(question)
        print(speak)
    elif 'time' in question:
        hour = str(int(datetime.datetime.now().hour))
        min = str(int(datetime.datetime.now().minute))
        time = (hour+"hours"+min+"minutes")
        speak(time)
    elif 'date' in question:
        date = str(int(datetime.datetime.now().day))
        mon = str(datetime.datetime.now().month)
        year = str(int(datetime.datetime.now().year))
        speak(date)
        speak(mon)
        speak(year)
    elif 'your name' in question:
        speak("My name is Finder")
        print(speak)
    elif 'open google' in question:
        webbrowser.open("google.com")
    elif 'tomorrow' in question:
        date = str(int(datetime.datetime.now().day) + 1)
        speak(date)
    elif 'is this a leap year' in question:
        year = int(datetime.datetime.now().year)
        l = year % 4
        if l == 0:
            print("Leap-Year")
            speak("Yes this is a leap year")
        else:

            print("Not a Leap-Year")
            speak("No this is not a leap year")   
    elif 'open instagram' in question:
        webbrowser.open('instagram.com')
    
    elif 'email to' in question:
        try:
            name = list(question.split())  # extract receiver's name
            name = name[name.index('to') + 1]
            speak("What should I say sir?")
            content = takeCommand()
            to = dict[name]  # Your email address
            sendEmail(to, content)
            print("Email has been sent!")
            speak("Email has been sent!")
        except Exception as e:
            # print(e)  # Print the exception for debugging
            print("Failed to send Email!")
            speak("Sorry sir, I have failed to send the email")
    elif 'email to' in question:
        try:
            name = list(question.split())  # extract receiver's name
            name = name[name.index('to') + 1]
            speak("What should I say sir?")
            content = takeCommand()
            to = dict[name]  # Your email address
            sendEmail(to, content)
            print("Email has been sent!")
            speak("Email has been sent!")
        except Exception as e:
            # print(e)  # Print the exception for debugging
            print("Failed to send Email!")
            speak("Sorry sir, I have failed to send the email")
    elif 'who are you' in question:
        print("I am Finder. An AI Featured Destop Assistant")
        speak("I am Finder. An AI Featured Destop Assistant")
    elif 'How are you' in question:
        print("I am well sir, How are you")
        speak("I am well sir, How are you")

    elif 'i am well' in question:
        print("Have a nice day sir")
        speak("Have a nice day sir")

    elif 'i am not well' in question:
        print("Sorry about that sir, may you recover soon")
        speak("Sorry about that sir, may you recover soon")
    elif 'exit' in question:
        print("Exiting...")
        exit()

    elif 'quit' in question:
        print("Quitting...")
        exit()

     


