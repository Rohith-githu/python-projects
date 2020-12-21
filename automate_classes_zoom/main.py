import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime
def sign_in(meeting_id, password) :
    subprocess.call("C:\\Users\\rohit\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    time.sleep(5)
    meeting_button = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(meeting_button)
    pyautogui.click()

    meeting_id_screen = pyautogui.locateCenterOnScreen('meeting_id_input.png')
    pyautogui.moveTo(meeting_id_screen)
    pyautogui.click()
    pyautogui.write(meeting_id)

    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # passcode = pyautogui.locateCenterOnScreen('passcode.png')
    # pyautogui.moveTo(passcode)
    # pyautogui.click()
    # pyautogui.write(password)

id_meeting = input("Enter the meeting id ")
password = input("Enter the password ")
sign_in(id_meeting, password)