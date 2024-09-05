#计算方法
#龙贝格求积分外推法
#2023-12-22
import numpy as np
np.set_printoptions(precision=7)
#------------------定义被积函数------------------------
def funx(x):
    f = 1/x
    return f
a = 1
b = 3
h = b - a
T = np.zeros(shape=(10,10) , dtype=np.float64)
n = 1
T[0, 0] = h / 2 * (funx(a) + funx(b))
err = 100
while err >= 1.e-5:
    #-----------先求第一列-------------
    sumf = 0
    for i in range(2**(n-1)):
        sumf = sumf + funx( (b-a) / 2**n + a + i * (b-a) / 2**(n-1) )
    T[n, 0] = 1 / 2 * T[n-1, 0] + h / 2 * sumf
    h = h / 2
    #----------再求该行的其他外推--------
    for j in range(1, n+1):
        T[n, j] = 4**j / (4**j - 1) * T[n, j-1] - 1/(4**j - 1) * T[n-1, j-1]
    err = abs(T[n,n] - T[n-1,n-1])
    n = n + 1
print(T)




