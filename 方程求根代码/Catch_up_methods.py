#方程求根实现
import numpy as np
np.set_printoptions(precision=9)
#--------------------创建系数矩阵和B矩阵----------------------
n = 30
A = np.zeros(shape=(n,n) , dtype=np.float64)
B = 15 * np.ones(shape=(n,1))
B[0,0] = 7.
B[n-1,0] = 14.
index = np.zeros(shape=(n, n) , dtype=np.int64)
i = np.arange(n).reshape((n,1))
i = i + index
j = np.arange(n)
j = j + index
off0_i = np.diagonal(i) #储存斜对角元素的i索引值
off0_j = np.diagonal(j) #储存斜对角元素的j索引值
off1_i = np.diagonal(i,offset=1) #储存上斜一行对角元素的i索引值
off1_j = np.diagonal(j,offset=1) #储存上斜一行对角元素的j索引值
offd1_i = np.diagonal(i,offset=-1) #储存下斜一行对角元素的i索引值
offd1_j = np.diagonal(j,offset=-1) #储存下斜一行对角元素的j索引值
A[off0_i , off0_j] = 6.
A[off1_i , off1_j] = 1.
A[offd1_i , offd1_j] = 8.
#---------------------------------------------------------------
#----------矩阵分解----------
L = np.zeros(shape=(n,n))
U = np.eye(n)
b = A[off0_i , off0_j].reshape((n,1))
c = A[off1_i , off1_j].reshape((n-1,1))
gama = A[offd1_i , offd1_j].reshape((n-1,1))
alpha = np.zeros(shape=(n , 1))
beta = np.zeros(shape=(n-1 , 1))
L[offd1_i , offd1_j] = A[offd1_i , offd1_j]
alpha[0 , 0] = b[0 , 0]
beta[0 , 0] = c[0 , 0] / alpha[0 , 0]
#注意gama的数组大小不同
for i in range(1 , n):
    alpha[i , 0] = b[i , 0] - gama[i-1 , 0] * c[i-1 , 0] / alpha[i-1 , 0]
    if i != n-1:
        beta[i , 0] = c[i , 0] / alpha[i , 0]
L[off0_i , off0_j] = alpha.reshape((n,))
U[off1_i , off1_j] = beta.reshape((n-1,))
#可以验证分解是否正确
print(np.dot(L,U))
#---------回代求解-----------
y = np.zeros(shape=(n,1))
x = np.zeros(shape=(n,1))
y[0,0] = B[0,0] / alpha[0,0]
for i in range(1,n):
    y[i,0] = (B[i,0] - gama[i-1,0] * y[i-1,0]) / alpha[i,0]
x[n-1 , 0] = y[n-1 , 0]
for i in range(n-2 , -1 , -1):
    x[i,0] = y[i,0] - beta[i,0] * x[i+1,0]
print(x.reshape((10,-1)))