# Ejercicio 1

# 1)
def contar_lineas (nombre_archivo: str) -> int:
    archivo: str = open(nombre_archivo,'r')
    lineas: list = []

    for line in archivo.readlines():
        lineas.append(line)

    return len(lineas)

# print(contar_lineas('archivo_palabras.txt'))

# 2)
def existe_palabra (palabra: str, nombre_archivo_input: str) -> bool:
    archivo_input = open(nombre_archivo_input,'r')
    lista_palabras = []

    for line in archivo_input.readlines():
        lista_palabras += line.split()

    if palabra not in lista_palabras:
        return False
    else:
        return True

# print(existe_palabra('una','archivo_palabras.txt'))

# 3)
def cantidad_apariciones (nombre_archivo: str, palabra: str) -> int:
    archivo_input = open(nombre_archivo,'r')
    lista_palabras = []
    apariciones = []
    diccionario = {}

    for line in archivo_input.readlines():
        lista_palabras += line.split()
        
    for word in lista_palabras:
        
        if word in diccionario:
            diccionario[word] += 1
        else:
            diccionario[word] = 1

    for word in diccionario:
        apariciones.append(diccionario[word])
        
    if palabra in diccionario:
        return diccionario[palabra]

# print(cantidad_apariciones('archivo_palabras.txt',"prueba"))

# Ejercicio 2
def es_un_comentario(line: str) -> bool:
    for c in line:
        if c != ' ':
            if c == '#':
                return True # es un comentario
            return False # NO es un comentario
    return False # caso todos chars ' '

def clonarSinComentarios(nombre_archivo_input: str) -> None:

# abrir archivo de input
    archivo_input = open (nombre_archivo_input,"r")

# Idem output
    nombre_archivo_output: str = 'ejercicio_2_output.txt'
    archivo_output = open(nombre_archivo_output,"w")

    for line in archivo_input.readlines():
        if not es_un_comentario(line):
            archivo_output.write(line)

    archivo_input.close()
    archivo_output.close()

# clonarSinComentarios('ejercicio_2_input.txt')

# Ejercicio 3

def reverso (nombre_archivo_input: str):
    archivo_input: str = open(nombre_archivo_input,'r')

    nombre_archivo_output: str = 'reverso.txt'
    archivo_output = open(nombre_archivo_output, 'w')
    
    lineas: list = []

    for line in archivo_input.readlines():
        lineas.append(line)

    lineas.reverse()

    for line in lineas:
        archivo_output.write(f"{line}\n")

# reverso('archivo_palabras.txt')

# Ejercicio 4

def frase (nombre_archivo: str, nueva_frase: str):
    archivo: str = open (nombre_archivo,'r')

    todas_las_lineas: list = []

    for line in archivo.readlines():
        todas_las_lineas.append(line)

    todas_las_lineas.append(nueva_frase)

    archivo: str = open(nombre_archivo,'w')

    print(todas_las_lineas)

    for line in todas_las_lineas:
        
        archivo.write(line)

# frase('archivo_palabras.txt',"que onda")

# Ejercicio 5

def frase_al_inicio (nombre_archivo: str, nueva_frase: str):
    archivo: str = open (nombre_archivo,'r')

    todas_las_lineas: list = []

    for line in archivo.readlines():
        todas_las_lineas.append(line)

    todas_las_lineas.insert(0,f"{nueva_frase}\n")

    print(todas_las_lineas)

    archivo: str = open(nombre_archivo,'w')
    for line in todas_las_lineas:
        archivo.write(line)

# frase_al_inicio('archivo_palabras.txt',"que onda")

# PILAS
from queue import LifoQueue as Pila

# Ejercicio 9

p = Pila()
p.put(1)
p.put(2)
p.put(3)

def pila_copy (p: Pila) -> Pila:
    elements = []
    p_copy = Pila()

    while not p.empty():
        elements.append(p.get())

    for i in range (len(elements)-1,-1,-1):
        p_copy.put(elements[i])

    return p_copy


def cantidad_elementos (p: Pila) -> int: 

    contador = 0

    while not p.empty():
        elemento = p.get()
        contador += 1

    return contador

# print(cantidad_elementos(p))

# Ejercicio 10
from queue import LifoQueue

def copiar(p: LifoQueue) -> LifoQueue:
    elements:[int] = []
    while not p.empty():
        elements.append(p.get())
    p_copy: LifoQueue = LifoQueue()
    for i in range(len(elements)-1,0-1,-1):
        p.put(elements[i])
        p_copy.put(elements[i])
    return p_copy

def buscarElMaximo (p: LifoQueue) -> int:
    p_copy: LifoQueue = copiar(p)
    value = p_copy.get()
    while not p_copy.empty():
        next_value = p_copy.get()
        value = max(next_value, value)
    return value

pila: LifoQueue = LifoQueue()
pila.put(1)
pila.put(3)
pila.put(-4)
# print(list(pila.queue))
# print(buscarElMaximo(pila))

# Ejercicio 16
import numpy as np
from queue import Queue
import random

def armarSecuenciaDeBingo() -> Queue:
    l: [int] = []
    for i in range(0,99+1,1):
        l.append(i)
    random.shuffle(l)
    result: Queue[int] = Queue()
    for elem in l:
        result.put(elem)
    return result

bolillero = armarSecuenciaDeBingo()
# print(bolillero.get())

carton = [4,20,30,40,65,81,22,61,49,72,14,35]
def jugarCartonDeBingo (carton: list, bolillero: Queue) -> int:
    jugadas = 0
    casillas_completadas_en_carton = 0
    while not bolillero.empty():
        # saco una bola
        bola = bolillero.get()
        jugadas += 1
        if bola in carton:
            casillas_completadas_en_carton += 1
            # chequeo si gané
        if casillas_completadas_en_carton == len(carton):
            return jugadas
    return -1

print(jugarCartonDeBingo(carton,bolillero))

# Ejercicio 19

def agruparPorLongitud (nombre_archivo_input: str) -> dict:
    archivo_input = open(nombre_archivo_input,'r')     # Abre el archivo en modo lectura

    res : dict = {}

    for line in archivo_input.readlines():
        for word in line.split():
            if len(word) not in res:
                
                res[len(word)] = 1
            else:
                res[len(word)] += 1
        
    archivo_input.close()

    return res

# print(agruparPorLongitud('archivo_palabras.txt'))

# Ejercicio 21

def laPalabraMasFrecuente(nombre_archivo_input: str):
    archivo_input = open(nombre_archivo_input,'r')
    lista_palabras = []
    apariciones = []
    texto_formateado = []

    diccionario = {}

    for line in archivo_input.readlines():
        
        lista_palabras += line.split()
    
    # este for me formatea las palabras que esan en lista_palabras, quita las mayusculas, '.' etc etc
    for word in lista_palabras:
        
        word = word.lower()
        word = word.replace('.','')
        word = word.replace(',','')
        texto_formateado.append(word)
        
    for word in texto_formateado:
        
        if word in diccionario:
            diccionario[word] += 1
        else:
            diccionario[word] = 1

    for word in diccionario:
        apariciones.append(diccionario[word])
    cantidad_maxima_de_apariciones = max(apariciones)
    
    for word in diccionario:
        if diccionario[word] == cantidad_maxima_de_apariciones:
            return word
   
print(laPalabraMasFrecuente('archivo_palabras.txt'))


    
