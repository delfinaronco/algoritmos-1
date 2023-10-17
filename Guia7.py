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
    if len (vocaleshalladas) >= 3:
        return True
    else:
        return False
            
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
    return historial

# print(sube())

