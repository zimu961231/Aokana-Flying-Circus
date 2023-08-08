# http://desktop-rqq242g:8111/

import requests

# 通过传入参数获得指定数据
def getData(url,str):
    response = requests.get(url)
    data = response.json()
    try:
        answer = data[str]
        return answer
    except KeyError:
        return None
# http://localhost:8111/state
# 重要参数："AoA, deg":攻角    "H, m":高度

# http://localhost:8111/indicators
# "throttle":节流阀  "type": "dummy_plane"=未起飞
# 炸弹点示例↓
# {"type":"bombing_point","color":"#fa0C00","color[]":[250,12,0],"blink":0,"icon":"bombing_point","icon_bg":"none","x":0.517530,"y":0.471646},

def getState():
    url = 'http://localhost:8111/state'
    str = "AoA, deg"    # "AoA, deg":攻角
    AoA = getData(url, str)
    str = "H, m"        # "H, m":高度
    Hm = getData(url, str)

    url = 'http://localhost:8111/indicators'
    str = "throttle"    # "throttle":节流阀
    throttle = getData(url, str)
    str = "type"        # "type": "dummy_plane"=未起飞
    type = getData(url, str)
    return AoA, Hm, throttle, type