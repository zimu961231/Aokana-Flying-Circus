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
def moveUp():
    keyboard.press(';')
    time.sleep(0.05)
    keyboard.release(';')

# 鼠标移动事件：向下
def moveDwon():
    keyboard.press('.')
    time.sleep(0.05)
    keyboard.release('.')
    print("开始下降")

# 鼠标移动事件：L
def moveL():
    keyboard.press(',')
    time.sleep(0.05)
    keyboard.release(',')
    print("左转")

def moveR():
    keyboard.press('/')
    time.sleep(0.05)
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
time.sleep(2)

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

death = 0

while True:
    # 判断
    bollen = Fighting.back(x, y)
    if death == 1 and bollen == 1:  # 返回机库
        print("载具被摧毁")
        pyautogui.moveTo(x + 1000, y + 710)
        Click()
        break
    # 判断节流阀位置
    Vy, Hm, throttle, IAS = port8111.getState()

    num = 0
    while throttle < 110:
        print(f"节流阀： {throttle} 正在加力;")
        pushW()
        time.sleep(3)
        num += 1
        if num == 10:
            break
    count = 0  # 计数器变量
    while count < 10:
        Vy, Hm, throttle, IAS = port8111.getState()
        print(f"空速：{IAS} 高度：{Hm} 爬升率：{Vy} 节流阀：{throttle}")
        # if IAS is None:
        #     time.sleep(1)
        #     break
        # elif Hm is None:
        #     time.sleep(1)
        #     break
        # elif Vy is None:
        #     time.sleep(1)
        #     break
        # elif power is None:
        #     time.sleep(1)
        #     break
        # IAS = int(IAS)
        # Hm = int(Hm)
        # Vy = float(Vy)
        # power = float(power)
        # print(f"空速： {IAS} 高度： {Hm} 爬升率： {Vy}")

        if throttle == 0 and IAS == 0:    # 判断是否死亡
            death = 1
            print(f"节流阀： {throttle} 空速： {IAS}")
            break
        elif IAS < 250:     # 判断是否具有起飞速度
            print(f"空速： {IAS}")
            print("无法起飞")
            break
        elif Hm < 500:      # 判断水平高度
            if Vy < 7:      # 判断爬升率
                moveUp()
                print("开始爬升")
            elif Vy > 10:
                moveDwon()
        elif 500 < Hm < 1000:   # 稳定飞行区间
            if Vy < -3:
                moveUp()
                print("开始爬升")
            elif Vy > 5:
                moveDwon()
            print("保持高度")
        elif Hm > 1000 and Vy > 0:  # 开始下降
            moveDwon()
        count += 1