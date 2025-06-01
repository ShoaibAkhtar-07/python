import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def processcommand(s):
    s = s.lower().strip()

    if s == "open google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")
    elif s == "open youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")
    elif s == "open github":
        speak("Opening GitHub")
        webbrowser.open("https://github.com/")
    elif s == "open linkedin":
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com/")
    elif s == "can you hear the music":
        speak("Yes, I can")
        webbrowser.open("https://www.youtube.com/watch?v=LYigiwbaX_U&pp=ygUWY2FuIHlvdSBoZWFyIHRoZSBtdXNpYw%3D%3D")
    elif s.startswith("play"):
        song = s.replace("play", "").strip()
        if song in musiclibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musiclibrary.music[song])
        else:
            speak(f"Sorry, I couldn't find the song: {song}")
    elif s == "news":
        response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=b92aba363afe41b78c4806a2cd2aab46")
        # Check response
        if response.status_code == 200:
           data = response.json()
           articles = data.get("articles", [])
           for article in articles :
              speak(article["title"])
        else:
           print("Failed to fetch news")

    else:
        speak("Sorry, I don't know how to do that.")

if __name__ == "__main__":
    speak("~~~ Initializing jarvis ~~~")
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                word = r.recognize_google(audio)
                print(f"You said: {word}")

            if word.lower() == "jarvis":
                speak("yes? How can I help you?")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Listening for command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")
                    processcommand(command)
                    
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
        except sr.RequestError as e:
            speak(f"API error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")