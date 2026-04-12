import numpy as np

A = np.array([
    [3, -5, -3],
    [6, -2, 0],
    [-8, 4, 1]
], dtype=float)

w = np.array([1, 3, -4], dtype=float)

# NUL(A)
Aw = A @ w
# print("A w =", Aw)


# Col(A)
Ab = np.column_stack((A, w))

rows, cols = Ab.shape

for i in range(rows):
    for j in range(i+1, rows):
        if Ab[i, i] != 0:
            factor = Ab[j, i] / Ab[i, i]
            for k in range(cols):
                Ab[j, k] -= factor * Ab[i, k]

# print("Matriz escalonada:")
# print(Ab)

no_solution = False

for i in range(rows):
    # si todo es 0 a la izquierda y algo != 0 a la derecha => no hay solución
    if np.allclose(Ab[i, :-1], 0) and not np.isclose(Ab[i, -1], 0):
        no_solution = True

if np.allclose(Aw, 0) and not no_solution:
    print("w está en AMBOS (Nul y Col)")
elif np.allclose(Aw, 0):
    print("w solo está en Nul(A)")
elif not no_solution:
    print("w solo está en Col(A)")
else:
    print("w no está en ninguno")