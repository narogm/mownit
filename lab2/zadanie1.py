import numpy as np
import time


def get_pivot(A):
    max_i = 0
    max_j = 0
    n = len(A)
    for i in range(n):
        for j in range(n):
            if abs(A[i, j]) > abs(A[max_i, max_j]):
                max_i, max_j = i, j
    return max_i, max_j


def full_pivot_gauss(A):
    n = len(A)
    tmp = [i for i in range(n+1)]
    # skalowanie
    max_i, max_j = get_pivot(A)
    max_val = abs(A[max_i, max_j])
    for i in range(n):
        for j in range(n+1):
            A[i, j] = A[i, j] / max_val

    for k in range(n):
        max_i, max_j = get_pivot(A[k:n, k:n+1])
        A[[k, max_i+k]] = A[[max_i+k, k]]
        A[:, [k, max_j+k]] = A[:, [max_j+k, k]]
        tmp[k], tmp[max_j+k] = tmp[max_j+k], tmp[k]
        for i in range(k+1, n):
            val = A[i][k]/A[k][k]
            for j in range(k, n+1):
                if j == k:
                    A[i][j] = 0
                else:
                    A[i][j] -= val * A[k][j]
        for i in range(k):
            val = A[i][k] / A[k][k]
            for j in range(k, n + 1):
                if j == k:
                    A[i][j] = 0
                else:
                    A[i][j] -= val * A[k][j]
    for i in range(n):
        c = 1.0/A[i][i]
        A[i][i] *= c
        A[i][n] *= c
    ind = 0
    for i in range(n+1):
        if tmp[i] != i:
            ind = tmp.index(i)
            A[i, n], A[ind, n] = A[ind, n], A[i, n]
            tmp[i], tmp[ind] = tmp[ind], tmp[i]
    return A


def gauss_jordan(A):
    n = len(A)
    for i in range(0, n):
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    for i in range(n):
        for k in range(0, i):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    for i in range(n):
        c = 1.0/A[i][i]
        A[i][i] *= c
        A[i][n] *= c
    return A


A = np.array([[1.0, -3.0, 2.0, 3.0], [1.0, 1.0, -2.0, 1.0], [2.0, -1.0, 1.0, -1.0]])
# print(A)
# print()
# B = np.array([[1.0, -3.0, 2.0], [1.0, 1.0, -2.0], [2.0, -1.0, 1.0]])
# C = np.array([3.0, 1.0, -1.0])
B = np.random.rand(500, 500)

#print(B)
#print("|||||||||")
C = np.random.rand(500, 1)
BC = np.hstack([B, C.reshape(-1, 1)])
start = time.time()
D = full_pivot_gauss(BC)
duration = time.time() - start
print(duration)
start = time.time()
X = np.linalg.solve(B, C)
duration = time.time() - start
print(duration)
start = time.time()
E = gauss_jordan(BC)
duration = time.time() - start
print(duration)
#print(D)

# print(full_pivot_gauss(A))
# print()
# print(X)
# print(gauss_jordan(A))
# BC = np.hstack([B, C.reshape(-1,1)])
# print(gauss(BC))


# B = np.array([[1.0, -3.0, 2.0], [1.0, 1.0, -2.0], [2.0, -1.0, 1.0]])
# print(B)
# B[0], B[2] = B[2], B[0]
# print(B)

# B = np.array([[1.0, -3.0, 2.0], [1.0, 1.0, -2.0], [2.0, -1.0, 1.0]])
# print(B)
# B[:, [0, 2]] = B[:, [2,0]]
# print(B)
# tmp = B[0]
# print()
# print(tmp)
# print()
# B[0] = B[2]
# print(B)
# B[2] = tmp
# print(B)