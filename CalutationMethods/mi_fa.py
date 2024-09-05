# 幂法求解特征值和特征向量
# 2024-1-3

import numpy as np
A = np.array([[7,3,-2],[3,4,-1],[-2,-1,3]])
v0 = np.array([[1],[1],[1]])
n = 8
for i in range(n):
    u1 = np.dot(A,v0)
    lam = np.max(u1)
    v1 = u1 / lam
    print(lam,v1)
    v0 = v1
