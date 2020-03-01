import numpy as np


def generate_random_martix(x, y):
    return np.random.rand(x, y)


def normalize(v):
    return v/np.linalg.norm(v)


def get_sum(M, Q, k):
    sum = 0
    for i in range(k):
        # sum += np.dot(Q[..., i], M[..., i]) * Q[..., i]
        sum += (Q[:, i].dot(M[:, i])) * Q[:, i]
    return sum


def qr(M):
    Q = np.zeros(M.shape)
    print(M)
    Q[:, 0] = normalize(M[:, 0])
    for i in range(1, Q.shape[1]):
        Q[:, i] = normalize(M[:, i] - get_sum(M, Q, i))
    print("Q\n", Q)


# for i in range(1):
M = generate_random_martix(5, 5)
qr(M)
q, r = np.linalg.qr(M)
print(q)
# print(r)
