from pyautogui import *
import pyautogui
import pygetwindow
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import time

rev = []
rel = []
loop = 0
returned = []

def testresult():
        rev = []
        returned = []
        rel = []
        # from pyautogui import *
        # import pyautogui
        # import pygetwindow
        # import pytesseract as tess
        # tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        # from PIL import Image
        # import time

        img = tess.image_to_string(Image.open("ObtainedResults1.png"))

       # print(img)

        res = img.splitlines()


       # print(res)




        for line in res:
                if (re.findall(r'\w+', line)) == ['Obtained'] or (re.findall(r'\w+', line)) == []:
                        continue
                else:
                        rev.append((re.findall(r'\w+', line)))
                     #   print(rev)


        for row in rev:
                if row[0] == '4':
                        row.remove('4')

                if 'x' in row[-1]:
                     #   print('i see')

                        row[-1] = int((row[-1].replace('x', '')))
                    #    print(row[-1])

                if isinstance(row[-1], int):
                      #  print('passed here')

                        rel += [[(' '.join(row[:-1]))] + [row[-1]]]
                      #  print(rel)

                else:
                        rel += [(' '.join(row))]



        return rel




        #print(rev)

#print(returned)

#testresult()



#a ={"Item":[], "Amount":[]}
#b = list(a.values())



# itm = a[0]
# amt = a[1]

# for line in b:
#         print(re.findall(r'\w+', line))

#print(b)

#itm =


#print(take)