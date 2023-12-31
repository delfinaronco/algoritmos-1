import random
import numpy as np

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
def ordenados(l) -> bool:
    for i in range (len(l)-1):
        if not (l[i] < l[i+1]): 
            return False
    return True

# print(ordenados([1,2,3,2]))

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

# 7)
def contraFuerte (c: str) -> str:
    def tieneDigito (a:str) -> bool:
        for i in a:
            if i.isdigit():
                return True
        return False
    verde: bool = len(c) > 8  and (not c.islower()) and (not c.isupper()) and tieneDigito(c)
    if verde:
        return "VERDE"
    elif len(c) < 5:
        return "ROJA"
    else:
        return "AMARILLA"
    
# 8) 
def saldo_cuenta (historia: list) -> int:
    saldo: int = 0
    for i in historia:
        if i[0] == "I":
            saldo += i[-1]
        elif i[0] == "R":
            saldo = saldo - i[-1]
    return saldo

# print(saldo_cuenta ([("I",2000),("R",20),("R",1000),("I",300)]))

# 9) 
def tiene_3_vocales_distintas (palabra: str) -> bool:
    palabra.lower()
    vocaleshalladas: list = []
    for letra in palabra:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            vocaleshalladas.append(letra)
    vocaleshalladas = eliminar_repetidos(vocaleshalladas)
    if len (vocaleshalladas) >= 3:
        return True
    else:
        return False
    
# print(tiene_3_vocales_distintas("goool"))  
# print(tiene_3_vocales_distintas("camaleon"))

# SEGUNDA PARTE
# Ejercicio 2

# 1)
def cero_en_pos_pares_inout (l: list[int]) -> list:
    for i in range (len(l)):
        if i % 2 == 0:
            l[i] = 0
    return l

# 2)
def cero_en_pos_pares_in (l: list[int]) -> list:
    listaNueva: list = []
    for i in range (len(l)):
        if i % 2 == 0:
            listaNueva.append(0)
        else:
            listaNueva.append(i)
    return listaNueva

# 3)
def sin_vocales (text: str) -> str:
    vocales: list[str] = ["a","e","i","o","u"]
    nuevoText: str  = ""
    for letter in text:
        if letter not in vocales:
            nuevoText += letter
    return nuevoText

# 4)
def reemplazaVocales (text: str) -> str:
    vocales: list[str] = ["a", "e", "i", "o", "u"]
    nuevoText: str = ""
    for letter in text:
        if letter in vocales:
            nuevoText += "_"
        else:
            nuevoText += letter
    return nuevoText

# 5)
def daVueltaStr (text: str) -> str:
    textDadoVuelta : str = ""
    for i in range(len(text)-1, -1, -1):
        textDadoVuelta += text[i]
    return textDadoVuelta
# 6)
def eliminar_repetidos (l):
    res = []
    for i in range (len(l)):
        if not pertenece (res,l[i]):
            res.append(l[i])
    return res

# print(eliminar_repetidos(["hola","hola","chau"]))
    
# Ejercicio 3
def aprobado (notas: list[int]) -> int:
    promedio: int = sumTotal(notas) / len(notas)
    for i in range (0,len(notas)):
        if all (nota >= 4 for nota in notas) and promedio >= 7:
            res = 1
        elif all (nota >= 4 for nota in notas) and promedio >= 4 and promedio < 7:
            res = 2
        else:
            res = 3
    return res

# Ejercicio 4
# 1)
def mis_estudiantes ():
    mis_estudiantes: list = []
    name = ""
    while name != "listo":
        name = input("nombre de estudiantes:")
        mis_estudiantes.append(name)
        if pertenece (mis_estudiantes,"listo"):
            mis_estudiantes.remove("listo")
    return (mis_estudiantes)

# 2)
def sube()-> int:
    saldo = 0
    historial: list = []
    tipoDeOperacion = ""
    while tipoDeOperacion != "X":
        tipoDeOperacion = input("OPERACION A REALIZAR: ")
        if tipoDeOperacion == "C":
            monto = int(input("MONTO: "))
            saldo += monto
            historial.append((tipoDeOperacion, monto))
        elif tipoDeOperacion == "D":
            monto = int(input("MONTO: "))
            saldo = saldo - monto
            historial.append((tipoDeOperacion, monto))
    return f"{historial}, tu saldo disponible es:{saldo}"

# print(sube())

# Ejercicio 5
# 1)
def pertenece_a_cada_uno (l: list, elem: int) -> bool:
    res: list[bool] = []
    for sublista in l:
        if pertenece (sublista,elem):
            res.append(True)
        else:
            res.append(False)
    print(res)

# pertenece_a_cada_uno([[1,2,3],[2,4]],1)

# 2)
def es_matriz (s: list) -> bool:
    inicio: int = len(s[0])
    for i in range(len(s)):
        if inicio != len(s[i]):
            return False
    return True

# print(es_matriz([[1,2],[1,2],[1,2,3]]))

# 3)
def filas_ordenadas (matriz: list) -> list:
    res: list[bool] = []
    for fila in matriz:
        if ordenados(fila) == True:
            res.append(True)
        else:
            res.append(False)
    return res

# print(filas_ordenadas ([[1,2,3],[3,2],[4,6,9]]))



