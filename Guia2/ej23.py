import numpy as np
import matplotlib.pyplot as plt

def escalar(v, a, b):
    matriz_escalada = np.array([[a, 0], [0, b]])
    return np.dot(matriz_escalada, v)

def rotar(v, phi_grados):
    phi = np.radians(phi_grados)
    matriz_rot = np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi),  np.cos(phi)]])
    return np.dot(matriz_rot, v)

originales = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])

escalados = [escalar(v, 2, 0.5) for v in originales]
rotados = [rotar(v, 45) for v in originales]

def plot_vectors(vs, titulo, color):
    vs = np.array(vs)
    plt.scatter(vs[:,0], vs[:,1], color=color)
    plt.title(titulo)
    plt.grid(True)
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.xlim(-2, 3)
    plt.ylim(-2, 3)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plot_vectors(originales, "Originales", "blue")

plt.subplot(1, 3, 2)
plot_vectors(escalados, "Escalados (alpha=2, beta=0.5)", "green")

plt.subplot(1, 3, 3)
plot_vectors(rotados, "Rotados (45°)", "red")

plt.tight_layout()
plt.show()