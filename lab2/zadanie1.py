import numpy as np
import time


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


B = np.random.rand(3, 3)
C = np.random.rand(3, 1)
BC = np.hstack([B, C.reshape(-1, 1)])
start = time.time()
D = gauss_jordan(BC)
duration = time.time() - start
print(duration)
start = time.time()
X = np.linalg.solve(B, C)
duration = time.time() - start
print(duration)
print(X)
print(D)

#A = np.array([[1.0, -3.0, 2.0, 3.0], [1.0, 1.0, -2.0, 1.0], [2.0, -1.0, 1.0, -1.0]])
#print(gauss(A))
#B = np.array([[1.0, -3.0, 2.0], [1.0, 1.0, -2.0], [2.0, -1.0, 1.0]])
#C = np.array([3.0, 1.0, -1.0])
#BC = np.hstack([B, C.reshape(-1,1)])
#print(gauss(BC))