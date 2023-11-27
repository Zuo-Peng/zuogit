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


cond = np.linalg.cond(A, p=None)
print('A的条件数为：',cond)
