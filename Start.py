from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
# number 1 location and colour: X: 1633 Y:  197 RGB: (155, 148, 121)

while 1:
    if pyautogui.locateOnScreen('Start.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see start")
       # time.sleep(0.5)
    else:
        print("I am unable to see start")
     #   time.sleep(0.5)

    if pyautogui.locateOnScreen('Lair.png', region=(1000,60,920,500)) != None:
        print("I can see Lair")
        time.sleep(2)
    else:
        print("I am unable to see Lair")
      #  time.sleep(0.5)

    if pyautogui.locateOnScreen('dark Lair.png', region=(1000,60,920,500)) != None:
        print("I can see dark Lair")
      #  time.sleep(0.5)
    else:
        print("I am unable to see dark Lair")
      #  time.sleep(0.5)  
        
    if pyautogui.locateOnScreen('Wave.png', region=(1020,150,100,100), confidence =0.80) != None:
        print("I can see Wave")
        time.sleep(2)
    else:
        print("I am unable to see Wave")
     #   time.sleep(0.5)
        
    if pyautogui.locateOnScreen('Check.png', region=(1500,160,170,70),grayscale=True, confidence =0.95) != None:
        print("I can see Check")
     #   time.sleep(0.5)
    else:
        print("I am unable to see Check")
     #   time.sleep(0.5)

    if pyautogui.locateOnScreen('Exit.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see Exit")
     #   time.sleep(0.5)
    else:
        print("I am unable to see Exit")
     #   time.sleep(0.5)
        
    if pyautogui.locateOnScreen('Confirm.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see Confirm")
     #   time.sleep(0.5)
    else:
        print("I am unable to see Confirm")
     #   time.sleep(0.5)
     
    if pyautogui.locateOnScreen('One.png', region=(1500,160,170,70),grayscale=True, confidence =0.95) != None:
        print("I can see One")
     #   time.sleep(0.5)
    else:
        print("I am unable to see One")
     #   time.sleep(0.5)
     
    if pyautogui.locateOnScreen('checktest.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see checktest")
     #   time.sleep(0.5)
    else:
        print("I am unable to see checktest")
     #   time.sleep(0.5)
    if pyautogui.pixelMatchesColor(1633 ,197,(155, 148, 121)) == True:
        print("i can see the pixel")
        time.sleep(0.5)

    else:
        print("I'm unable to see the pixel")

    if pyautogui.locateOnScreen('Zero.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see Zero")
       # time.sleep(0.5)
    else:
        print("I am unable to see Zero")
     #   time.sleep(0.5)

        
