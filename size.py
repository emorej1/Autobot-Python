from pyautogui import *
import pyautogui
import pygetwindow
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

win = pygetwindow.getWindowsWithTitle('BlueStacks')[0]
win.moveTo(1054,40)
win.size = (866,502)

