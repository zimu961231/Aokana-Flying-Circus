import time
import Fighting
import pygetwindow as gw    # 引入包pygetwindow使用别名gw（getWindows）
import pyautogui




x=0
y=0
window = gw.getWindowsWithTitle('War Thunder')[0]   # 寻找游戏窗口
x = window.left  # 窗口的左边界坐标
y = window.top  # 窗口的顶部边界坐标
while True:
    Fighting.ccrp1(x, y)
    Fighting.ccrp2(x, y)
    # 获取当前鼠标的坐标
    # mx, my = pyautogui.position()
    # 打印坐标
    # print(f"当前鼠标坐标：({x}, {y})")
    time.sleep(1)