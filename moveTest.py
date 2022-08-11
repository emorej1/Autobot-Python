from pyautogui import *
import pyautogui
import pygetwindow
import time
import keyboard
import random
import win32api, win32con
import subprocess
import psutil

#auto location: X: 1834 Y:  144

#centre: X: 1455 Y:  315



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def clickauto():
    click(1834,144)
    
win = pygetwindow.getWindowsWithTitle('BlueStacks')[0]
win.moveTo(1022,40)
win.size = (898,520)
win.activate()

#left: pyautogui.dragTo(-100, 0,1, button='left')
#right: pyautogui.dragTo(100, 0,1, button='left')
#up: pyautogui.dragTo(0, -100,1, button='left')
#down: pyautogui.dragTo(0, 100,1, button='left')
    
time.sleep(1)


click(1455,315)
time.sleep(0.5)
# clickauto()
# time.sleep(6.5)
# clickauto()
# time.sleep(1)
# pyautogui.moveTo(1455,315)
# time.sleep(1)
#












