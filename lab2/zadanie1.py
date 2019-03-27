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
    for i in range(n+1):
        if tmp[i] != i:
            ind = tmp.index(i)
            A[i, n], A[ind, n] = A[ind, n], A[i, n]
            tmp[i], tmp[ind] = tmp[ind], tmp[i]
    return A


def get_times(sizes):
    for i in sizes:
        print("size: ", i)
        B = np.random.rand(i, i)
        C = np.random.rand(i, 1)
        BC = np.hstack([B, C.reshape(-1, 1)])
        start = time.time()
        D = full_pivot_gauss(BC)
        duration = time.time() - start
        print("time for my algorithm: ", duration)
        start = time.time()
        X = np.linalg.solve(B, C)
        duration = time.time() - start
        print("time for library algorithm: ", duration, "\n---------------\n")


get_times([10, 200, 500])

# start = time.time()
# E = gauss_jordan(BC)
# duration = time.time() - start
# print(duration)
# print(D)
