from pyautogui import *
import pyautogui
import pygetwindow
import time
import keyboard
import random
import win32api, win32con

win = pygetwindow.getWindowsWithTitle('BlueStacks')[0]
time.sleep(0.7)
win.moveTo(1022,40)
time.sleep(0.7)
win.size = (898,520)

pyautogui.displayMousePosition()
