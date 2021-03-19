import time
import os
def screentime():
    """
    This program will shutdown your pc after 4 hours of screen time
"""
    from pyttsx3 import speak
    speak('Hi There your screentime had started')
    time.sleep(4*60*60)
    speak('your screen time has ended')

