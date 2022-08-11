from pyautogui import *
import pyautogui
import pygetwindow
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import time
import keyboard
import random
import win32api, win32con
import ImageTestResults

win = pygetwindow.getWindowsWithTitle('BlueStacks')[0]
win.moveTo(1022, 40)
win.size = (898, 520)
win.activate()

while pyautogui.locateOnScreen('Obtained.png', region=(1000, 60, 920, 500), grayscale=True, confidence=0.90) != None:

    image = pyautogui.screenshot(region=(1200, 240, 500, 160))
    image.save(r"C:\Users\JSP10\Desktop\Android bots\Autobot Python\ObtainedResults1.png")

  #  img = tess.image_to_string(Image.open("ObtainedResults1.png"))

    results = ImageTestResults.testresult()

    with open(r'C:/Users/JSP10/Desktop/Android bots/Autobot Python/Logs/received.txt', 'a') as fp:
        for item in results:
            # write each item on a new line
            fp.write("%s\n" % item)
        print('Done')



    #print(img)
    time.sleep(2.5)
else:
    print('Returning to map')