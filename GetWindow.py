import time
import pygetwindow as gw    # 引入包pygetwindow使用别名gw（getWindows）

print("启动完毕，正在寻找游戏……")

x = 0
y = 0
def returData():
    while True:
        try:
            window = gw.getWindowsWithTitle('War Thunder')[0]   # 寻找游戏窗口
            x = window.left  # 窗口的左边界坐标
            y = window.top  # 窗口的顶部边界坐标
            print("成功找到游戏\n")
            print("窗口坐标 X："+str(x) + "，Y：" + str(y))    # 输出窗口坐标
            print("请勿随意拖动窗口")
            window.activate()
            time.sleep(3)
            return x,y
            break
        except IndexError:
            print("未找到游戏窗口")
            time.sleep(3)