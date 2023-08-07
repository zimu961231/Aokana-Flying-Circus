import time                 # 调用时间函数
import GetWindow            # 调用窗口索引
import HangarMenu as hm     # 调用机库识图
import pyautogui            # 调用鼠标移动
import keyboard             # 调用键盘按键


x,y=GetWindow.returData()   # 调用模块获得窗口坐标

def Click():
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.mouseUp()

def Esc():
    keyboard.press('esc')
    time.sleep(0.1)
    keyboard.release('esc')

def starGame(x,y):
    pyautogui.moveTo(x + 650, y + 70)
    time.sleep(1)
    Click()

# 机库界面循环
while True:
# 将窗口坐标传入机库识图模块,获得机库识图模块返回值，值为1则成功，值为0则失败
    Bollen = hm.cooData(x,y)
    if Bollen == 0:
        starGame(x,y)
        time.sleep(1)
        Esc()
        time.sleep(1)
    else:
        print("图像识别成功")
        break

starGame(x,y)
time.sleep(1)