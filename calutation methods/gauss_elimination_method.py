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

#solve
A = np.concatenate((A, B), axis=1)
rows,columns = A.shape
ans = np.zeros(shape=(rows,1))

for c1 in range(rows-1):
    for c2 in range(rows-c1-1):
        if A[c1+c2+1 , c1] != 0:
            a = A[c1+c2+1 , c1] / A[c1 , c1]
            A[c1+c2+1:c1+c2+2 , :] = A[c1+c2+1:c1+c2+2 , :] - A[c1:c1+1 , :] * a


for i in range(rows):
    ans[rows-i-1] = A[rows-i-1 , columns-1] / A[rows-i-1 , columns-2-i]
    A[: , columns-1:columns] = A[: , columns-1:columns] - ans[rows-i-1] * A[: , rows-i-1:rows-i]
print(ans)