
def Ak_rec(A, k, curr):
    if k == 1:
        return curr
    else:
        A_size = len(A)
        res = [[0]*A_size for _ in range(A_size)]
        for i in range(A_size):
            for j in range(A_size):
                for h in range(A_size):
                    res[i][j] += curr[i][h]*A[h][j]
        return Ak_rec(A, k-1, res)
    
def Ak(A, k):
    return Ak_rec(A, k, A)

A = [[1/6, 1/2, 1/3],
     [1/2, 1/4, 1/4],
     [1/3, 1/4, 5/12]]

k = int(input("Ingresa un k grande : "))
res = Ak(A, k)
for i in range(3):
    print(res[i])

# Con K -> infinito cada posicion de la matriz converge a 1/3