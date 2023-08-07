import time

from python_imagesearch.imagesearch import imagesearcharea  # 引入识图函数
def CooData(x,y):
    counter = 1   # 循环计数器
    while counter <= 5:
        Num = 0   # 获取图片个数
        pos = imagesearcharea("image/HangarMenu/Setting.png", x, y, x+192, y+128)
        if pos[0] != -1:
            Num += 1
        else:
            print("'Setting' image not found")

        pos = imagesearcharea("image/HangarMenu/Battle.png", x+400, y, x+800, y+300)
        if pos[0] != -1:
            Num += 1
        else:
            print("'Battle' image not found")

        pos = imagesearcharea("image/HangarMenu/Help.png", x + 1000, y, x + 1500, y + 128)
        if pos[0] != -1:
            Num += 1
        else:
            print("'Help' image not found")

        if Num == 3:
            return 1  # 返回值1，识别成功
            break
        else:
            print("图像识别失败，请查看游戏界面是否被遮挡")
            print("第"+ str(counter)+"次识别失败")
            counter += 1
            time.sleep(3)
    print("界面识别失败，请检查")
    return 0  # 返回值0，识别失败
