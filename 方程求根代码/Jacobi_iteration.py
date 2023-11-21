import numpy as np

# Creating the coefficient matrix
n = 10
v1 = np.ones(n - 1) * 1
v2 = np.ones(n) * 6
v3 = np.ones(n - 1) * 8
A = np.diag(v1, 1) + np.diag(v2) + np.diag(v3, -1)

B = np.ones(n) * 15
B[0] = 7
B[-1] = 14
B = B.reshape(n,1)

#-----------------------使用Jacobi迭代求解方法-------------------------
def spectral_radius(M):
    a,b=np.linalg.eig(M) #a为特征值集合，b为特征值向量
    return np.max(np.abs(a)) #返回谱半径
ans1 = np.zeros(shape=(n,1))
ans2 = np.zeros(shape=(n,1))
a = np.diagonal(A) #取出对角线的元素
a = a.reshape((n, 1)) #将一维数组转换成二维数组
A = -1*A
i, j = np.diag_indices_from(A) #取出对角线元素的坐标索引值
A[i,j] = 0
A = A/a
B = B/a
if spectral_radius(A) > 1:
    #谱半径大于1，计算不收敛
    print('computationally non-convergent')
else:
    err = 3
    k = 0
    #设置精度
    while err >= 1.e-1 :
        ans2 = np.dot(A,ans1) + B
        err = np.max(np.abs(ans1 - ans2))
        ans1 = ans2.copy()
        k = k + 1
        print(k) #打印已迭代次数
    x = ans2.reshape((10,-1))
    print(x)