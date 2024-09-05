import numpy as np

def qr_algorithm(matrix, max_iterations=1000, tolerance=1e-10):
    A = matrix.copy()

    for iteration in range(max_iterations):
        # QR分解
        Q, R = np.linalg.qr(A)

        # 相似变换
        A = np.dot(R, Q)

        # 判断是否收敛
        off_diagonal = np.sum(np.abs(A - np.triu(A)))  # 计算上三角形元素之外的绝对值和
        if off_diagonal < tolerance:
            break

    # 提取特征值
    eigenvalues = np.diag(A)

    # 提取特征向量
    eigenvectors = np.linalg.inv(Q)  # 反向迭代

    return eigenvalues, eigenvectors

# 示例矩阵
matrix = np.array([[2, 1, 0],
                   [1, 3, 1],
                   [0, 1, 4]])

# 调用QR算法
eigenvalues, eigenvectors = qr_algorithm(matrix)

# 打印结果
print("特征值:", eigenvalues)
print("特征向量:\n", eigenvectors)
