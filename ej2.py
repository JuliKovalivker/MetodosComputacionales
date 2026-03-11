### a ###
def suma_y_resta(x, y, op):
    res = []
    if op=="+":
        for i in range(len(x)):
            res.append([x[i][j] + y[i][j] for j in range(len(x[i]))])
        return res
    for i in range(len(x)):
        res.append([x[i][j] - y[i][j] for j in range(len(x[i]))])
    return res

### b ###
def multiplicacion_por_escalar(x, y):
    return [[x[j][i]*y for i in range(len(x[j]))] for j in range(len(x))] 

### c ###
def multiplicacion_por_vector(x, y):
    res = []
    sum = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            sum += x[i][j] * y[j]
        res.append(sum)
        sum = 0
    return res

### d ###
def multiplicacion_de_matrices(x, y):
    sub_res = []
    res = []
    sum = 0
    for i in range(len(x)):
        for w in range(len(y[i])):
            for j in range(len(y)):
                sum += x[i][j]*y[j][w]
            sub_res.append(sum)
            sum = 0
        res.append(sub_res)
        sub_res = []
    return res    

matriz_a = [[1, 2, 3],
            [4, 5, 6]]

matriz_b = [[0, 1],
            [2, 3],
            [4, 5]]

# matriz_c = suma_y_resta(matriz_a, matriz_b, "+")
# print(matriz_c)
# matriz_c = suma_y_resta(matriz_a, matriz_b, "-")
# print(matriz_c)

# matriz_d = multiplicacion_por_escalar(matriz_a, 2)
# print(matriz_d)

# vector_a = [2, 3, 4]
# vector_b = multiplicacion_por_vector(matriz_a, vector_a)
# print(vector_b)

matriz_e = multiplicacion_de_matrices(matriz_a, matriz_b)
print(matriz_e)
