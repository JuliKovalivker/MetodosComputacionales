import numpy as np

M = np.array([
    [0.61, 0.29, 0.150],
    [0.32, 0.59, 0.063],
    [0.04, 0.12, 0.787]
])

# valores random
X = 0.5
Y = 0.4
Z = 0.6
XYZ = np.array([X, Y, Z]) 

RGB = np.linalg.inv(M) @ XYZ  # la cosa rara hace la inversa
print("RGB =", RGB)