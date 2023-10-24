
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

q = armarSecuenciaDeBingo()
# print(q.get())

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

print(jugarCartonDeBingo(carton,q))

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


    
