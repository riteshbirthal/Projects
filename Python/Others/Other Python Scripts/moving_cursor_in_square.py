import pyautogui
import time

while True:
    pyautogui.moveRel(500, 0, duration = 2)
    time.sleep(10)
    pyautogui.moveRel(0, 500, duration = 2)
    time.sleep(10)
    pyautogui.moveRel(-500, 0, duration = 2)
    time.sleep(10)
    pyautogui.moveRel(0, -500, duration = 2)
    time.sleep(10)