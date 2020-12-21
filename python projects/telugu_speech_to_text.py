import speech_recognition as sr
from pyttsx3 import *
import pyperclip
import datetime
while True:
    r = sr.Recognizer()
    try :
        with sr.Microphone() as source :
            print('listening...')
            audio = r.listen(source)
            r.pause_threshold = 5
        try :
            print('Recognizing...')
            query = r.recognize_google(audio, language = 'te-IN')
            print(f'{query}\n')
            pyperclip.copy(query)
        except Exception as e :
            print(e)
            sp('okasaari malli cheppu...')

    except OSError as e :
        print('can\'t detect microphone')
        speak('mike dhorakaledu')
        input('exit')
    except UnicodeError as e :
        sp('This program is not supported here.')