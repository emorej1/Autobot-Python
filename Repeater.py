from pyautogui import *
import pyautogui
import pygetwindow
import time
import keyboard
import random
import win32api, win32con
import sys

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

run = 0
num = 0

win = pygetwindow.getWindowsWithTitle('BlueStacks')[0]
win.size = (898,520)
win.moveTo(1022,40)
sleep(0.5)

print("Starting in 3")
time.sleep(0.7)
print("            2")
time.sleep(0.7)
print("            1")
time.sleep(0.7)


#Game region=(1028,60,880,500), win.size = (898,520), win.moveTo(1022,40)

def freeze():
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


while keyboard.is_pressed("caps_lock") == False:

    while run < 100:

        run = run + 1

        if pyautogui.locateOnScreen('Next1.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see Next1")
            click(1524,530)
            time.sleep(1)
        
        elif pyautogui.locateOnScreen('Done1.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see Done1")
            num = num + 1
            print("This is run ---------------------->",num)
            if num == 20:
                sys.exit("Error message")
            click(1449,504)
            time.sleep(1)

        elif pyautogui.locateOnScreen('Try.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see Try")
            click(1756,531)
            time.sleep(4)

        elif pyautogui.locateOnScreen('Daily.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see Daily")
            click(1687,439)
            time.sleep(1)

        elif pyautogui.locateOnScreen('points.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see points")
            click(1756,531)
            time.sleep(1)

        elif pyautogui.locateOnScreen('Start.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see start")
            click(1518,505)
            time.sleep(1)
            
##        elif pyautogui.locateOnScreen('Stamina.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
##            print("I can see Stamina")
##            pyautogui.moveTo(1440, 330)
##            time.sleep(1)
##            pyautogui.scroll(-400)
##            time.sleep(1)
##            pyautogui.scroll(+100)
##            time.sleep(1)
##            click(1440, 330)
##            time.sleep(1)
##            #click 100
##            #click(1506,233)
##            #Double click plus
##            click(1605,226)
##            time.sleep(0.9)
##            click(1605,226)
##            time.sleep(1)
##            #click minus
##            click(1412,236)
##            time.sleep(1)
##            #click confirm
##            click(1551,505)
##            time.sleep(1.5)
##            click(1451,446)
##            time.sleep(1.5)
        

    else:
        freeze()
        run = 0

