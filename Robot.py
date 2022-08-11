from pyautogui import *
import pyautogui
import pygetwindow
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

#Check if there is any running process that contains the given name processName.

def checkIfProcessRunning(processName):
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def startUp():

    while pyautogui.locateOnScreen('Nier.png', region=(1028,60,880,500)) == None:
     print("Waiting for Nier")
     time.sleep(5)



    else:
            loading = 1
            time.sleep(0.5)
            print("clicked")
            click(1384,161)
            time.sleep(21)
            click(1384,161)
            while pyautogui.locateOnScreen('Resume.png', region=(1028,60,880,500),grayscale=True) == None and loading < 30:
                    print("Waiting for Continue")
                    loading = loading + 1
                    print(loading)
                    time.sleep(1)

            else:
              time.sleep(0.5)
              print("clicked")
              click(1537,448)
              time.sleep(0.5)
              loading = 1


def reset():

    time.sleep(1)
    click(1196,62)
    time.sleep(1)
    click(1654,114)
    time.sleep(1)


def checkRoom():

    loading = 1
    ghost = 0
    while pyautogui.locateOnScreen('Ghost.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) == None and loading < 10:
            print("We're not in Mama's room. Moving to room")
            click(1809,482)
            click(1809,482)
            time.sleep(3)
            click(1282,462)
            time.sleep(3)
            click(1803,467)
            ghost = ghost + 1
            if ghost == 20:
                print (ghost, ("run"))
                ghost = 0
                reset()
                startUp()
                checkRoom()


    else:
        print("We're in Mama's room")
        loading = 1
        time.sleep(5)

loading = 1


if checkIfProcessRunning('HD-Player'):
    print('Bluestacks is open')

else:
    subprocess.Popen("C:\Program Files\BlueStacks_nxt\HD-Player.exe")
    time.sleep(10)


win = pygetwindow.getWindowsWithTitle('BlueStacks 1')[0]
win.moveTo(1022,40)
win.size = (898,520)
win.activate()

time.sleep(5)



if checkIfProcessRunning('HD-Player'):
    print('Bluestacks confirmed open. Starting Nier')

    reset()
    startUp()
    while pyautogui.locateOnScreen('skip.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
        click(1843,98)
        time.sleep(1.5)

    else:
     time.sleep(2)
     checkRoom()

else:
    print("Error?")




import Arena
time.sleep(2)
click(1843,98)
time.sleep(2)
click(1843,98)
time.sleep(2)
click(1843,98)
time.sleep(2)



if pyautogui.locateOnScreen('Ghost.png', region=(1000,60,920,500),grayscale=True, confidence =0.95) != None:
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

import Dailybot










