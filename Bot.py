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

print("Starting in 3")
time.sleep(0.7)
print("            2")
time.sleep(0.7)
print("            1")
time.sleep(0.7)

g = 0
run = 0


def freeze():
    counter = 1

    iml = pyautogui.screenshot(region=(1028,60,880,500))
    iml.save(r"C:\Users\JSP10\Desktop\Android bots\Autobot Python\Checking.png")

    print("I've taken a screenshot")
    time.sleep(0.7)    
    while pyautogui.locateOnScreen('Checking.png', region=(1028,60,880,500)) != None: 
        
        
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
         

#Game region=(1028,60,880,500)

while keyboard.is_pressed("caps_lock") == False:

    while run < 30:

   #     print("Run number",run)
        run = run + 1

        if pyautogui.locateOnScreen('Wave.png', region=(1020,148,100,15), confidence =0.90) != None:
            print("I can see Wave")
            click(1857,88)
            time.sleep(1.5)
            
        

            if pyautogui.locateOnScreen('Check.png', region=(1500,160,170,70),grayscale=True, confidence =0.95) != None:
                print("Shit you got something")
                time.sleep(2)
                click(1452, 506)
                while pyautogui.locateOnScreen('Done.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) == None:
                                       print("Waiting for Done")
                                       freeze() 
                                       time.sleep(2)
                else:
                                       iml = pyautogui.screenshot(region=(1028,60,880,500))
                                       iml.save(r"C:\Users\JSP10\Desktop\Android bots\Autobot Python\what.png")
                                       g = 0
                                       time.sleep(0.5)
                                       click(1768,528)
                                       time.sleep(20)
                                       click(1873,311)                          
                                                           
            elif pyautogui.locateOnScreen('Check.png', region=(1500,160,170,70),grayscale=True, confidence =0.95) != None:
                print("Shit you got something Revel 2")
                time.sleep(2)
                iml = pyautogui.screenshot(region=(1028,60,880,500))
                iml.save(r"C:\Users\j.sherdrack\Documents\Autobots-main\Autobots-main\what.png")
                click(1452, 506)
                while pyautogui.locateOnScreen('Done.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) == None:
                                       print("Waiting for Done")
                                       time.sleep(2)
                else:
                                       iml = pyautogui.screenshot(region=(1028,60,880,500))
                                       iml.save(r"C:\Users\JSP10\Desktop\Android bots\Autobot Python\what.png")
                                       time.sleep(0.5)
                                       click(1768,528)
                                       time.sleep(20)
                                       click(1873,311)   

            elif pyautogui.pixelMatchesColor(1633 ,197,(155, 148, 121)) == True:
                print("Shit you got something and this thing freaking missed it! How many missed :(")
                time.sleep(2)
                iml = pyautogui.screenshot(region=(1028,60,880,500))
                iml.save(r"C:\Users\j.sherdrack\Documents\Autobots-main\Autobots-main\what.png")
                click(1452, 506)
                while pyautogui.locateOnScreen('Done.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) == None:
                                       print("Waiting for Done")
                                       time.sleep(2)
                else:            
                                       time.sleep(0.5)
                                       click(1768,528)
                                       time.sleep(20)
                                       click(1873,311)   

            elif pyautogui.locateOnScreen('Zero.png', region=(1000,60,920,500),grayscale=True, confidence =0.97) != None:
                g = g + 1
                print("I can see Zero. Count:",g)
                click(1504,454)
                time.sleep(1.2)
                click(1504,454)
                time.sleep(7)

            
          
            
        elif pyautogui.locateOnScreen('Lair.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see Lair")
            click(1574,188)
            time.sleep(1)
            

        elif pyautogui.locateOnScreen('Stamina.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see Stamina")
            pyautogui.moveTo(1440, 330)
            time.sleep(1)
            pyautogui.scroll(-300)
            time.sleep(1)
            pyautogui.scroll(+70)
            time.sleep(1)
            click(1440, 420)
            time.sleep(1)
            #click 100
            click(1506,233)
            time.sleep(1)
            #click minus
            click(1412,236)
            time.sleep(1)
            #click confirm
            click(1551,505)
            time.sleep(1.5)
            click(1451,446)
            time.sleep(1.5)
       

        elif pyautogui.locateOnScreen('Start.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see start")
            click(1518,505)
            time.sleep(3)

        elif pyautogui.locateOnScreen('Ghost.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see Ghost")
            time.sleep(0.5)
            click(1809,482)
            time.sleep(0.5)
            click(1809,482)
            time.sleep(3)
            click(1282,462)
            time.sleep(3)
            click(1452,241)
            time.sleep(2)
            pyautogui.moveTo(1110, 470)
            time.sleep(1)
            pyautogui.dragTo(1, -100,0.2, button='left')
           # pyautogui.scroll(-500)
            time.sleep(1)
            click(1110,470)
            time.sleep(1)
            click(1271,267)
          #  click(1601,444)
            time.sleep(1)

        elif pyautogui.locateOnScreen('Next.png', region=(1655,180,26,26),grayscale=True, confidence =0.95) != None:
            print("I can see Next")
            click(1873,311)
            time.sleep(0.5)

        elif pyautogui.locateOnScreen('error.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see error")
            click(1462,490)
            time.sleep(10)
            click(1462,490)

        elif pyautogui.locateOnScreen('Resume.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see Resume")
            click(1537,448)        

        elif pyautogui.locateOnScreen('Refresh.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
            print("I can see Refresh")
            loading = 1
            click(1455,506)
            time.sleep(30)
            click(1455,506)
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
        freeze()
        run = 0
        
        
        
            
        

    
