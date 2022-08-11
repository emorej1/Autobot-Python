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

win = pygetwindow.getWindowsWithTitle('BlueStacks 1')[0]
win.moveTo(1020,45)
time.sleep(0.7)
win.moveTo(1022,40)
time.sleep(0.7)
win.size = (898,520)
win.activate()

sleep(0.5)

print("Starting in 3")
time.sleep(0.7)
print("            2")
time.sleep(0.7)
print("            1")
time.sleep(0.7)

run = 0
count = 0

#Game region=(1028,60,880,500), win.size = (898,520), win.moveTo(1022,40)


def convert(a):
    num = ""
    for c in a:
        if c.isdigit():
            num = num + c           
    return(num)



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

#while keyboard.is_pressed("caps_lock") == False:

while run < 80:

    run = run + 1

    if pyautogui.locateOnScreen('Battle.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see Battle")
        time.sleep(1.2)
        click(1749,447)
        time.sleep(3)

        if pyautogui.locateOnScreen('AConfirm.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
         print("I can see AConfirm")
         time.sleep(0.5)
         import Select
         Select.capture() 
         time.sleep(0.8)
         click(1550,508)
         time.sleep(2)
         count = 0
         run = 0

    ##             if pyautogui.locateOnScreen('BP.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
    ##                    print("I can see BP")
    ##                    pyautogui.moveTo(1445, 362)
    ##                    time.sleep(0.5)
    ##                    pyautogui.scroll(-200)
    ##                    time.sleep(1.5)
    ##                    # Medium BP
    ##                   # click(1445, 362)
    ##                    # Large BP
    ##                    click(1445, 440)
    ##                    time.sleep(1)
    ##                    click(1551, 505)
    ##                    time.sleep(1.5)
    ##                    click(1465, 451)
    ##                    time.sleep(1)
    ##                    click(1550,508)
    ##                    time.sleep(3)
    ##
    ##            else:
    ##               while count < 6:
    ##                time.sleep(0.5)
    ##                click(1217,405)
    ##                time.sleep(0.8)
    ##                click(1550,508)
    ##                time.sleep(2)
    ##                count = count + 1
    ##
    ##                if pyautogui.locateOnScreen('BP.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
    ##                    print("I can see BP")
    ##                    pyautogui.moveTo(1445, 362)
    ##                    time.sleep(0.5)
    ##                    pyautogui.scroll(-200)
    ##                    time.sleep(1.5)
    ##                    # Medium BP
    ##                   # click(1445, 362)
    ##                    # Large BP
    ##                    click(1445, 440)
    ##                    time.sleep(1)
    ##                    click(1551, 505)
    ##                    time.sleep(1.5)
    ##                    click(1465, 451)
    ##                    time.sleep(1)
    ##                    click(1550,508)
    ##                    time.sleep(3)
    ##
    ##                
    ##                print("Count: " ,count)
    ##                while pyautogui.locateOnScreen('Quit.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) == None:
    ##                    print("Waiting for Game")
    ##                    time.sleep(2)
    ##                else:
    ##                    time.sleep(5)
    ##                    print("I can see Quit")
    ##                    #quit menu button
    ##                    click(1859,89)
    ##                    time.sleep(0.8)
    ##                    #quit button
    ##                    click(1442,347)
    ##                    time.sleep(0.8)
    ##                    #confirm quit
    ##                    click(1571,447)
    ##                    time.sleep(8)
    ##                    #confirm match end results
    ##                    click(1681,371)
    ##                    time.sleep(15)
    ##                    click(1749,447)
    ##                    time.sleep(3)
    ##                    if count == 1:
    ##                        click(1285,161)
    ##                    elif count == 6:
    ##                        click(1378,500)
    ##                    
    ##                    
    ##                    
    ##                    
                
                
            
    ##            
    ##
    ##        elif pyautogui.locateOnScreen('BP.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
    ##            print("I can see BP")
    ##            pyautogui.moveTo(1445, 362)
    ##            time.sleep(0.5)
    ##            pyautogui.scroll(-200)
    ##            time.sleep(1.5)
    ##            # Medium BP
    ##            click(1445, 362)
    ##            # Large BP
    ##           # click(1445, 440)
    ##            time.sleep(1)
    ##            click(1551, 505)
    ##            time.sleep(1.5)
    ##            click(1465, 451)
    ##            time.sleep(1)
    ##            click(1550,508)
    ##            time.sleep(3)

    elif pyautogui.locateOnScreen('Done1.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see Done1")
        click(1693, 443)
        time.sleep(1)

    elif pyautogui.locateOnScreen('BP.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see BP. Time to wait")
        run = 80
        
        
    ##            click(1550,508)
    ##            time.sleep(2)
    ##            click(1350,503)
    ##            time.sleep(1801)
    ##            print("I'm halfway now")
    ##            time.sleep(1801)
    ##            print("Let's do this")
        

    elif pyautogui.locateOnScreen('Ghost.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        print("I can see Ghost")
        time.sleep(0.5)
        #double hit for square
        click(1809,482)
        time.sleep(0.5)
        click(1809,482)
        time.sleep(3)
        #Quest
        click(1282,462)
        time.sleep(2)
        #Arena
        click(1455,389)
        time.sleep(1)
                
                
                

            
                    
    else:
        freeze()
        print(("Run no: "), run)
      #  run = 0         
                
            
            
            
            
            
