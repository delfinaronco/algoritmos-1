# Ejercicio 3 recu python

cotizaciones_diarias = {"YPF" : [(1,10),(15, 3), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}
# resultado_esperado es: {"YPF" : (3,100), "ALUA" : (0,50)} 

def valor_min (l: list) -> int:
    min = 31

    for element in l:
        if element <= min:
            min = element
    
    return min

# print(valor_min([4,7,2,0,5]))

def valor_max (l: list) -> int:

    max = 0
    for element in l:
        if element >= max:
            max = element

    return max

def valores_extremos (cotizaciones_diarias: dict) -> dict:
    minmax = {}
    for empresa, cotizaciones in cotizaciones_diarias.items():
        lista = []
        for cotizacion in cotizaciones:
            lista.append(cotizacion[1])

        minmax[empresa] = (valor_min(lista), valor_max(lista))

    return minmax

# valores_extremos(cotizaciones_diarias)

def aprobados_algoritmos (archivo_texto: str) -> dict:

    archivo = open(archivo_texto,'r')
    lista = []
    insuficiente = 0
    final = 0
    coloquio = 0
    res: dict = {}

    for line in archivo.readlines():
        lista += line.split()

    for i in lista:
        if i == "Insuficiente":
            insuficiente += 1
        if i == "Final":
            final += 1
        if i == "Coloquio":
            coloquio += 1

    total = insuficiente + final + coloquio

    res["insuficiente"] = (insuficiente/total) * 100
    res["final"] = (final/total) * 100
    res["coloquio"] = (coloquio/total) * 100
    
    return res


# print(aprobados_algoritmos('algoritmos.txt'))

# Ejericio 4 recu python

def cantApariciones (e: int, s: [int]) -> int:
    contador: int = 0
    for elem in s:
        if elem == e:
            contador += 1

    return contador

# print(cantApariciones(2,[1,2,3,2]))

def cantAparicionesEnPosicion (e: int, pos: int, s: [[int]]) -> int:
    contarPosicionI: Int = 0

    for fila in s:
        for i in range(len(fila)):
            if fila[i] == e and i == pos:
                contarPosicionI += 1

    return contarPosicionI

# print(cantAparicionesEnPosicion(2,1,[[1,2,3],[2,2,6]]))


def es_sudoku_valido (m: list) -> bool:

    for fila in m:
        for elem in fila:
            if elem != 0 and cantApariciones (elem, fila) > 1:
                return False
            
    for elem in [1,2,3,4,5,6,7,8,9]:
        for i in range(0,9):
            if cantAparicionesEnPosicion(elem, i, m) > 1:
                return False
            
    return True

m = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 0, 6, 0, 0, 0, 0],
[0, 0, 0, 5, 0, 0, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 3, 0, 0, 0, 0, 0, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 0, 0]
] 

# print(es_sudoku_valido(m))