from pyautogui import *
import pyautogui
import pygetwindow
import pytesseract as tess

import ImageTestResults

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import time
import keyboard
import random
import win32api, win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def clickauto():
    click(1834, 144)


def checkRoom():
    click(1290, 428)
    time.sleep(1)
    loading = 1
    ghost = 0
    while pyautogui.locateOnScreen('Ghost.png', region=(1000, 60, 920, 500), grayscale=True,
                                   confidence=0.97) == None and loading < 10:
        print("We're not in Mama's room. Moving to room")
        if pyautogui.locateOnScreen('Cross.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1809, 482)
            time.sleep(1)
        click(1809, 482)
        time.sleep(3)
        click(1282, 462)
        time.sleep(3)
        click(1803, 467)
        time.sleep(20)
        ghost = ghost + 1
        if ghost == 2:
            print(ghost, ("run"))
            ghost = 0
            reset()
            startUp()


    else:
        print("We're in Mama's room")
        loading = 1
        time.sleep(1)
        gotoMap()


def gotoMap():
    click(1809, 482)
    time.sleep(1)
    click(1809, 482)
    time.sleep(3)
    click(1457, 463)
    time.sleep(3)


def checkMap(x):
    time.sleep(1)
    pyautogui.moveTo(1119, 307)
    time.sleep(0.5)
    pyautogui.scroll(460)
    time.sleep(3)
    if x == 1:
        click(1094, 140)
        time.sleep(1)
        click(1116, 299)
        time.sleep(1)
    elif x == 2:
        click(1094, 140)
        time.sleep(1)
        click(1118, 344)
        time.sleep(1)
    elif x == 3:
        click(1094, 140)
        time.sleep(1)
        click(1116, 388)
        time.sleep(1)
    elif x == 4:
        click(1094, 140)
        time.sleep(1)
        click(1116, 435)
        time.sleep(1)
    elif x == 5:
        click(1094, 140)
        time.sleep(1)
        click(1116, 480)
        time.sleep(1)
    elif x == 6:
        click(1094, 140)
        time.sleep(1)
        pyautogui.moveTo(1119, 307)
        time.sleep(0.5)
        pyautogui.scroll(-100)
        time.sleep(2)
        click(1108, 422)
        time.sleep(1)
    elif x == 7:
        click(1094, 140)
        time.sleep(1)
        pyautogui.moveTo(1119, 307)
        time.sleep(0.5)
        pyautogui.scroll(-460)
        time.sleep(3)
        click(1109, 233)
        time.sleep(1)
    elif x == 8:
        click(1094, 140)
        time.sleep(1)
        pyautogui.moveTo(1119, 307)
        time.sleep(0.5)
        pyautogui.scroll(-460)
        time.sleep(3)
        click(1109, 276)
        time.sleep(1)
    elif x == 9:
        click(1094, 140)
        time.sleep(1)
        pyautogui.moveTo(1119, 307)
        time.sleep(0.5)
        pyautogui.scroll(-460)
        time.sleep(3)
        click(1109, 325)
        time.sleep(1)
    elif x == 10:
        click(1094, 140)
        time.sleep(1)
        pyautogui.moveTo(1119, 307)
        time.sleep(0.5)
        pyautogui.scroll(-460)
        time.sleep(3)
        click(1109, 375)
        time.sleep(1)
    elif x == 11:
        click(1094, 140)
        time.sleep(1)
        pyautogui.moveTo(1119, 307)
        time.sleep(0.5)
        pyautogui.scroll(-460)
        time.sleep(3)
        click(1109, 422)
        time.sleep(1)
    elif x == 12:
        click(1094, 140)
        time.sleep(1)
        pyautogui.moveTo(1119, 307)
        time.sleep(0.5)
        pyautogui.scroll(-460)
        time.sleep(3)
        click(1109, 477)
        time.sleep(1)
    elif x == 13:
        click(1201, 136)
        time.sleep(2)
        click(1110, 293)
        time.sleep(1)
    elif x == 14:
        click(1201, 136)
        time.sleep(1)
        click(1110, 332)
        time.sleep(1)
    elif x == 15:
        click(1201, 136)
        time.sleep(1)
        click(1110, 392)
        time.sleep(1)
    elif x == 16:
        click(1201, 136)
        time.sleep(1)
        click(1110, 477)
        time.sleep(1)


def checkLoot():
    resetcount = 0
    time.sleep(1)
    click(1695, 496)
    time.sleep(5)
    while pyautogui.locateOnScreen('Obtained.png', region=(1000, 60, 920, 500), grayscale=True,
                                   confidence=0.90) == None:
        time.sleep(2)
        resetcount = resetcount + 1
        if resetcount == 6:
            print('Found nothing, returning to map')
        break

    else:
        if pyautogui.locateOnScreen('Obtained.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.90) != None:
            time.sleep(1)

            while pyautogui.locateOnScreen('Obtained.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.90) != None:

                image = pyautogui.screenshot(region=(1200,200,500,200))
                image.save(r"C:\Users\JSP10\Desktop\Android bots\Autobot Python\ObtainedResults1.png")

                results = ImageTestResults.testresult()

                with open(r'C:/Users/JSP10/Desktop/Android bots/Autobot Python/Logs/received.txt', 'a') as fp:
                    for item in results:
                        # write each item on a new line
                        fp.write("%s\n" % item)
                    fp.write("%s\n" % '-----------------------------')
                    print('Done')




                click(1655, 345)
                time.sleep(2.5)
            else:
                print('Returning to map')

    gotoMap()


def startUp():
    while pyautogui.locateOnScreen('Nier.png', region=(1028, 60, 880, 500)) == None:
        print("Waiting for Nier")
        time.sleep(5)



    else:
        loading = 1
        time.sleep(0.5)
        print("clicked")
        click(1384, 161)
        time.sleep(21)
        click(1384, 161)
        while pyautogui.locateOnScreen('Resume.png', region=(1028, 60, 880, 500),
                                       grayscale=True) is None and loading < 30:
            print("Waiting for Continue")
            loading = loading + 1
            print(loading)
            time.sleep(1)

        else:
            time.sleep(0.5)
            print("clicked")
            click(1537, 448)
            time.sleep(0.5)
            loading = 1


def reset():
    time.sleep(1)
    click(1196, 62)
    time.sleep(1)
    click(1654, 114)
    time.sleep(1)


def close():
    if pyautogui.locateOnScreen('Cross.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
        print('I can see cross')
        click(1859, 99)
        time.sleep(3)
    elif pyautogui.locateOnScreen('Book.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
        print('I can see book')
        click(1807, 480)
        time.sleep(3)


def selectMap():
    time.sleep(1)
    click(1546, 445)
    time.sleep(29)
    click(1455, 315)
    time.sleep(0.5)


win = pygetwindow.getWindowsWithTitle('BlueStacks')[0]
win.moveTo(1022, 40)
win.size = (898, 520)
win.activate()

print("Starting in 3")
time.sleep(0.7)
print("            2")
time.sleep(0.7)
print("            1")
time.sleep(0.7)

close()
time.sleep(3)
chapter = 12
mapCount = 0

gotoMap()

if pyautogui.locateOnScreen('Girl.png', region=(1000, 60, 920, 500), grayscale=True,
                            confidence=0.97) or pyautogui.locateOnScreen('SunMoon.png', region=(1000, 60, 920, 500),
                                                                         grayscale=True, confidence=0.97) != None:
    checkMap(chapter)
    time.sleep(2)
    while chapter == 1:
        if pyautogui.locateOnScreen('c1-1-1.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1275, 339)
            selectMap()
            clickauto()
            time.sleep(6.5)
            clickauto()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(100, 0, 1.9, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-1-2.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1439, 335)
            selectMap()
            clickauto()
            time.sleep(19)
            clickauto()
            time.sleep(0.5)
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            print('dragging')
            pyautogui.drag(-100, 0, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-1-3.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1598, 389)
            selectMap()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(0, -100, 7.7, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-1-4.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1633, 408)
            selectMap()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(0, -100, 8, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 2:
        if pyautogui.locateOnScreen('c1-2-1.png', region=(1000,60,920,500),grayscale=True, confidence =0.97) != None:
            click(1263,337)
            selectMap()
            clickauto()
            time.sleep(9)
            clickauto()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(-100, 0,1.8, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-2-2.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1421, 312)
            selectMap()
            clickauto()
            time.sleep(6)
            clickauto()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(50, -100, 2, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)
        elif pyautogui.locateOnScreen('c1-2-3.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1614, 307)
            selectMap()
            clickauto()
            time.sleep(43)
            clickauto()
            pyautogui.moveTo(1455, 400)
            time.sleep(1)
            pyautogui.drag(-100, 25, 1.3, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)
        elif pyautogui.locateOnScreen('c1-2-4.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1713, 308)
            selectMap()
            clickauto()
            time.sleep(31)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(3.7)
            pyautogui.moveTo(1455, 400)
            time.sleep(1)
            pyautogui.drag(100, 0, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 3:
        if pyautogui.locateOnScreen('c1-3-1.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1250, 337)
            selectMap()
            clickauto()
            time.sleep(40)
            clickauto()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(15, 100, 2.7, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-3-2.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1517, 336)
            selectMap()
            clickauto()
            time.sleep(4.1)
            clickauto()
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-3-3.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1652, 361)
            selectMap()
            clickauto()
            time.sleep(19.5)
            clickauto()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(0, -100, 2.2, button='left')
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-3-4.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1757, 297)
            selectMap()
            pyautogui.drag(-52, -100, 4.5, button='left')
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 4:
        if pyautogui.locateOnScreen('c1-4-1.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1245, 338)
            selectMap()
            clickauto()
            time.sleep(33)
            clickauto()
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-4-2.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1422, 312)
            selectMap()
            clickauto()
            time.sleep(5.2)
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(-100, 0, 1.2, button='left')
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-4-3.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1574, 362)
            selectMap()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(10, -100, 6, button='left')
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-4-4.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1670, 363)
            selectMap()
            clickauto()
            time.sleep(15.5)
            clickauto()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(100, 0, 2.5, button='left')
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 5:

        if pyautogui.locateOnScreen('c1-5-1.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1264, 337)
            selectMap()
            clickauto()
            time.sleep(16)
            clickauto()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(100, 0, 2.1, button='left')
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-5-2.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1423, 290)
            selectMap()
            clickauto()
            time.sleep(31.3)
            clickauto()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(-100, 0, 4, button='left')
            time.sleep(1)
            checkLoot()
            checkMap(chapter)
        elif pyautogui.locateOnScreen('c1-5-3.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1537, 280)
            selectMap()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(100, -100, 1, button='left')
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-5-4.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1657, 337)
            selectMap()
            clickauto()
            time.sleep(7.5)
            clickauto()
            checkLoot()
            checkMap(chapter)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 6:
        if pyautogui.locateOnScreen('c1-6-1.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1258, 326)
            selectMap()
            clickauto()
            time.sleep(16.2)
            clickauto()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(100, 0, 1.5, button='left')
            time.sleep(1)
            checkLoot()
            checkMap(chapter)


        if pyautogui.locateOnScreen('c1-6-2.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1412, 301)
            selectMap()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(70, -100, 5, button='left')
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-6-3.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1760, 311)
            selectMap()
            clickauto()
            time.sleep(51)
            clickauto()
            time.sleep(5)
            clickauto()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(-100, 0, 1, button='left')
            time.sleep(9)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-6-4.png', region=(1000, 60, 920, 500), grayscale=True,
                                      confidence=0.97) != None:
            click(1816, 375)
            time.sleep(1)
            click(1546, 445)
            time.sleep(25)
            while pyautogui.locateOnScreen('s1-6-4.png', region=(1000, 60, 920, 500), confidence=0.97) == None:
                time.sleep(2.2)
                click(1455, 315)
                time.sleep(0.5)
                clickauto()
                time.sleep(29.5)
                clickauto()
                time.sleep(8)
                pyautogui.moveTo(1455, 315)
                time.sleep(1)
                pyautogui.drag(-100, 0, 2.5, button='left')
                time.sleep(1)
                checkLoot()
                checkMap(chapter)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 7:
        if pyautogui.locateOnScreen('c1-7-1.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1280, 305)
            selectMap()
            time.sleep(36)
            click(1455, 315)
            pyautogui.drag(27, -100, 5, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-7-2.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1279, 308)
            selectMap()
            clickauto()
            time.sleep(9)
            clickauto()
            time.sleep(1)
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(100, -50, 1)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-7-3.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.99) != None:
            click(1350, 359)
            selectMap()
            clickauto()
            time.sleep(18)
            clickauto()
            time.sleep(1)
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(-100, 0, 2)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif pyautogui.locateOnScreen('c1-7-4.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1717, 350)
            selectMap()
            time.sleep(1)
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(-19, -100, 6, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif mapCount == 7:
            time.sleep(1)
            pyautogui.moveTo(1455, 315)
            pyautogui.scroll(400)
            time.sleep(2)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 8:
        if pyautogui.locateOnScreen('c1-8-1.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1246, 326)
            selectMap()
            time.sleep(10.5)
            click(1455, 315)
            time.sleep(1)
            clickauto()
            time.sleep(11)
            click(1455, 315)
            time.sleep(1)
            pyautogui.drag(-25, -100, 3, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)


        if pyautogui.locateOnScreen('c1-8-2.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1436, 358)
            selectMap()
            clickauto()
            time.sleep(8)
            clickauto()
            click(1455, 315)
            time.sleep(1)
            pyautogui.drag(35, -100, 3.5, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-8-3.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1572, 370)
            selectMap()
            clickauto()
            time.sleep(9.2)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-8-4.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1651, 386)
            selectMap()
            clickauto()
            time.sleep(15.5)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(-100, 0, 2.5, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 9:
        if pyautogui.locateOnScreen('c1-9-1.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1244, 305)
            selectMap()
            time.sleep(45)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(27)
            click(1636, 281)
            time.sleep(11)
            clickauto()
            time.sleep(10)
            clickauto()
            time.sleep(1)
            checkLoot()
            checkMap(chapter)


        if pyautogui.locateOnScreen('c1-9-2.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1446, 308)
            selectMap()
            clickauto()
            time.sleep(35)
            pyautogui.moveTo(1569, 206)
            time.sleep(1)
            pyautogui.drag(100, -30, 1.3, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)
        if pyautogui.locateOnScreen('c1-9-3.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1522, 358)
            selectMap()
            clickauto()
            time.sleep(7.5)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(100, 0, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-9-4.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1703, 383)
            selectMap()
            clickauto()
            time.sleep(3)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(-100, 0, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 10:

        if pyautogui.locateOnScreen('c1-10-1.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.97) != None:
            click(1246, 379)
            selectMap()
            time.sleep(17)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(19)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(-100, 0, 1.9, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-10-2.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1394, 274)
            selectMap()
            clickauto()
            time.sleep(18)
            click(1455, 315)
            time.sleep(1)
            click(1455, 315)
            time.sleep(1)
            click(1455, 315)
            time.sleep(1)
            click(1455, 315)
            time.sleep(1)
            click(1455, 315)
            time.sleep(1)
            click(1455, 315)
            time.sleep(1)
            click(1455, 315)
            time.sleep(1)
            click(1455, 315)
            time.sleep(5)
            clickauto()
            time.sleep(21)
            clickauto()
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-10-3.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1482, 347)
            selectMap()
            clickauto()
            time.sleep(38)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(100, 0, 1.9, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-10-4.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1765, 339)
            selectMap()
            clickauto()
            time.sleep(2)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(-100, 0, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 11:

        if pyautogui.locateOnScreen('c1-11-1.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1250, 368)
            selectMap()
            time.sleep(26)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(12.2)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(-100, 0, 1.2, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-11-2.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1402, 361)
            selectMap()
            clickauto()
            time.sleep(3)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(100, 60, 2, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-11-3.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1573, 366)
            selectMap()
            clickauto()
            time.sleep(28.2)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(100, 0, 3, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-11-4.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1777, 372)
            selectMap()
            clickauto()
            time.sleep(32)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(0, 100, 2, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 12:

        if pyautogui.locateOnScreen('c1-12-1.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1251, 279)
            selectMap()
            time.sleep(3)
            click(1455, 315)
            time.sleep(3)
            click(1455, 315)
            time.sleep(3.5)
            clickauto()
            time.sleep(31)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(-10, -100, 5.5, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-12-2.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1409, 260)
            selectMap()
            clickauto()
            time.sleep(21.5)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(-100, -15, 2, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-12-3.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1429, 327)
            selectMap()
            clickauto()
            time.sleep(3)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c1-12-4.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1575, 339)
            selectMap()
            clickauto()
            time.sleep(13.5)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            pyautogui.drag(-100, 0, 3, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 13:

        if pyautogui.locateOnScreen('c2-1-1.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.95) != None:
            click(1264, 278)
            selectMap()
            clickauto()
            time.sleep(10.5)
            clickauto()
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c2-1-2.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1335, 265)
            selectMap()
            clickauto()
            time.sleep(23)
            click(1455, 315)
            pyautogui.drag(100, -25, 1.5, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c2-1-3.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1523, 286)
            selectMap()
            clickauto()
            time.sleep(13)
            click(1749, 144)
            time.sleep(0.8)
            click(1551, 448)
            time.sleep(24)
            click(1455, 315)
            pyautogui.drag(100, -10, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c2-1-4.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1686, 410)
            selectMap()
            clickauto()
            time.sleep(2)
            click(1455, 315)
            time.sleep(0.5)
            time.sleep(21)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            time.sleep(1)
            pyautogui.drag(100, 0, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif mapCount == 10:
            time.sleep(1)
            pyautogui.moveTo(1455, 315)
            pyautogui.scroll(400)
            time.sleep(2)

        mapCount = mapCount + 1
        if mapCount == 15:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 14:

        if pyautogui.locateOnScreen('c2-2-1.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1542, 464)
            selectMap()
            time.sleep(2)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(54)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(9.5)
            clickauto()
            time.sleep(1)
            click(1455, 315)
            time.sleep(1)
            pyautogui.drag(-100, 0, 1.7, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)


        if pyautogui.locateOnScreen('c2-2-2.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1517, 445)
            selectMap()
            time.sleep(2)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(5.5)
            click(1455, 367)
            time.sleep(11)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(9)
            clickauto()
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c2-2-3.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1566, 201)
            selectMap()
            time.sleep(2)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(15)
            clickauto()
            time.sleep(4)
            click(1455, 215)
            pyautogui.drag(-100, 0, 2, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c2-2-4.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1533, 372)
            selectMap()
            time.sleep(2)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(10)
            click(1466, 336)
            time.sleep(10)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(7)
            clickauto()
            click(1455, 315)
            time.sleep(1)
            pyautogui.drag(-100, 50, 1, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif mapCount == 7:
            time.sleep(1)
            pyautogui.moveTo(1455, 315)
            pyautogui.scroll(-400)
            time.sleep(2)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)

    while chapter == 15:

        if pyautogui.locateOnScreen('c2-3-1.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1841, 483)
            selectMap()
            time.sleep(65)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(15)
            click(1455, 260)
            time.sleep(1)
            click(1749, 144)
            time.sleep(0.8)
            click(1551, 448)
            time.sleep(24)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(6.1)
            clickauto()
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c2-3-2.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1726, 427)
            selectMap()
            clickauto()
            time.sleep(35)
            click(1749, 144)
            time.sleep(0.8)
            click(1551, 448)
            time.sleep(28)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(7.2)
            clickauto()
            time.sleep(1)
            checkLoot()
            checkMap(chapter)


        if pyautogui.locateOnScreen('c2-3-3.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1612, 329)
            selectMap()
            click(1455, 315)
            time.sleep(0.5)
            pyautogui.drag(0, -100, 5, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(100, 0, 15.5, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(0, 100, 11, pyautogui.easeOutQuad)
            time.sleep(1)
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(-100, -10, 22.2, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c2-3-4.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1471, 228)
            selectMap()
            time.sleep(2)
            click(1455, 315)
            time.sleep(0.5)
            clickauto()
            time.sleep(6.5)
            clickauto()
            time.sleep(1)
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(-100, 0, 1.8, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)


    while chapter == 16:

        if pyautogui.locateOnScreen('c2-4-1.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1803, 272)
            selectMap()
            time.sleep(24)
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(-33, -100, 3.5, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c2-4-2.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1731, 240)
            selectMap()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(100, 0, 3, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c2-4-3.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1543, 260)
            selectMap()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(50, -100, 1.5, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        if pyautogui.locateOnScreen('c2-4-4.png', region=(1000, 60, 920, 500), grayscale=True,confidence=0.97) != None:
            click(1379, 388)
            selectMap()
            pyautogui.moveTo(1455, 315)
            time.sleep(1)
            pyautogui.drag(-5, 100, 18.8, pyautogui.easeOutQuad)
            time.sleep(1)
            checkLoot()
            checkMap(chapter)

        elif mapCount == 6:
            time.sleep(1)
            pyautogui.moveTo(1455, 315)
            pyautogui.scroll(400)
            time.sleep(2)

        mapCount = mapCount + 1
        if mapCount == 10:
            mapCount = 0
            chapter = chapter + 1
            checkMap(chapter)




