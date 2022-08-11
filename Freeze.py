from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def Freeze():
    counter = 1
    

    iml = pyautogui.screenshot(region=(1028,60,880,500))
    iml.save(r"C:\Users\JSP10\Desktop\Android bots\Autobot Python\Checking.png")

    print("I've taken a screenshot")
    time.sleep(0.7)    
    while pyautogui.locateOnScreen('Checking.png', region=(1028,60,880,500),grayscale=True) != None: 
        
        
          print("Seems like it's frozen. Restarting at 100")
          counter = counter + 1
          loading = 1
          print(counter)
          if counter == 100:
              click(1199,57)
              time.sleep(1)
              click(1652,111)
              time.sleep(1)
              click(1384,156)
              time.sleep(21)
              click(1384,161)
              while pyautogui.locateOnScreen('Resume.png', region=(1028,60,880,500)) == None and loading < 30:
                print("Waiting for Continue")
                loading = loading + 1
                print(loading)
                time.sleep(1)
                
              else:
                    time.sleep(0.5)
                    print("clicked")
                    click(1537,448)
                            
          
          
    else:
          
         print("Not Frozen. Moving on")


Freeze()

