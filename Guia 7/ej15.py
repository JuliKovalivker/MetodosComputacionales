import numpy as np

A = np.array([
    [-6, -3,  6,  1],
    [-1,  2,  1, -6],
    [ 3,  6,  3, -2],
    [ 6, -3,  6, -1],
    [ 2, -1,  2,  3],
    [-3,  6,  3,  2],
    [-2, -1,  2, -3],
    [ 1,  2,  1,  6]
])

n = A.shape[1]
for i in range(n):
    for j in range(i+1, n):
        prod = np.dot(A[:,i], A[:,j])
        print(f"col{i+1} · col{j+1} = {prod}")

print("¿Las columnas son ortogonales?", all(
    np.dot(A[:,i], A[:,j]) == 0 
    for i in range(n) for j in range(i+1, n)
))

ATA = A.T @ A
print("AᵀA =")
print(ATA)
print("\nLas columnas son ortogonales porque AᵀA es diagonal:", 
      np.all(ATA - np.diag(np.diagonal(ATA)) == 0))