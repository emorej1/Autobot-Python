from pyautogui import *
import pyautogui
import pygetwindow
import time
import keyboard
import random
import win32api, win32con
import subprocess
import psutil

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

mapCount = 0

while mapCount < 200:
        if pyautogui.locateOnScreen('c1-4-1.png', region=(1000,60,920,500),grayscale=True, confidence =0.98) != None:
            print('i can see 1')
        elif pyautogui.locateOnScreen('c1-5-2.png', region=(1000,60,920,500),grayscale=True, confidence =0.98) != None:
            print('i can see 2')
        elif pyautogui.locateOnScreen('c1-5-3.png', region=(1000,60,920,500),grayscale=True, confidence =0.98) != None:
            print('i can see 3')
        elif pyautogui.locateOnScreen('c1-5-4.png', region=(1000,60,920,500),grayscale=True, confidence =0.98) != None:
            print('i can see 4')
        mapCount = mapCount + 1
        print(mapCount)
