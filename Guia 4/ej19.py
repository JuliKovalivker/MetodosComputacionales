import numpy as np

A = np.array([
    [3, -1,  0,  0],
    [-1, 3, -1,  0],
    [0, -1,  3, -1],
    [0,  0, -1,  3]
], dtype=float)

### a ###

def lu(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i, i] = 1

        # U
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))

        # L
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

    return L, U


L, U = lu(A)

print("L =\n", L)
print("\nU =\n", U)
print("\nVerificación LU - A =\n", L @ U - A)


### b ###

t = np.array([10, 15, 15, 10], dtype=float)


for k in range(1, 5):
    y = np.linalg.solve(L, t)
    t = np.linalg.solve(U, y)

    print(f"\nt{k} =", t)