import time                 # 调用时间函数
import GetWindow            # 调用窗口索引
import HangarMenu as hm     # 调用机库识图
import pyautogui            # 调用鼠标移动
import keyboard             # 调用键盘按键
import Waitting             # 调用等待界面
import port8111             # 调用8111端口
import Fighting             # 调用战斗中图像识别

# 鼠标单击事件
def Click():
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.mouseUp()

# CCRP开启
def ccrpStart():
    keyboard.press('o')
    time.sleep(0.1)
    keyboard.release('o')

# Esc单击事件
def Esc():
    keyboard.press('esc')
    time.sleep(0.1)
    keyboard.release('esc')

# 单击【加入战斗】
def starGame(x,y):
    pyautogui.moveTo(x + 650, y + 70)
    time.sleep(1)
    Click()

# 油门轴事件
def pushW():
    keyboard.press('w')
    time.sleep(3)
    keyboard.release('w')

# 鼠标移动事件：向上
def moveUp(m):
    keyboard.press(';')
    time.sleep(m)
    keyboard.release(';')

# 鼠标移动事件：向下
def moveDwon(m):
    keyboard.press('.')
    time.sleep(m)
    keyboard.release('.')

# 鼠标移动事件：向左
def moveL(m):
    keyboard.press(',')
    time.sleep(m)
    keyboard.release(',')
    print("左转")

# 鼠标移动事件：向右
def moveR(m):
    keyboard.press('/')
    time.sleep(m)
    keyboard.release('/')
    print("右转")

x, y=GetWindow.returData()   # 调用模块获得窗口坐标

bollen = 0
# 机库界面循环
while True:
    # 将窗口坐标传入机库识图模块,获得机库识图模块返回值，值为1则成功，值为0则失败
    Bollen = hm.cooData(x, y)
    if Bollen == 0:
        starGame(x, y)
        time.sleep(1)
        Esc()
        time.sleep(1)
    else:
        print("图像识别成功")
        break

# 点击开始游戏
starGame(x, y)
time.sleep(1)

bollen = Waitting.waitSearch(x, y)
pyautogui.moveTo(x + 950, y + 710)
Click()
time.sleep(5)

# 取消按钮搜索
while True:
    bollen = Waitting.startCancel(x, y)
    if bollen == 1:
        print("正在等待开始")
        time.sleep(1)
    else:
        break

# 检测飞机是否存在，如果存在则Type=="飞机型号"
# while True:
#     Type = port8111.startReady()
#     if Type == "dummy_plane":
#         print("正在等待开始")
#         time.sleep(1)
#     elif Type is None:
#         break
#     else:
#         break

# death = 0

#   战斗界面循环
flag = 0    # 设立判断
x, y = Fighting.getWin()    # 重新获得游戏窗口坐标
while True:
    # 判断是否存活
    bollen = Fighting.back(x, y)
    if bollen == 1:  # 返回机库
        print("载具被摧毁")
        keyboard.release('space')
        pyautogui.moveTo(x + 1000, y + 710)
        Click()
        break

    throttle = 0
    # 起飞事件
    num = 0
    while throttle < 110:    # 判断节流阀位置
        if num == 5:
            break
        elif flag == 1:
            break
        print(f"节流阀：{throttle} 正在加力;")
        pushW()
        Vy, Hm, throttle, IAS = port8111.getState()
        num += 1

    while True:
        Vy, Hm, throttle, IAS = port8111.getState()
        print(f"空速：{IAS} 高度：{Hm} 爬升率：{Vy} 节流阀：{throttle}")

        if throttle == 0 and IAS < 100:    # 判断是否死亡
            # death = 1
            print(f"节流阀：{throttle} 空速：{IAS} 可能死亡")
            time.sleep(3)
            break
        elif IAS < 250 and flag == 0:     # 判断是否具有起飞速度
            print(f"空速：{IAS} 无法起飞")
            break
        elif Hm < 700:      # 判断水平高度
            if Vy < 7:      # 判断爬升率
                moveUp(m=0.05)
                print("开始爬升")
            elif Vy > 10:
                moveDwon(m=0.01)
                print("起飞微调")
        elif Hm > 700 and flag == 0:
            flag = 1   # 标记为1 表示已经起飞过一次了
        elif 700 < Hm < 1000:   # 稳定飞行区间
            if Vy < -5:
                moveUp(m=0.01)
                print("开始爬升")
            elif Vy > 5:
                moveDwon(m=0.01)
                print("微调下降")
            print("保持高度")

            # CCRP寻路区
            flag = 2    # 准备开启CCRP
            if flag == 2:
                aimX = Fighting.ccrp2(x, y)
            if aimX is not None:    # 已获得屏幕中间坐标
                flag = 3
                ccrpStart()
            ccrpX = Fighting.ccrp1(x, y)
            if ccrpX is not None and aimX is not None:    # 已获得ccrp坐标
                flag = 4
                keyboard.press('space')     # 空格猴子
                if (ccrpX - aimX) > 200:    # 点在右边远处
                    moveR(m=0.05)
                elif (aimX - ccrpX) > 200:  # 点在左边远处
                    moveL(m=0.05)
                elif 0 < (ccrpX - aimX) < 200:  # 点在右边近处
                    moveR(m=0.01)
                elif 0 < (aimX - ccrpX) < 200:  # 点在左边近处
                    moveL(m=0.01)
            else:
                flag = 3
        elif Hm > 1000 and Vy > 0:  # 开始下降
            moveDwon(m=0.05)
            print("开始下降")
