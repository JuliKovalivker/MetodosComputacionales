
def curr_por_S(curr, S):
    S_size = len(S)
    res = [[0]*S_size for _ in range(S_size)]
    for i in range(S_size):
        for j in range(S_size):
            for h in range(S_size):
                res[i][j] += curr[i][h]*S[h][j]
    return res

def Sk2_rec(S, k, curr):
    if k == 1:
        return curr_por_S(curr, curr)
    else:
        return Sk2_rec(S, k-1, curr_por_S(curr, S))
    
def Sk2(S, k):
    return Sk2_rec(S, k, S)


S_size = 5
S = [[1 if i == j - 1 else 0 for j in range(S_size)] for i in range(S_size)]

k = int(input("Ingresa un k entre 2 y 6: "))
if k < 2 or k > 6:
    print("k invalido, debe estar entre 2 y 6")
else:
    res = Sk2(S, k)
    for i in range(S_size):
            print(res[i])