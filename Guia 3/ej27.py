
def mult_por_bloques(A, B, n):
    size = len(A)
    C = [[0 for _ in range(size)] for _ in range(size)]
    for i0 in range(0, size, n):    
        for j0 in range(0, size, n):
            for k0 in range(0, size, n):
                for i in range(i0, min(i0+n, size)):
                    for j in range(j0, min(j0+n, size)):
                        for k in range(k0, min(k0+n, size)):
                            C[i][j] += A[i][k] * B[k][j]
    return C

# def mult_por_bloques(A, B):
#     size = len(A)
    
#     if size == 1:
#         return [[A[0][0] * B[0][0]]]
    
#     mid = size // 2
    
#     A11 = [fila[:mid] for fila in A[:mid]]
#     A12 = [fila[mid:] for fila in A[:mid]]
#     A21 = [fila[:mid] for fila in A[mid:]]
#     A22 = [fila[mid:] for fila in A[mid:]]
    
#     B11 = [fila[:mid] for fila in B[:mid]]
#     B12 = [fila[mid:] for fila in B[:mid]]
#     B21 = [fila[:mid] for fila in B[mid:]]
#     B22 = [fila[mid:] for fila in B[mid:]]

#     A11_B11 = mult_por_bloques(A11, B11)
#     A12_B21 = mult_por_bloques(A12, B21)
#     C11 = [[A11_B11[i][j] + A12_B21[i][j] for j in range(len(A11_B11))] for i in range(len(A11_B11))]
    
#     A11_B12 = mult_por_bloques(A11, B12)
#     A12_B22 = mult_por_bloques(A12, B22)
#     C12 = [[A11_B12[i][j] + A12_B22[i][j] for j in range(len(A11_B12))] for i in range(len(A11_B12))]
    
#     A21_B11 = mult_por_bloques(A21, B11)
#     A22_B21 = mult_por_bloques(A22, B21)
#     C21 = [[A21_B11[i][j] + A22_B21[i][j] for j in range(len(A21_B11))] for i in range(len(A21_B11))]

#     A21_B12 = mult_por_bloques(A21, B12)
#     A22_B22 = mult_por_bloques(A22, B22)
#     C22 = [[A21_B12[i][j] + A22_B22[i][j] for j in range(len(A21_B12))] for i in range(len(A21_B12))]

#     C = []
#     for i in range(mid):
#         fila = []
#         for j in range(mid):
#             fila.append(C11[i][j])
#         for j in range(mid):
#             fila.append(C12[i][j])
#         C.append(fila)
#     for i in range(mid):
#         fila = []
#         for j in range(mid):
#             fila.append(C21[i][j])
#         for j in range(mid):
#             fila.append(C22[i][j])
#         C.append(fila)
    
#     return C
