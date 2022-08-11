from pyautogui import *
import pyautogui
import pygetwindow
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import time
import ImageTestResults
y = 0
returned = []
value = []
z = 0

#results = ImageTestResults.testresult()

results = [['Medium Stamina Recovery', 2], ['Explorer s Ticket', 2],['Medium Stamina Recovery', 3], ['Explorer s Ticket', 2]]




# while y < 2:
#     y = y + 1
#     returned.extend(results)

#print(returned)

# for x in results:
#
#     if x[0] not in value:
#          print('passed')
#          value.append(x)
#          print(value)
#          # for a in x:
#          #        if a == x[a]:
#          #            print('wo')
#                    # a[1] = (a[1]+x[1])
#     else:
#         print('added')
#
#         print(value)


for x in results:

    for a in x:
        print("a is now: ",a)
        if isinstance(a, int):
            break
        else:
            print('passed')

    if a not in value:
        print('added')
        value.append(x)

    if x[0] in value:



            #print(value)


print(value)