import time

import Back
import Fighting
import pygetwindow as gw    # 引入包pygetwindow使用别名gw（getWindows）
import pyautogui




x=0
y=0
try:
    window = gw.getWindowsWithTitle('War Thunder')[0]  # 寻找游戏窗口
    x = window.left  # 窗口的左边界坐标
    y = window.top  # 窗口的顶部边界坐标
    print("成功找到游戏\n")
    print("窗口坐标 X：" + str(x) + "，Y：" + str(y))  # 输出窗口坐标
    print("请勿随意拖动窗口")
    window.activate()
    time.sleep(2)
except IndexError:
    print("未找到游戏窗口")
    time.sleep(2)
pyautogui.moveTo(x + 1200, y + 565)
# flag = Back.imgFound(x, y)
# print(flag)