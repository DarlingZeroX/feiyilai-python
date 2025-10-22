import 飞易来键鼠
import time
from headers.VKCode import VKCode as KCode

mMSC = 飞易来键鼠.键鼠模拟()

while True:
    print("F键按下")
    mMSC.KeyPress2(KCode['F'], 1)
    time.sleep(0.1)