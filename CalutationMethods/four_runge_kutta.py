# 4阶龙格库塔法
# 2023-12-29

import numpy as np

def funx(x,y):
    # 定义f(x,y)
    ans = 3*y/(x + 1)
    return ans
a = 0
b = 1
y0 = 1
h = 0.2
#============================
xn = a
yn = y0
while xn <= b :
    k1 = funx(xn, yn)
    k2 = funx(xn + h/2, yn + h * k1 / 2)
    k3 = funx(xn + h/2, yn + h * k2 / 2)
    k4 = funx(xn + h, yn + h * k3)
    yn_add1 = yn + h * (k1 + 2*k2 + 2*k3 +k4) / 6
    xn = xn + h
    yn = yn_add1
    print(xn,yn)












