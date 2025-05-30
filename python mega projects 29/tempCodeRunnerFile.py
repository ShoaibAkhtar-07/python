import speech_recognition as sr
import webbrowser
import pyttsx3

r= sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processcommand(s):
    print(s)
if __name__ =="__main__":
    speak("--initilizing jarvis--")
    while True:
        # Use the microphone
        # Recognize using Google
        try:
            with sr.Microphone() as source:
              print("LISTENING...")
              audio = r.listen(source,timeout=2,phrase_time_limit=1)
              print("Processing...")
            word = r.recognize_google(audio)
            if(word.lower() =="jarvis"):
                speak("ya")
                print("JARVIS IS LISTENING")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                processcommand(command)
                
                
        except Exception as e:
            print("Could not request results; {0}".format(e))