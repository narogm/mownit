import numpy as np
import time
import scipy.linalg


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


def get_times(sizes):
    for i in sizes:
        print("size: ", i)
        A = np.random.rand(i, i)
        start = time.time()
        LU = lu(A)
        duration = time.time() - start
        print("time for my algorithm: ", duration)
        start = time.time()
        P, L, U = scipy.linalg.lu(A)
        duration = time.time() - start
        print("time for library algorithm: ", duration, "\n---------------\n")


# get_times([10, 50, 200, 500])

A = np.random.rand(5, 5)
print(A)
LU = lu(A)
print()
print(LU)
L, U = extract_L_and_U(A)
print()
print(L)
print()
print(U)
print()
print(L@U)