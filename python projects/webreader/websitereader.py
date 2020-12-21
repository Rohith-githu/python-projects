fimport requests, bs4, pyttsx3, webbrowser
from gtts import gTTS
try : 
    url = input("enter the url of the website to get the text from: ")
    try :
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        hi = soup.select('div')
        hititle = soup.select('title')
        webtext = hi[0].getText()
        webtitle = hititle[0].getText()
    except Exception as e:
        print('url not found')
    engine = pyttsx3.init()
    ask = input('how do you want to run the file (speak/file): ')
    if 'speak' in ask:
        print(webtext)
        engine.say(webtitle)
        engine.say(hi[0].getText())
        engine.runAndWait()
    elif 'file' in ask:
        tts = gTTS(webtext)
        tts.save(f'{webtitle}.mp3')
        print(f'the audio file is saved as {webtitle}')
except Exception as e:
    print('something went wrong')