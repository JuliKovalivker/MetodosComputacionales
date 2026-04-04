import numpy as np

# supongo A siempre de 4x4
def test_I(A):
    A = np.array(A)
    I = np.eye(4) #np.eye(4) hace I de 4x4

    izq = np.dot((A + I), (A - I)) # @ hace lo mismo
    der = np.dot(A, A) - I
   
    return np.allclose(izq, der)

# supongo A  y B siempre de 4x4
def test_B(A, B):
    A = np.array(A)
    B = np.array(B)

    izq = np.dot((A + B), (A - B))
    der = np.dot(A, A) - np.dot(B, B)
   
    return np.allclose(izq, der)


# testeo ambas funciones
def testear_I(k):
    for i in range(k):
        A = np.random.randint(-10, 10, (4, 4))
        if not test_I(A):
            print(f"Falló en test {i+1}")
            return
    print("Todos los test_I dieron True")
testear_I(10)

def testear_B(k):
    for i in range(k):
        A = np.random.randint(-10, 10, (4, 4))
        B = np.random.randint(-10, 10, (4, 4))
        print(f"Test {i+1}: {test_B(A, B)}")
testear_B(10)