import numpy as np

A = np.array([[4, -1, -1, 0, 0, 0, 0, 0],
     [-1, 4, 0, 1, 0, 0, 0, 0],
     [-1, 0, 4, -1, -1, 0, 0, 0],
     [0, -1, -1, 4, 0, -1, 0, 0],
     [0, 0, -1, 0, 4, -1, -1, 0],
     [0, 0, 0, -1, -1, 4, 0, -1],
     [0, 0, 0, 0, -1, 0, 4, -1],
     [0, 0, 0, 0, 0, -1, -1, 4]])

### a ###

def lu_decomposition(A):
    A = A.astype(float)
    n = A.shape[0]

    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        for k in range(i, n):
            suma = 0
            for j in range(i):
                suma += L[i][j] * U[j][k]
            U[i][k] = A[i][k] - suma

        L[i][i] = 1

        for k in range(i + 1, n):
            suma = 0
            for j in range(i):
                suma += L[k][j] * U[j][i]
            L[k][i] = (A[k][i] - suma) / U[i][i]

    return L, U


L, U = lu_decomposition(A)

print("Matriz L:\n", L)
print("\nMatriz U:\n", U)

print("\nLU - A:\n", L @ U - A)
print("\n¿Es correcto?:", np.allclose(L @ U, A))


### b ###

b =  [5, 15, 0, 10, 0, 10, 20, 30]
y = np.linalg.solve(L, b)

x = np.linalg.solve(U, y)

print("Solución x =\n", x)


### c ###

A_inv = np.linalg.inv(A)

print("A^{-1} =\n", A_inv)
print("\n¿Es densa? (muchos valores no cero)")
print(A_inv)