import numpy as np
# import matplotlib.pyplot as plt


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def get_sum(A, Q, k):
    sum = 0
    for i in range(k):
        sum += (Q[:, i].dot(A[:, i])) * Q[:, i]
    return sum


def qr(A):
    Q = np.zeros((A.shape[0], A.shape[1]))
    R = np.zeros((A.shape[0], A.shape[1]))
    for i in range(Q.shape[0]):
        Q[:, i] = A[:, i] - get_sum(A, Q, i)
        Q[:, i] = normalize(Q[:, i])

    for i in range(R.shape[0]):
        for j in range(i, R.shape[1]):
            R[i, j] = Q[:, i].dot(A[:, i])

    return Q, R


# def generate_matrices():
#     matrices_conds = []
#     matrix = np.random.rand(8, 😎
#     for i in range(60):
#         u, s, vh = np.linalg.svd(matrix, full_matrices=False)
#         s[0] *= 1.1
#         cond = s[0] / s[1]
#         matrix = np.matmul(u * s[..., None, 🙂, vh)
#         matrices_conds.append((matrix, cond))
#         print(cond)
#     return matrices_conds
#

A = np.random.rand(5, 5)
print(A)
q, r = np.linalg.qr(A)
print(q)
# print(r)

print("*********************************")
# print(A)
my_q, my_r = qr(A)
print(q)
# print(r)
#
# conds = []
# norms = []
# d = generate_matrices()
# d = list(sorted(d, key=lambda t: t[1]))
# for i in range(len(d)):
#     matrix = d[i][0]
#     q, _ = qr(matrix)
#     conds.append(d[i][1])
#     norms.append(np.linalg.norm(np.identity(matrix.shape[0]) - q.T @ q))
#
# print(norms)
# plt.scatter(conds, norms)
# plt.show()