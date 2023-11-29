# Guia 7
# LISTAS

def pertenece (l:list, e) -> bool:
    if e in l:
        return True
    else:
        return False
    
# print(pertenece(["hola","chau"],"hola"))
    
def divide_a_todos (l:list, e:int) -> bool:
    for i in l:
        if not (i % e) == 0:
            return False
        
    return True

# print(divide_a_todos([3,6,9,18],3))

def sumaTotal (s:list) -> int:
    suma = 0

    for i in s:
        suma += i

    return suma

# print(sumaTotal([20,10,35]))

def ordenados (s:list) -> bool:
    for i in range(len(s)-1):
        if not (s[i] <= s[i+1]):
            return False
        
    return True

# print(ordenados([5,4,3]))

def longitud_mayor_a_7 (l:list) -> bool:
    for i in l:
        if len(i) > 7:
            return True
        
    return False

#print(longitud_mayor_a_7 (["hola","chau","ornitorrinco"]))

def es_palindromo (palabra: str) -> bool:

    i: int = len(palabra) - 1
    p_invertida: str = ''

    while i >= 0:

        p_invertida += palabra [i]
        i -= 1

    return palabra == p_invertida

# print(es_palindromo ("oso"))


def formatear_texto (texto: str) -> str:
    texto_formateado = texto

    texto_formateado = texto_formateado.replace (' ','')
    texto_formateado = texto_formateado.lower()

    return texto_formateado

#print(formatear_texto("Ho la"))

def es_palindromo2 (palabra: str) -> str:
    invertida: str = ''

    for i in range(len(palabra)-1,-1,-1):
        invertida += palabra[i]
    
    palabra_formateada = formatear_texto(palabra)
    invertida_formateada = formatear_texto(invertida)

    return palabra_formateada == invertida_formateada

# print(es_palindromo2("a la torre derrotala"))


def hay_mayuscula (palabra: str) -> bool:

    for i in palabra:
        if i.isupper():
            return True
    return False
    
# print (hay_mayuscula("holA"))

def hay_minuscula (palabra: str) -> bool:

    for i in palabra:
        if i.islower():
            return True
        
    return False

# print(hay_minuscula("HOLA"))

def hay_numero (caracters: str) -> bool:

    for i in caracters:
        if i.isnumeric():
            return True
        
    return False

# print(hay_numero("delfi12"))

def fortaleza_contraseña (contra: str) -> str:

    if (len(contra) > 7) and hay_mayuscula(contra) and hay_minuscula(contra) and hay_numero(contra):
        return "VERDE"
    elif (len(contra)) < 5:
        return "ROJA"
    else:
        return "AMARILLA"
    
# print(fortaleza_contraseña("Del"))

# también lo podía hacer con el código ascii

def hay_mayuscula_ascii (contra: str) -> bool:

    for i in contra:
        if not (65 <= ord(i) <= 90):
            return False
        
    return True

# print(hay_mayuscula("deLfi"))

def hay_minuscula_ascii (contra: str) -> bool:

    for i in contra:
        if not (97 <= ord(i) <= 122):
            return False
        
    return True

# print(hay_minuscula("HOLA"))

def hay_numero_ascii (contra: str) -> bool:

    for i in contra:
        if 48 <= ord(i) <= 57:
            return True
        
    return False

# print(hay_numero_ascii("delfi"))

def cuenta_bancaria (historial: list) -> int:

    saldo = 0

    for i in historial:
        if i[0] == "I":
            saldo += i[1]

        elif i[0] == "R":
            saldo -= i[1]

    return saldo

# print(cuenta_bancaria([("I",2000),("R",300)]))


def eliminar_repetidos (l: list) -> list:
    res: list = []

    for i in l:
        if not (pertenece(res,i)):
            res.append(i)

    return res

# print(eliminar_repetidos(["a","e","a","u"]))


def almenos_3_vocales_distintas (palabra: str) -> bool:
    vocales: list = []

    for i in palabra:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vocales.append(i)

    vocales = eliminar_repetidos(vocales)

    if len(vocales) >= 3:
        return True
    else:
        return False

# print(almenos_3_vocales_distintas("avion"))

def cero_posiciones_pares (l: list) -> list:

    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = 0

    return l

# print(cero_posiciones_pares([1,2,3,4,5,6]))

def cero_pos_pares_lista_nueva (l: list) -> list:

    nueva_lista: list = []

    for i in range(len(l)):
        nueva_lista.append(l[i])

    for i in range(len(nueva_lista)):
        if i % 2 == 0:
            nueva_lista[i] = 0

    return nueva_lista

# print(cero_pos_pares_lista_nueva([1,2,3,4,5,6]))

def sin_vocales (palabra: str) -> str:

    res: str = ''

    for i in palabra:
        if not (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
            res += i 

    return res

# print(sin_vocales("hola"))

def reemplaza_vocales (texto: str) -> str:

    vocales = ["a","e","i","o","u"]
    res: str = ''

    for i in texto:
        if pertenece (vocales,i):
            res += '_'
        else:
            res += i

    return res

# print(reemplaza_vocales("ornitorrinco"))

def da_vuelta_str (palabra: str) -> str:

    res: str = ''

    for i in range(len(palabra)-1,-1,-1):
        res += palabra[i]
    
    return res

# print(da_vuelta_str("hola"))
    
def promedio (notas: list) -> float:

    res = sumaTotal(notas) / len(notas)

    return res

# print(promedio([7,10,8,9,10]))

def aprobado (notas: list) -> int:

    for i in notas:
        if i >= 4 and promedio(notas) >= 7:
            return 1
        
        elif i >= 4 and (4 <= promedio(notas) < 7):
            return 2
    
        elif not (i >= 4) or promedio(notas) < 4:
            return 3
        
# print(aprobado([5,6]))

def mis_estudiantes () -> list:

    nombre: str = input("nombres de estudiantes: ")
    listaEstudiantes: list = []
    
    while nombre != 'listo':
        listaEstudiantes.append(nombre)
        nombre: str = input("nombres de estudiantes: ")

    return listaEstudiantes 

# print(mis_estudiantes())

def sube () -> list:
    operacion: str = ""
    historial: list = []
    saldo: int = 0

    while operacion != "X":
        operacion: str = input("operacion: ")

        if operacion == "C":
            monto = int(input ("monto: "))
            saldo += monto
            historial.append(("C",monto))
            
        elif operacion == "D":
            monto = int(input("monto: "))
            saldo -= monto 
            historial.append(("D",monto)) 

    return f"{historial}, tu saldo disponible es: {saldo}"

# print(sube())

def pertenece_a_cada_uno (lista: list, n: int) -> list:
    res: list = []

    for i in lista:
        if pertenece (i,n):
            res.append(True)
        else: 
            res.append(False)

    return res

# print(pertenece_a_cada_uno([[1,2,3],[2,3,4],[1,2,1]],3))

def es_matriz (s: list) -> bool:

    for i in range(len(s)):
        if len(s[0]) != len(s[i]):
            return False
        
    return True
                          
# print(es_matriz([[1,2,3],[2,1,4],[5,5,5]]))

def filas_ordenadas (matriz: list) -> list:
    res: list = []

    for fila in matriz:
        if not ordenados(fila):
            res.append(False)
        else:
            res.append(True)

    return res

# print(filas_ordenadas([[1,2,3],[2,1,3],[1,2,2]]))


