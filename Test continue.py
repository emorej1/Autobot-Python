from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


time.sleep(2)

while pyautogui.locateOnScreen('Next.png', region=(1655,180,26,26),grayscale=True, confidence =0.95) != None:
        print("I can see Next")
else:
    sleep(0.5)
    print("clicked")
    iml = pyautogui.screenshot(region=(1655,180,26,26))
    iml.save(r"C:\Users\j.sherdrack\Documents\Autobots-main\Autobots-main\tests.png")
