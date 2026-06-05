import numpy as np
import matplotlib.pyplot as plt

# Datos
puntos = [(1, 2.5), (2, 4.3), (3, 5.5), (4, 6.1)]
x = np.array([p[0] for p in puntos])
y = np.array([p[1] for p in puntos])

# Matriz A con columnas x y x²
A = np.column_stack([x, x**2])

# Mínimos cuadrados: AᵀA β = Aᵀb
ATA = A.T @ A
ATb = A.T @ y
beta = np.linalg.solve(ATA, ATb)
print(f"β₁ = {beta[0]:.4f}, β₂ = {beta[1]:.4f}")

# Curva ajustada
x_plot = np.linspace(0.5, 4.5, 200)
y_plot = beta[0]*x_plot + beta[1]*x_plot**2

# Gráfico
plt.figure(figsize=(7, 5))
plt.scatter(x, y, color='red', zorder=5, label='Datos')
plt.plot(x_plot, y_plot, color='blue', label=f'y = {beta[0]:.3f}x + {beta[1]:.3f}x²')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste por cuadrados mínimos')
plt.legend()
plt.grid(True)
plt.savefig('curva_ajustada.png')
plt.show()
print("Gráfico guardado.")