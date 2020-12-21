import pyttsx3
i = 2
while i >= 2:
    engine = pyttsx3.init('sapi5')
    text = input('enter the text to convert >>> ')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', int(175))
    engine.say(text)
    engine.runAndWait()
