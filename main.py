import GetWindow            # 调用窗口索引
import HangarMenu as hm     # 调用机库识图


x,y=GetWindow.returData()   # 调用模块获得窗口坐标

# 将窗口坐标传入机库识图模块
def pushDatatohm(x,y):
    hm.CooData(x,y)

# 获得机库识图模块返回值，值为1则成功，值为0则失败
Bollen = hm.CooData(x,y)
print(Bollen)