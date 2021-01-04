import pyperclip, pyttsx3
from gtts import gTTS

ask = input('Choose a action (instant/save): \n')
if 'in' in ask:
	engine = pyttsx3.init()
	engine.say(pyperclip.paste())
	engine.runAndWait()
elif 'sa' in ask:
	try :
		tts = gTTS(pyperclip.paste())
		tts.save('instant.mp3')
		pyttsx3.speak('file saved successfully')
	except:
		print('some error occurred')
		speak('some error occurred')