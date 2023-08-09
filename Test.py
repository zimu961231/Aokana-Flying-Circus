import Waitting
import time
import GetWindow
import Fighting
import pyautogui


x,y=GetWindow.returData()
while True:
    bollen = Fighting.back(x,y)
    if bollen == 1:
        print("1")
        time.sleep(1)
        pyautogui.moveTo(x + 1000, y + 710)
    else:
        break