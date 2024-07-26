import pyttsx3 as sx3
import speech_recognition as sr
import webbrowser
import time

wel = sx3.init()
voices = wel.getProperty('voices')
print('voice',voices[0].id)

def speak(audio):
    wel.say(audio)
    wel.runAndWait()

def take_command():
    command = sr.Recognizer()
    with sr.Microphone() as mic:
        print('say commands sir...')
        command.phrase_threshold = 1
        audio = command.listen(mic)
        try:
            print('Recording...')
            query = command.recognizer_google(audio, language = 'en')
            print(f'you said : {query}')
        except Exception as Error:
            return None
        return query.lower()

speak('Hello Mr Ahmed , say your commands please')

while True:
    query = take_command()
    if 'hello' in query:
        speak(' Hello Mr Ahmed ')
    if 'how are you' in query:
        speak(' am fine Mr , and you')
    if 'open google' in query:
        speak('ok sir')
        time.sleep(3)
        webbrowser.open_new_tab('https://www.google.com')
