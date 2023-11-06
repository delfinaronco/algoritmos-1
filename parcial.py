# Ejercicio 3

def matriz_capicua (m: list) -> bool:

    for i in m:
        if i != i[::-1]:
            return False

    return True

# print(matriz_capicua([[1,2,1],[2,0,1]]))

# Ejercicio 1

def intercalar (s1: list, s2: list) -> list:

    res = []

    lista_concatenada = s1 + s2

    for i in range(len(lista_concatenada)):
        if i % 2 == 0:
            res.append(s1[0])
            s1.remove(s1[0])
        else:
            res.append(s2[0])
            s2.remove(s2[0])

    return res
    

# print(intercalar([1,2,3],[4,5,6]))

# debería devolver [1,4,2,5,3,6]

# Ejercicio 3

def n_apariciones (l: list, n: int, e: int) -> int:

    contador = 0

    for i in range(len(l)):
        if l[i] == e:
            contador += 1
        if contador == n:
                return i

    return -1


# print(n_apariciones([33,129,98,129,33],3,129))

# Ejercicio 2

caballos = ['pepito','juanita','carlos','rayo']

carreras = {'carrera1':['juanita','pepito','rayo','carlos'],'carrera2':['rayo','carlos','pepito','juanita']}

def pos_caballos (caballos: list, carreras: dict) -> dict:
    
    claves_caballos: dict = {}

    for i in caballos:
        
