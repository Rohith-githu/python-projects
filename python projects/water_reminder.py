from plyer import notification
import time
import playsound

while True :
    playsound.playsound(r"C:\Users\rohit\Downloads\ios_notification.mp3")
    notification.notify(
		app_name = 'NXT creators',
        title = 'Drink Water',
        message = 'you have not drinked water from last hour please drink water. And give a gap from screen',
		app_icon = "glass_icon.ico",
        timeout = 10
    )
    time.sleep(60*60)
