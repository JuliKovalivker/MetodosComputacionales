import numpy as np

def gram_schmidt(vectores):
    base = []
    for v in vectores:
        w = v.astype(float)
        for u in base:
            w = w - (np.dot(v, u) / np.dot(u, u)) * u
        if np.linalg.norm(w) < 1e-10:
            print("Vector linealmente dependiente, se omite.")
            continue
        base.append(w / np.linalg.norm(w))
    return np.array(base).T

def factorizacion_QR(A):
    columnas = [A[:, i] for i in range(A.shape[1])]
    Q = gram_schmidt(columnas)
    R = Q.T @ A
    return Q, R

# Prueba con columnas LI
print("=== Columnas linealmente independientes ===")
A = np.array([
    [3, 0,  5],
    [4, 0, -1],
    [2, 5,  0],
    [0, 5, -5],
    [1, 6,  3]
], dtype=float)

Q, R = factorizacion_QR(A)
print("Q ="); print(np.round(Q, 4))
print("R ="); print(np.round(R, 4))
print("Verificación A = QR:"); print(np.round(Q @ R, 4))

# Prueba con columnas LD
print("\n=== Columnas linealmente dependientes ===")
B = np.array([
    [1, 1, 0],
    [0, 0, 0],
    [-1, 0, 1]
], dtype=float)

Q, R = factorizacion_QR(B)
print("Q ="); print(np.round(Q, 4))
print("R ="); print(np.round(R, 4))
print("Verificación A = QR:"); print(np.round(Q @ R, 4))