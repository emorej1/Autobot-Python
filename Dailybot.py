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
win.moveTo(1022,40)
win.size = (898,520)

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

def loop():
  i = 1
  a = 1
 # time.sleep(1)
  while a < 10:
      
    freeze()
    if pyautogui.locateOnScreen('Dark Lair Easy.png', region=(1000,60,920,500), confidence =0.99) != None:         
           print("I can see Easy Lair")
           time.sleep(1)
           click(1607, 194)
           while i < 2:
               
             freeze()  
             if pyautogui.locateOnScreen('Start.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
                   print("I can see start")
                   time.sleep(0.5)
                   i = i + 1
                   print (i)
                   click(1518,505)
                   while i < 3:
                       
                           freeze()
                           if pyautogui.locateOnScreen('Done.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
                               print("I can see Done")
                               time.sleep(0.5)
                               i = i + 1
                               a = 1
                               print (i)
                               click(1768,528)
                               time.sleep(15)
                   

    elif pyautogui.locateOnScreen('Dark Lair Normal.png', region=(1000,60,920,500), confidence =0.99) != None:
           print("I can see Normal Lair")
           time.sleep(1)
           click(1596,272)
           while i < 2:
               
             freeze()  
             if pyautogui.locateOnScreen('Start.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
                   print("I can see start")
                   time.sleep(0.5)
                   i = i + 1
                   print (i)          
                   click(1518,505)
                   while i < 3:
                       
                           freeze()
                           if pyautogui.locateOnScreen('Done.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
                               print("I can see Done")
                               time.sleep(0.5)
                               i = i + 1
                               a = 1
                               print (i)
                               click(1768,528)
                               time.sleep(15)


    elif pyautogui.locateOnScreen('Dark Lair Hard.png', region=(1000,60,920,500), confidence =0.99) != None:
            print("I can see Hard Lair")
            time.sleep(1)
            click(1622,353)
            while i < 2:
                
             freeze()  
             if pyautogui.locateOnScreen('Start.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
                   print("I can see start")
                   time.sleep(0.5)
                   i = i + 1
                   print (i)          
                   click(1518,505)
                   while i < 3:

                           freeze()
                           if pyautogui.locateOnScreen('Done.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
                               print("I can see Done")
                               time.sleep(0.5)
                               i = i + 1
                               a = 1
                               print (i)
                               click(1768,528)
                               time.sleep(15)

    elif a == 5:
      click(1873,311)
      print ("clicked next")
      
      
    i = 1
    a = a + 1
    print (a)
  return

#win = pygetwindow.getWindowsWithTitle('BlueStacks')[0]
##win.size = (898,520)
##win.moveTo(1022,40)
##sleep(0.5)




#click(1270,202)    
loop()
#click(1368,208)
loop()
#click(1471,210) 
loop()
#click(1588,233)
loop()
#click(1697,234)
loop()
#click(1785,252)
loop()
#click(1263,450)
loop()
#click(1371,457)
loop()
#click(1480,449)
loop()
#click(1601,444)
loop()
#click(1697,444)
loop()
loop()
loop()
#click(1785,444)
loop()

