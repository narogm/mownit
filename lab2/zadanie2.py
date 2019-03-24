import numpy as np


def lu(A):
    n = len(A)
    for k in range(n):
        for i in range(k+1, n):
            val = +A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] -= val * A[k, j]
            A[i][k] = val
    return A


def extract_L_and_U(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i > j:
                L[i, j] = A[i, j]
                U[i, j] = 0
            elif i == j:
                L[i, j] = 1
                U[i, j] = A[i, j]
            else:
                L[i, j] = 0
                U[i, j] = A[i, j]
    return L, U


# A = np.array([[5.0, 3.0, 2.0], [1.0, 2.0, 0.0], [3.0, 0.0, 4.0]])
# lu(A)
A = np.random.rand(5, 5)
print(A)
LU = lu(A)
L, U = extract_L_and_U(A)
# print(L)
# print()
# print(U)
# print()
print(L@U)

