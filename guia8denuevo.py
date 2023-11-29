def contar_lineas (nombre_archivo: str) -> int:
    archivo: str = open(nombre_archivo,'r')
    lineas: list = []

    for line in archivo.readlines():
        lineas.append(line)

    return len(lineas)

# print(contar_lineas('archivo_palabras.txt'))

def existe_palabra (palabra: str, nombre_archivo: str) -> bool:

    archivo: str = open(nombre_archivo,'r')
    palabras: list = []

    for line in archivo.readlines():
        palabras += line.split()

    if palabra in palabras:
        return True
    else:
        return False 

# print(existe_palabra("hola",'archivo_palabras.txt'))

def cantidad_apariciones (nombre_archivo: str, palabra: str) -> int:

    archivo: str = open (nombre_archivo,'r')
    palabras: list = []
    contador: int = 0

    for line in archivo.readlines():
        palabras += line.split()

    for i in palabras:
        if i == palabra:
            contador += 1

    return contador

# print(cantidad_apariciones('archivo_palabras.txt',"prueba"))

def reverso (nombre_archivo_input: str):

    archivo_input: str = open (nombre_archivo_input,'r')
    nombre_archivo_output: str = 'reverso.txt'
    archivo_output: str = open (nombre_archivo_output,'w')

    lineas: list = []

    for line in archivo_input.readlines():
        lineas.append(line)

    lineas.reverse()

    for line in lineas:
        archivo_output.write(f"{line}\n")

# reverso('archivo_palabras.txt')

# PILAS

from queue import LifoQueue as Pila
import random

def generar_nros_al_azar (n: int, desde: int, hasta: int) -> Pila:

    nros = Pila()

    for i in range(n):
        nros.put(random.randint(desde,hasta))

    print(list(nros.queue))

# generar_nros_al_azar(5,1,10)

p = Pila()
p.put(1)
p.put(2)
p.put(3)
p.put(4)
p.put(5)

def copiar(p: Pila) -> Pila:

    elements:[int] = []

    while not p.empty():
        elements.append(p.get())

    p_copy: Pila = Pila()

    for i in range(len(elements)-1,0-1,-1):
        p.put(elements[i])
        p_copy.put(elements[i])

    return p_copy

# print(list(copiar(p).queue))

def cantidad_elementos (p: Pila) -> int:

    contador = 0

    while not p.empty():
        elemento = p.get()
        contador += 1

    return contador

# print(cantidad_elementos(copiar(p)))

def buscar_el_maximo (p: Pila) -> int:

    p_copy: Pila = copiar(p)
    value = p_copy.get()

    while not p_copy.empty():
        next_value = p_copy.get()
        value = max (next_value, value)

    return value

# print(buscar_el_maximo(p))

def esta_bien_balanceada (s: str) -> bool:

    parentesis: list = []
    parentesis_de_apertura: list = []
    parentesis_de_cierre: list = []

    for i in s:
        if i == "(" or i == ")":
            parentesis.append(i)

    if not ((parentesis[0] == "(") and (len(parentesis) % 2 == 0)):
            return False

    for i in parentesis:
        if i == "(":
            parentesis_de_apertura.append(i)
        elif i == ")":
            parentesis_de_cierre.append(i)

    return len(parentesis_de_apertura) == len(parentesis_de_cierre)

# print(esta_bien_balanceada("(1+2*5"))

# COLAS

from queue import Queue as Cola

c = Cola()

c.put(1)
c.put(5)
c.put(3)
c.put(9)

def cantidad_elementos_cola (c: Cola) -> int:
    elementos: list = []
    contador: int = 0

    while not c.empty():
        elementos.append(c.get())
        contador += 1

    # reconstruimos la cola

    for i in elementos:
        c.put(i)

    return contador

# print(cantidad_elementos_cola(c))


def maximo (l: list) -> int:

    max_value = l[0]

    for i in l:
        if i > max_value:
            max_value = i
        
    return max_value

# print(maximo([1,2,6,5]))

def buscar_el_maximo_cola (c: Cola) -> int:
    elementos: list = []
    
    while not c.empty():
        elementos.append(c.get())

    return maximo(elementos)

# print(buscar_el_maximo_cola(c))

def armar_secuencia_de_bingo () -> Cola[int]:

    l: int = []

    for i in range(0,99+1,1):
        l.append(i)

    random.shuffle(l)

    result: Cola[int] = Cola()

    for elem in l:
        result.put(elem)

    return result

bolillero = armar_secuencia_de_bingo()
# print(bolillero.get())

def jugar_carton_de_bingo (carton: list[int], bolillero: Cola[int]) -> int:
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

carton = [25,50,32,10,23,80,71,99,5,65,48,19]

# print(jugar_carton_de_bingo(carton,bolillero))

pacientes = Cola()

pacientes.put((2,'Delfina','oculista'))
pacientes.put((5,'Nahuel','dentista'))
pacientes.put((1,'Franco','traumatologo'))
pacientes.put((8,'Maria','dermatologo'))

def n_pacientes_urgentes (pacientes: Cola) -> int:
    lista_pacientes: list = []
    contador: int = 0

    while not pacientes.empty():
        lista_pacientes.append(pacientes.get())

    for i in range(len(lista_pacientes)):
        if lista_pacientes[i][0] <= 3:
            contador += 1

    # para reconstruir la cola

    for i in lista_pacientes:
        pacientes.put(i)

    return contador

# print(n_pacientes_urgentes(pacientes))

cola_de_ingreso = Cola()

cola_de_ingreso.put(("Delfina Ronco",43866161,False,False))
cola_de_ingreso.put(("Maria Suarez",29872343,True,False))
cola_de_ingreso.put(("Ramona Ojeda",21045121,True,True))
cola_de_ingreso.put(("Gabriel Esteban",23454212,False,True))

def a_clientes (cola_de_ingreso: Cola) -> Cola:

    cola_de_atencion = Cola()
    clientes: list = []
    clientes_con_prioridad: list = []
    clientes_con_cuenta: list = []
    clientes_sin_cuenta: list = []


    while not cola_de_ingreso.empty():
        clientes.append(cola_de_ingreso.get())

    for i in range(len(clientes)):

        if clientes[i][3] == True:
            clientes_con_prioridad.append(clientes[i])

        elif clientes[i][2] == True:
            clientes_con_cuenta.append(clientes[i])

        else:
            clientes_sin_cuenta.append(clientes[i])

    clientes = clientes_con_prioridad + clientes_con_cuenta + clientes_sin_cuenta

    for i in clientes:
        cola_de_atencion.put(i)

    print(list(cola_de_atencion.queue))

    return cola_de_atencion

# a_clientes(cola_de_ingreso)


        














    



