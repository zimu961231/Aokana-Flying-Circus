import time

from python_imagesearch.imagesearch import imagesearcharea  # 引入识图函数

# 识图函数
def imgSearch(imgData,sx,sy,ex,ey):
    pos = imagesearcharea(imgData, sx, sy, ex , ey , precision=0.7)
    if pos[0] != -1:
        bollen = 1
        return bollen
    else:
        bollen = 0
        return bollen

# 【取消】按钮识别
def waitCancel(x,y):
    sx = x+400
    sy = y
    ex = x+800
    ey = y+300
    imgData = "image/Loading/Cancel.png"
    bollen = imgSearch(imgData,sx,sy,ex,ey)
    if bollen == 1:
        print("正在匹配")
        return bollen
    else:
        bollen = 0
        return bollen

# 正在加入游戏界面识别
def waitJoin(x,y):
    sx = x+400
    sy = y+300
    ex = x+800
    ey = y+700
    imgData = "image/Loading/WaittingJoin.png"
    bollen = imgSearch(imgData,sx,sy,ex,ey)
    if bollen == 1:
        print("正在加入游戏")
        print("空战-历史性能\n")
        return bollen
    else:
        bollen = 0
        return bollen

# 正在载入游戏界面识别
def waitLoad(x,y):
    num = 1

    while num < 4:
        bollen = 0
        match num:
            case 1:
                sx = x
                sy = y + 64
                ex = x + 192
                ey = y + 256
                imgData = "image/Loading/HelpF1.png"
            case 2:
                sx = x + 300
                sy = y
                ex = x + 900
                ey = y + 500
                imgData = "image/Loading/WarThunder.png"
            case 3:
                sx = x + 600
                sy = y + 500
                ex = x + 1500
                ey = y + 1600
                imgData = "image/Loading/Loading.png"
        bollen = imgSearch(imgData, sx, sy, ex, ey)
        # 如果识别到图片则进入识别下一个特征，识别不到则退出函数
        if bollen == 1:
            num += 1
        else:
            bollen = 0
            return bollen

# 开始战斗界面识别
def startGame(x,y):
    sx = x + 600
    sy = y + 500
    ex = x + 1500
    ey = y + 1600
    imgData = "image/Loading/StatGame.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey)
    if bollen == 1:
        print("开始战斗\n")
        bollen = -1
        return bollen
    else:
        bollen = 0
        return bollen

# 循环判断是否加入战斗
def waitSearch(x,y):
    num = 0
    bollen = 0
    while num < 1000:
        time.sleep(0.5)
        # 匹配界面识别
        bollen = waitCancel(x, y)
        if bollen == 1:
            num == 0
            time.sleep(2)
        # 加入游戏界面识别
        bollen = waitJoin(x, y)
        if bollen == 1:
            num == 0
            time.sleep(1)
        # 载入游戏界面识别
        bollen = waitLoad(x, y)
        if bollen == 1:
            print("正在载入……\n")
            num == 0
            time.sleep(1)
        # 关键点：开始战斗界面识别
        bollen = startGame(x, y)
        if bollen == -1:
            return bollen
        num += 1
    print(num)