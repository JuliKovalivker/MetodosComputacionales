import numpy as np

def gram_schmidt(vectores):
    base = []
    for v in vectores:
        # Restar proyecciones sobre los vectores ya procesados
        w = v.astype(float)
        for u in base:
            w = w - (np.dot(v, u) / np.dot(u, u)) * u
        
        # Condición para LD: si la norma es casi 0, el vector es LD
        if np.linalg.norm(w) < 1e-10:
            print("Vector linealmente dependiente, se omite.")
            continue
        
        # Normalizar
        base.append(w / np.linalg.norm(w))
    
    return np.array(base).T

# a)
print("=== a) ===")
v1 = np.array([3, 4, 2, 0, 1])
v2 = np.array([0, 0, 5, 5, 6])
v3 = np.array([5, -1, 0, -5, 3])
Q = gram_schmidt([v1, v2, v3])
print("Base ortonormal (columnas):")
print(np.round(Q, 4))
print("Verificación QᵀQ = I:")
print(np.round(Q.T @ Q, 4))

# b)
print("\n=== b) ===")
v1 = np.array([7, 1, 4, 0, 12, -3, 8])
v2 = np.array([-4, 2, 0, 0, 1, -6, 9])
v3 = np.array([11, 11, 41, 0, 12, 99, -15])
Q = gram_schmidt([v1, v2, v3])
print("Base ortonormal (columnas):")
print(np.round(Q, 4))
print("Verificación QᵀQ = I:")
print(np.round(Q.T @ Q, 4))

# c)
print("\n=== c) ===")
v1 = np.array([1, 0, -1])
v2 = np.array([1, 0, 0])
v3 = np.array([0, 0, 1])
Q = gram_schmidt([v1, v2, v3])
print("Base ortonormal (columnas):")
print(np.round(Q, 4))
print("Verificación QᵀQ = I:")
print(np.round(Q.T @ Q, 4))