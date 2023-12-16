reproducciones = {"Arctic Monkeys":[("Too Much to Ask",10010),("The Bakery",800)],"Cage The Elephant":[("Telescope",1620),("The Unforgiven",589)],"AURORA":[("Exist for Love",331),("Everything Matters",2050)]}

# debería devolver {"Arctic Monkeys": 1810, "Cage The Elephant": 1209, "AURORA": 331}

reproduccioness = [("Too Much to Ask",1010),("The Bakery",800)]

def suma_reproducciones (reproduccioness: list) -> int:
    suma: int = 0

    for (cancion,numero) in reproduccioness:
        suma += numero

    return suma

# print(suma_reproducciones(reproduccioness))

def maximo (l: list) -> int:
    max = l[0]

    for i in range(len(l)):
        if l[i] >= max:
            max = l[i]

    return max

# print(maximo ([2,7,4,3]))

def artista_mas_escuchado (reproducciones: dict) -> str:

    reproducciones_por_artista: dict = {}
    numeros: list = []

    for artista,canciones in reproducciones.items():
        reproducciones_por_artista[artista] = suma_reproducciones(canciones)
        numeros.append(reproducciones_por_artista[artista])
    
    for artista,numero in reproducciones_por_artista.items():
        if maximo(numeros) == numero:
            return artista
    
         
# print(artista_mas_escuchado(reproducciones))

def colectivos_a_bondis (nombre_archivo_input: str):

    archivo_input = open(nombre_archivo_input,'r')
    archivo_output = open('bondis','w')
    palabras: list = []
    nuevo_texto: list = []

    for line in archivo_input.readlines():
        palabras += line.split()

    for palabra in palabras:

        palabra = palabra.replace('colectivo','bondi')
        palabra = palabra.replace('.','.\n')
        nuevo_texto.append(palabra)

    for word in nuevo_texto:
        if '.' in word:
            archivo_output.write(word)
        else:
            archivo_output.write(word + ' ')

    return archivo_output

# colectivos_a_bondis('colectivos.txt')
