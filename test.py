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


#Game region=(1000,60,920,500)

#click(1270,202)
    
while 1:
    
   if pyautogui.locateOnScreen('Dark Lair Easy.png', region=(1000,60,920,500), confidence =0.99) != None:
           print("I can see Easy Lair")
           time.sleep(0.5)
   else:
            print("Easy nothing")
            time.sleep(0.5)
#pyautogui.click('Dark Lair Easy.png')
   if pyautogui.locateOnScreen('Dark Lair Normal.png', region=(1000,60,920,500), confidence =0.99) != None:
           print("I can see Normal Lair")
           time.sleep(0.5)
   else:
            print("Normal nothing")
            time.sleep(0.5)

   if pyautogui.locateOnScreen('Dark Lair Hard.png', region=(1000,60,920,500), confidence =0.99) != None:
           print("I can see Hard Lair")
           time.sleep(0.5)
   else:
            print("Hard nothing")
            time.sleep(0.5)
elif pyautogui.locateOnScreen('Start.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see start")
        
