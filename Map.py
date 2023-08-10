import requests
import hashlib
from io import BytesIO

def calculate_md5(file_data):
    md5_hash = hashlib.md5()
    md5_hash.update(file_data)
    return md5_hash.hexdigest()

# 这些内容是校验MD5值
def MD5():
    url = 'http://localhost:8111/map.img'
    response = requests.get(url)

    if response.status_code == 200:
        file_data = response.content
        md5_value = calculate_md5(file_data)
        return md5_value    # 返回md5值
    else:
        print("获取地图失败")

def foundMap():
    h1 = 1000
    h2 = 1500
    press = 1
    Vietnam = 'a546079510cd41d19f5a26bbbc4e738d'
    SinaiPeninsula = '24a39808b80abe5359d23ec454ffb536'
    GolanHeights = '166b151d03e6ecb507b0af3ba19583cf'
    Spain = '4c088fd502175f94fe1cf82a58135d82'
    PyreneesMountains = 'd8997861e6b8bb555064bb554719a18b'
    md5 = MD5()
    if md5 == Vietnam:
        print("地图 越南")
        h1 = 900
        h2 = 1500
        press = 1
        return h1, h2, press
    elif md5 == SinaiPeninsula:
        print("地图 西奈半岛")
        h1 = 700
        h2 = 1200
        press = 1
        return h1, h2, press
    elif md5 == GolanHeights:
        print("地图 戈兰高地")
        h1 = 1200
        h2 = 1600
        press = 1
        return h1, h2, press
    elif md5 == Spain:
        print("地图 西班牙")
        h1 = 1200
        h2 = 1600
        press = 2
        return h1, h2, press
    elif md5 == PyreneesMountains:
        print("地图 比利牛斯山脉")
        h1 = 3500
        h2 = 4000
        press = 1
        return h1, h2, press
    else:
        return h1, h2, press

