import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.array([4, 6, 8, 12, 14, 16, 18])
y = np.array([1.58, 2.08, 2.5, 3.1, 3.4, 3.8, 4.32])

# Matriz A con columnas x, x², x³
A = np.column_stack([x, x**2, x**3])

# Mínimos cuadrados
ATA = A.T @ A
ATb = A.T @ y
beta = np.linalg.solve(ATA, ATb)
print(f"β₁ = {beta[0]:.6f}")
print(f"β₂ = {beta[1]:.6f}")
print(f"β₃ = {beta[2]:.6f}")

# Curva ajustada
x_plot = np.linspace(3, 19, 300)
y_plot = beta[0]*x_plot + beta[1]*x_plot**2 + beta[2]*x_plot**3

# Gráfico
plt.figure(figsize=(7, 5))
plt.scatter(x, y, color='red', zorder=5, label='Datos')
plt.plot(x_plot, y_plot, color='blue', 
         label=f'y = {beta[0]:.4f}x + {beta[1]:.4f}x² + {beta[2]:.4f}x³')
plt.xlabel('x (nivel de ventas)')
plt.ylabel('y (millones de pesos)')
plt.title('Ajuste cúbico por cuadrados mínimos')
plt.legend()
plt.grid(True)
plt.savefig('curva_costos.png')
plt.show()