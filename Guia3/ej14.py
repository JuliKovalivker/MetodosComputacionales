import numpy as np
import itertools

M = np.array([
    [1, 0, -1, 0],
    [0, 1, 0, 0],
    [-1, 0, 1, 0],
    [0, 0, 0, 1]
])

posibles_vectores = list(itertools.product([0,1], repeat=4))

for x_tuple in posibles_vectores:
    x = np.array(x_tuple)
    resultado = x.T @ M @ x
    if resultado == 0 and np.any(x != 0):  # descartar el vector nulo
        print("Vector que coincide con el patrón:", x, "-> x^T M x =", resultado)