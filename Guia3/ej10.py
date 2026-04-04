


### a ###
def a(n, m):
    return [[0]*m for _ in range(n)]


### b ###
def b(n, m):
    return [[1]*m for _ in range(n)]

### c ###
def c(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

### d ###
def d(v):
    n = v.size()
    return [[v[i] if i == j else 0 for j in range(n)] for i in range(n)]
