from python_imagesearch.imagesearch import imagesearcharea  # 引入识图函数

def imgSearch(imgData,sx,sy,ex,ey):
    pos = imagesearcharea(imgData, sx, sy, ex , ey)
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