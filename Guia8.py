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

# Ejercicio 7

def promedio_estudiante (legajo: str) -> float:

    archivo_legajo: str = open('legajo.csv','r')
    datos: list = []
    datos_alumno: list = []
    notas_del_alumno: list = []
    notas_del_alumno_formateada: list = []
    notas_del_alumno_formateada_float: list = []

    suma_notas: float = 0

    for line in archivo_legajo.readlines():
        datos.append(line)
    
    for notas in datos:
        datos_alumno.append(notas.split(','))

    for i in range(len(datos_alumno)):
        notas_del_alumno.append(datos_alumno[i][-1])

    for i in range(len(notas_del_alumno)):
        notas_del_alumno_formateada.append(notas_del_alumno[i].strip('\n'))

    for notas in notas_del_alumno_formateada:
        notas_del_alumno_formateada_float.append(float(notas))

    for notas in notas_del_alumno_formateada_float:
        suma_notas += notas 

    promedio = suma_notas/len(notas_del_alumno_formateada_float)

    return promedio

# print(promedio_estudiante('legajo.csv'))

# PILAS
from queue import LifoQueue as Pila
import poplib
import random

# Ejercicio 8

def generar_nros_al_azar (n: int, desde: int, hasta: int) -> Pila:
    nros = Pila()

    for i in range (n):
        nros.put(random.randint(desde,hasta))

    print(list(nros.queue))

# generar_nros_al_azar(5,1,10)

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

# Ejercicio 11

def esta_bien_balanceada(s: str) -> bool:
    
    parentesis: list = []
    parentesis_de_apertura: list = []
    parentesis_de_cierre: list = []
    
    for i in s:
        if i == '(' or i == ')':
            parentesis.append(i)

    if  not (parentesis[0] == '('and len(parentesis)%2 == 0):
        return False
    
    for i in parentesis:
        if i == '(':
            parentesis_de_apertura.append(i)
        else:
            parentesis_de_cierre.append(i)    

    return len(parentesis_de_apertura) == len(parentesis_de_cierre)    

# print(esta_bien_balanceada('(2+(2*3)-(15/5)'))

# COLAS
from queue import Queue as Cola

# Ejercicio 13

def generar_nros_al_azar_colas (n: int, desde: int, hasta: int):
    cola: Cola = Cola()

    for i in range(n):
        cola.put(random.randint(desde,hasta))
    
    print(list(cola.queue))

# generar_nros_al_azar_colas(5,1,10)

# Ejercicio 14

c = Cola()

c.put(1)
c.put(5)
c.put(3)

def cantidad_elementos_cola (c: Cola) -> int:
    elementos: list = []
    contador: int = 0
    
    while not c.empty():
        elementos.append(c.get())
        contador += 1

# reconstruccion de la cola
    print(elementos)
    for i in range(len(elementos)):
        c.put(elementos[i])

    return contador

# print(cantidad_elementos_cola(c))

# Ejercicio 15

def buscar_el_maximo_cola (c: Cola) -> int:
    elementos: list = []

    while not c.empty():
        elementos.append(c.get())

    print(elementos)  

    for i in range(len(elementos)):
        c.put(elementos[i])

    return max(elementos)

# print(buscar_el_maximo_cola(c))

# Ejercicio 17

pacientes = Cola()

pacientes.put((1,'Maria','cirugia'))
pacientes.put((5,'Nicolas','oftalmologia'))
pacientes.put((2,'Lucia','dermatologia'))
pacientes.put((8,"Lucas","pediatria"))

def n_pacientes_urgentes (pacientes: Cola) -> int:
    lista_pacientes: list = []
    contador: int = 0

    while not pacientes.empty():
        lista_pacientes.append(pacientes.get())

    for i in range(len(lista_pacientes)):
        if lista_pacientes[i][0] <= 3:
            contador += 1

    # para reconstruir la cola
    for i in range(len(lista_pacientes)):
        pacientes.put(lista_pacientes[i])
    
    # print(list(pacientes.queue))

    return contador
    
# print(n_pacientes_urgentes(pacientes))

# Ejercicio 18

clientes_cola = Cola()
clientes_cola.put(('n',1, True, False))
clientes_cola.put(('e',9, False, False))
clientes_cola.put(('q',87, False, False))
clientes_cola.put(('hu',23, True, True))
clientes_cola.put(('j',7, True, False))
clientes_cola.put(('a',4, False, False))
clientes_cola.put(('x',2, True, True))

def promedio_estudiante(legajo: str) -> float:
    
    file_notas_alumnos: str = open('notas.csv', 'r')
    datos_alumnos: list = []
    notas_de_todos_alumnos: list = []
    notas_del_alumno: list = []
    notas_del_alumno_formateada: list = []
    notas_del_alumno_formateada_float: list = []
    
    suma_notas: float = 0
    
 
    for line in file_notas_alumnos.readlines():
     
        datos_alumnos.append(line)  
           
    for notas in datos_alumnos:
        notas_de_todos_alumnos.append(notas.split(','))
     
    for i in range(len(notas_de_todos_alumnos)):
            
        if f"'{legajo}'"== notas_de_todos_alumnos[i][0]:
            notas_del_alumno.append(notas_de_todos_alumnos[i][-1])

    for i in range(len(notas_del_alumno)):
        
        notas_del_alumno_formateada.append(notas_del_alumno[i].strip('\n'))

    for notas in notas_del_alumno_formateada:
        notas_del_alumno_formateada_float.append(float(notas))
        
    for notas in notas_del_alumno_formateada_float:
        sumar_notas += 0

    promedio = sumar_notas/len(notas_del_alumno_formateada_float)

    return promedio
   

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

