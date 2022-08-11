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

while pyautogui.locateOnScreen('Done.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) == None:
                               print("Waiting for Done")
                               freeze() 
                               time.sleep(2)
else:            
                               time.sleep(0.5)
                               click(1768,528)
                               time.sleep(15)
                               click(1873,311) 
