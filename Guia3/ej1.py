import random

# matriz simetrica
def S1(n):
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            val = random.randint(-100, 100)
            A[i][j] = val
            A[j][i] = val
    return A

def S2(n):
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        A[i][i] = random.randint(-100, 100)
    for i in range(n):
        for j in range(i+1, n): # no piso la diagonal
            val = random.randint(-100, 100)
            A[i][j] = val
            A[j][i] = 1 - val
    return A

# matriz antisimetrica
def S3(n):
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n): # diagonal de 0s: aij = -aji <=> aij = aji = 0
            val = random.randint(-100, 100)
            A[i][j] = val
            A[j][i] = -val
    return A

# matriz de traza nula
def S4(n):
    A = [[random.randint(-100, 100) for _ in range(n)] for _ in range(n)]
    suma = sum(A[i][i] for i in range(n))
    A[n-1][n-1] -= suma # mato a todos con el ultimo elemento pero habia infinitas formas de resolverlo
    return A

# matriz fila nula
def S5(n):
    fila_nula = random.randint(0, n-1)
    A = [[0 if i == fila_nula else random.randint(-100, 100) for _ in range(n)] for i in range(n)]
    return A


# aca me parece que esta mal la consigna porque dice matrices triangulares superiores
# pero define una traingular inferior, hago ambas por las dudas

# matriz triangular inferior
def S6_inferior(n):
    A = [[random.randint(-100, 100) if i >= j else 0 for j in range(n)] for i in range(n)]
    return A

# matriz triangular superior
def S6_superior(n):
    A = [[random.randint(-100, 100) if i <= j else 0 for j in range(n)] for i in range(n)]
    return A