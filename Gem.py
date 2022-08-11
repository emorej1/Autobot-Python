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

def freeze():
    counter = 1

    iml = pyautogui.screenshot(region=(1028,60,880,500))
    iml.save(r"C:\Users\JSP10\Desktop\Android bots\Autobot Python\Checking.png")

    print("I've taken a screenshot")
        
    while pyautogui.locateOnScreen('Checking.png', region=(1028,60,880,500)) != None: 
        
        
          print("I can see Checking")
          counter = counter + 1
          print(counter)
          if counter == 300:
              click(1296,57)
              time.sleep(1)
              click(1658,183)
              time.sleep(1)
              click(1384,161)
              time.sleep(18)
              click(1384,161)
              while pyautogui.locateOnScreen('Resume.png', region=(1028,60,880,500)) == None:
                print("Waiting for Continue")
              else:
                    sleep(0.5)
                    print("clicked")
                    click(1537,448)
                            
          
          
    else:
          
         print("Next")
         


    print("End")

while True:

    if pyautogui.locateOnScreen('GemLair.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see GemLair")
        click(1699,442)

    elif pyautogui.locateOnScreen('Start.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see start")
        click(1518,505)

    elif pyautogui.locateOnScreen('Done1.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see Done1")
        click(1462,504)

    elif pyautogui.locateOnScreen('Done.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see Done")
        click(1743,532)

    freeze()
