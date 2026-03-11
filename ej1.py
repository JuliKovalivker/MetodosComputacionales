### mucho abuso de notacion ###

def error():
    return "Los vectores poseen tamanios distintos"

def misma_len(x, y):
    return len(x) == len(y)

### a ###
def suma_y_resta(x, y, op):
    return ([x[i] - y[i] for i in range(len(x))] if op == "+" else [x[i] + y[i] for i in range(len(x))]) if misma_len(x, y) else error()

### b ###
def multiplicacion_por_escalar(x, y):
    return [x[i]*y for i in range(len(x))]

### c ###
def dot_product(x, y):
    if not misma_len(x, y): return error()
    res = 0
    for i in range(len(x)):
        res += x[i]*y[i]
    return res


vector_a = [1, 2, 3]
vector_b = [0, 1, 2]

vector_c = suma_y_resta(vector_a, vector_b, "+")
print(vector_c)
vector_c = suma_y_resta(vector_a, vector_b, "-")
print(vector_c)

vector_d = multiplicacion_por_escalar(vector_a, 2)
print(vector_d)

num = dot_product(vector_a, vector_b)
print(num)