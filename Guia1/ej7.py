import matplotlib.pyplot as plt
import numpy as np

# Este ejercicio es una version mas facil del 6 basicamente,
# por eso le robe la funcion y la hardcodee

def plot_functions(b1, b2):
    x = np.linspace(-3, 7, 100)
    y1 = (3*x + b1)/2
    y2 = (6*x + b2)/4
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()

b1 = 1
b2 = 2

plot_functions(b1, b2)