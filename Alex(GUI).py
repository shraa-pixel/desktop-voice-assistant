import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import tkinter as tk
from tkinter import scrolledtext
# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    elif hour < 20:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("Hello, I am Alex. Please tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Say something!")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        return "None"

def chooseBrowser():
    speak("Which browser would you like to use? You can choose Chrome or Edge.")
    browser_choice = takeCommand().lower()
    if 'chrome' in browser_choice or 'open chrome' in browser_choice:
        return 'chrome'
    elif 'edge' in browser_choice or 'open microsoft edge' in browser_choice:
        return 'edge'
    else:
        speak("Sorry, I didn't get that. Using default browser.")
        return 'default'

def openWithBrowser(url):
    browser = chooseBrowser()
    speak("Opening browser...")
    try:
        if browser == 'chrome':
            webbrowser.get('chrome').open(url)
        elif browser == 'edge':
            webbrowser.get('edge').open(url)
        else:
            webbrowser.open(url)
    except Exception as e:
        speak("Sorry, I couldn't open the browser.")
        print(e)
        
def update_chat(message):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, message)
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        update_chat("Assistant: Listening... Say something!")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        update_chat(f"You: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        update_chat("Assistant: Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        update_chat("Assistant: Could not request results; check your network connection.")
        return None

def respond(query):
    if query is None:
        return

    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            update_chat("Assistant: " + result + "\n")
            speak(result)
        except Exception as e:
            speak("Sorry, I couldn't find any information on that topic.")
            print(e)
            
def set_speaking_rate(rate):
    engine.setProperty('rate', rate)

def execute_command():
    query = listen()
    respond(query)

# Create the main window
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("400x500")

# Create a scrolled text area for chat
chat_box = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD)
chat_box.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create a button to start listening
listen_button = tk.Button(root, text="Start Listening", command=execute_command)
listen_button.pack(pady=10)

# Set speaking rate
set_speaking_rate(150)

# Start the greeting
wishMe()

# Run the Tkinter event loop
root.mainloop()

def tell_joke():
    jokes = [
        "Name the kind of tree you can hold in your hand? A palm tree!",
        "What did the left eye say to the right eye? Between us, something smells!",
        "What social events do spiders love to attend? Webbings.",
        "What is a room with no walls? A mushroom.",
        "Why was six afraid of seven? Because seven eight nine.",
        "What’s a dog’s favorite homework assignment? A lab report."
    ]
    
    joke_index = random.randint(0, len(jokes) - 1)
    joke = jokes[joke_index]
    speak(joke)

def set_speaking_rate(rate):
    engine.setProperty('rate', rate)

def main():
    set_speaking_rate(150)
    
    # Register browsers
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
    except Exception as e:
        print(f"Error during registering browsers: {e}")

    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            except Exception as e:
                speak("Sorry, I couldn't find any information on that topic.")
                print(e)
                
        elif 'show trending news' in query:
            openWithBrowser("https://timesofindia.indiatimes.com/")
                
        elif 'open google' in query:
            openWithBrowser("https://www.google.com")
            
        elif 'open youtube' in query:
            openWithBrowser("https://www.youtube.com")
        
        elif 'what' in query and 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'tell me a joke' in query or 'joke' in query:
            tell_joke()
        
        elif 'open word' in query:
            word_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(word_path)
            speak("Opening Word")
            
        elif 'open powerpoint' in query:
            powerpoint_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(powerpoint_path)
            speak("Opening PowerPoint")
            
        elif 'open excel' in query:
            excel_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            os.startfile(excel_path)
            speak("Opening Excel")
            
        elif 'openNote' in query:
            open_Note = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote.lnk"
            os.startfile(open_Note)
            speak("Opening OneNote")

        elif "play music" in query or "play song" in query:
            music_path = "C:\\Users\\ASUS\\OneDrive\\Desktop\\nikita dance.mp3"
            os.startfile(music_path)
            speak("Playing music")
            
        elif 'open files' in query or 'show my files' in query:
            my_files = "C:\\Program Files"
            os.startfile(my_files)
            speak("Opening files")
            
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break

        elif 'thank u' in query:
            speak("You're welcome. Feel free to ask anything...")

if __name__ == "__main__":
    main()
