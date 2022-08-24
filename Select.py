from pyautogui import *
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import subprocess
import psutil

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



#region 1 (region=(1160,230,140,30))


#region 2 (region=(1160,320,140,30))


#region 3 (region=(1160,410,140,30))

    
#Get numbers from string
def convert(a):
    num = ""
    for c in a:
        if c.isdigit():
            num = num + c           
    return(num)

def bptopup():
    time.sleep(2)
    if pyautogui.locateOnScreen('BP.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
           print("I can see BP")
           pyautogui.moveTo(1445, 362)
           time.sleep(0.5)
           pyautogui.scroll(-200)
           time.sleep(1.5)
           # Medium BP
           click(1445, 362)
           # Large BP
          # click(1445, 440)
           time.sleep(1)
           click(1551, 505)
           time.sleep(1.5)
           click(1465, 451)
           time.sleep(1)
           click(1550,508)
           time.sleep(3)



#take screenshots of region
def capture():
    iml = pyautogui.screenshot(region=(1160,215,140,45))
    iml.save(r"C:\Users\JSP10\Desktop\Android bots\Autobot Python\region1.png")

    iml = pyautogui.screenshot(region=(1160,305,140,45))
    iml.save(r"C:\Users\JSP10\Desktop\Android bots\Autobot Python\region2.png")

    iml = pyautogui.screenshot(region=(1160,395,140,45))
    iml.save(r"C:\Users\JSP10\Desktop\Android bots\Autobot Python\region3.png")


#convert image to string
    img = Image.open("region1.png")
    reg1 = tess.image_to_string(img)

    img = Image.open("region2.png")
    reg2 = tess.image_to_string(img)

    img = Image.open("region3.png")
    reg3 = tess.image_to_string(img)





#print(reg3)
#print("-----------------------------")


    

    creg1 = convert(reg1)
    creg2 = convert(reg2)
    creg3 = convert(reg3)

    print(creg1+","+creg2+","+creg3)


#change from string to interger
    ireg1 = int(creg1)
    ireg2 = int(creg2)
    ireg3 = int(creg3)


#picks lowest value

    if ireg3 < 78000:
        print("Found Bot")
        click(1211, 414)
        time.sleep(0.8)
        click(1550, 508)
        bptopup()
    else:
        print("No Bot, Resetting")
        count = 0
        while count < 6:
            count = count + 1
            print("run:", count)
            click(1211, 414)
            time.sleep(0.8)
            click(1550, 508)
            bptopup()
            time.sleep(8)
            while pyautogui.locateOnScreen('Quit.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) == None:
                print("Waiting for Game")
                time.sleep(2)
            else:
                time.sleep(5)
                print("I can see Quit")
                #quit menu button
                click(1859,89)
                time.sleep(1)
                #quit button
                click(1442,347)
                time.sleep(1)
                #confirm quit
                click(1571,447)
                time.sleep(9)
                #confirm match end results
                click(1681,371)
                time.sleep(24)
                click(1749,447)
                time.sleep(3)
                if count == 1:
                    click(1285,161)
                    time.sleep(1)
                elif count == 6:
                    click(1378,500)
                    time.sleep(1)

    # if ireg1 < ireg2:
    #     print("Region 1 is less than 2")
    #     if ireg1 < ireg3:
    #         print("Clicked Region 1")
    #         click(1211,229)
    #         time.sleep(1)
    #         click(1550, 508)
    #         bptopup()
    #
    #     else:
    #         if ireg3 < ireg2:
    #             print("Clicked Region 3")
    #             click(1211,414)
    #             time.sleep(1)
    #             click(1550, 508)
    #             bptopup()
    #         else:
    #             ("Clicked Region 2")
    #             click(1211,313)
    #             time.sleep(1)
    #             click(1550, 508)
    #             bptopup()
    # else:
    #     print("Region 2 is less than 1")
    #     if ireg2 < ireg3:
    #         print("Clicked Region 2")
    #         click(1211,313)
    #         time.sleep(1)
    #         click(1550, 508)
    #         bptopup()
    #     else:
    #         print("Clicked Region 3")
    #         click(1211,414)
    #         time.sleep(1)
    #         click(1550, 508)
    #         bptopup()



    






    



