import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Jarvis: {text}")
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
    elif s.startswith("play"):
        song = s.replace("play", "").strip()
        if song in musiclibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musiclibrary.music[song])
        else:
            speak(f"Sorry, I couldn't find the song: {song}")
    else:
        speak("Sorry, I don't know how to do that.")

if __name__ == "__main__":
    speak("~~~ Initializing Jarvis ~~~")
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
                word = r.recognize_google(audio)
                print(f"You said: {word}")

            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Listening for command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")
                    processcommand(command)
                    
        except Exception as e:
            print(f"Unexpected error: {e}")
