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

if pyautogui.locateOnScreen('Ghost.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see Ghost")
            time.sleep(0.5)
            click(1809,482)
            time.sleep(0.5)
            click(1809,482)
            time.sleep(3)
            click(1282,462)
            time.sleep(3)
            click(1452,241)
            time.sleep(2)
            pyautogui.moveTo(1107, 470)
            time.sleep(1)
            pyautogui.dragTo(1, -100,0.2, button='left')
           # pyautogui.scroll(-500)
            time.sleep(1)
            click(1110,470)
            time.sleep(1)
            click(1271,267)
          #  click(1601,444)
            time.sleep(1)
