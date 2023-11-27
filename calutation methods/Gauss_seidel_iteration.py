import numpy as np
def gauss_seidel_iteration_matrix(A):
    n = len(A)
    D = np.diag(np.diag(A))
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)
    D_inv = np.linalg.inv(D)
    M = np.dot(D_inv, L + U)
    return M

def spectral_radius(matrix):
    eigenvalues, _ = np.linalg.eig(matrix)
    return max(abs(eigenvalues))

def main(A):
    # 计算 Gauss-Seidel 迭代矩阵
    iteration_matrix = gauss_seidel_iteration_matrix(A)

    # 计算谱半径
    radius = spectral_radius(iteration_matrix)

    print("Gauss-Seidel 迭代矩阵:")
    print(iteration_matrix)
    print("谱半径:", radius)
#---------------------------------------------
# Creating the coefficient matrix
n = 30
v1 = np.ones(n - 1) * 1
v2 = np.ones(n) * 6
v3 = np.ones(n - 1) * 8
A = np.diag(v1, 1) + np.diag(v2) + np.diag(v3, -1)

B = np.ones(n) * 15
B[0] = 7
B[-1] = 14
B = B.reshape(n,1)
#----------------计算谱半径---------------------
if __name__ == '__main__':
    main(A)
#---------------------------------------------
ans1 = np.zeros(shape=(n,1))
ans2 = np.zeros(shape=(n,1))
a = np.diagonal(A).reshape((n, 1)) #取出对角线的元素
A = -1*A
i, j = np.diag_indices_from(A) #取出对角线元素的坐标索引值
A[i,j] = 0
A = A/a
B = B/a
err = 3
k = 0
while err >= 1.e-5:
    ans_tem = ans1.copy()
    for i in range(n):
        ans2[i,0] = np.dot(A[i:i+1] , ans1) + B[i,0]
        ans1[i,0] = ans2[i,0]
    err = np.max(np.abs(ans_tem - ans2))
    k = k + 1
    #print(k) #打印已迭代次数
x = ans2.reshape((10,-1))
print(x)