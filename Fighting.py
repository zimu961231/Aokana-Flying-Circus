from python_imagesearch.imagesearch import imagesearcharea  # 引入识图函数
import pygetwindow

def getWin():
    x = 0
    y = 0
    window = pygetwindow.getWindowsWithTitle('War Thunder')[0]  # 寻找游戏窗口
    x = window.left  # 窗口的左边界坐标
    y = window.top  # 窗口的顶部边界坐标
    return x, y
def imgSearch(imgData, sx, sy, ex, ey):
    pos = imagesearcharea(imgData, sx, sy, ex, ey)
    if pos[0] != -1:
        bollen = 1
        return bollen
    else:
        bollen = 0
        return bollen

def back(x,y):
    sx = x + 600
    sy = y + 500
    ex = x + 1200
    ey = y + 800
    imgData = "image/Fight/Back.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey)
    if bollen == 1:
        print("返回基地\n")
        return bollen
    else:
        bollen = 0
        return bollen

def ccrpSearch(imgData, sx, sy, ex, ey, pre):
    pos = imagesearcharea(imgData, sx, sy, ex, ey, precision=pre)
    if pos[0] != -1:
        return pos
    else:
        return None

def ccrp1(x, y):
    sx = x
    sy = y + 200
    ex = x + 1280
    ey = y + 600
    pre = 0.8
    imgData = "image/Fight/CCRP1.png"
    result = ccrpSearch(imgData, sx, sy, ex, ey, pre)
    if result is not None:
        ix, iy = result
        ix = ix + x
        print("CCRP坐标找到，位置：", ix, iy)
        return ix
    else:
        return None

def ccrp2(x, y):
    sx = x + 400
    sy = y + 200
    ex = x + 1000
    ey = y + 600
    pre = 0.5
    imgData = "image/Fight/CCRP2.png"
    result = ccrpSearch(imgData, sx, sy, ex, ey, pre)
    if result is not None:
        ix, iy = result
        ix = ix + 400 + x
        print("准星坐标找到，位置：", ix, iy)
        return ix
    else:
        return None