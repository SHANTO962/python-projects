import pyautogui
import time


time.sleep(0.5)
text = " I LOVE YOU "
while True:
    pyautogui.typewrite(text)

    time.sleep(0.5)
    pyautogui.press('enter')
    
