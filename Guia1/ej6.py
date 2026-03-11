import matplotlib.pyplot as plt
import numpy as np

### a ###
def plot_functions(m1, b1, m2, b2):
    x = np.linspace(-3, 7, 100)
    y1 = m1*x + b1
    y2 = m2*x + b2
    plt.plot(x, y1)
    plt.plot(x, y2)
    # plt.show()

### c ###
def ec_after_sustitution(m1, b1, m2, b2):
    # m1*x + b1 = m2*x + b2
    # m1*x - m2*x = b2 - b1
    # x*(m1 - m2) = b2 - b1
    # x = (b2 - b1)/(m1 - m2)
    x = (b2- b1)/(m1 - m2)
    plt.axvline(x)
    plt.show()


m1, b1 = 1, 0
m2, b2 = -0.5, 3

plot_functions(m1, b1, m2, b2)
ec_after_sustitution(m1, b1, m2, b2)

