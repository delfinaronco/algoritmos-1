# Ejercicio 1

# 1)
def pertenece (l: list, e: int) -> bool:
    if e in l:
        return True
    else:
        return False

# print (pertenece([1,2,3],4))

def pertenece2 (l,e) -> bool:  # si usamos tios genéricos puede buscar un caracter dentro de un string
    if e in l:
        return True
    else:
        return False
    
# print (pertenece("hola","p"))

# falta otra manera

# 2)
def divideATodos (s: list[int], e: int) -> bool:
    for i in s:
        if i % e != 0:
            return False
    else:
        return True
    
# print(divideATodos([3,9,27,81],3))

# 3)
def sumTotal (s: list[int]) -> int:
    suma = 0
    for i in s:
        suma += i
    return suma

# print(sumTotal([1,2,3,4,5]))

# 4)
def ordenados(s: list[int]) -> bool:
    elemanterior: int = s[0]
    s = s[1::]
    for i in s:
        if elemanterior > i:
            return False
        else:
            elemanterior = i
    return True

# print(ordenados ([1,2,3,4,1]))

# 5)
def palabraMayorA7 (l: list[str]) -> bool:
    for i in l:
        if len (i) > 7:
            return True
    return False
        
# print(palabraMayorA7(["oceano","hola","estupendo"]))

# 6)
def esPalindromo (l: str) -> bool:
    l = l.lower() # pasa l todo a lowercase
    for i in l:
        if i != l[-1]:
            return False
        else:
            l = l[:-1:]
    return True

# print(esPalindromo ("oso"))

