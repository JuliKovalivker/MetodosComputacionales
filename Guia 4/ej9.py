import numpy as np

A = np.array([
    [3, -5, -9],
    [8, 7, -6],
    [-5, -8, 3],
    [2, -2, -9]
], dtype=float)

y = np.array([-4, -8, 6, -5], dtype=float)

# matriz aumentada
Ab = np.column_stack((A, y))

rows, cols = Ab.shape

for i in range(rows):
    pivot = Ab[i, i] if i < cols - 1 else 0
    for j in range(i + 1, rows):
        if Ab[i, i] != 0:
            factor = Ab[j, i] / Ab[i, i]
            for k in range(cols):
                Ab[j, k] = Ab[j, k] - factor * Ab[i, k]

print("Matriz escalonada:")
print(Ab)

no_solution = False

for i in range(rows):
    if np.allclose(Ab[i, :-1], 0) and not np.isclose(Ab[i, -1], 0):
        no_solution = True

if no_solution:
    print("NO tiene solución (no está en el subespacio)")
else:
    print("Tiene solución (está en el subespacio)")