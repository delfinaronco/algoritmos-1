# 1) Intercalar [2 puntos]
# A la hora de jugar juegos de cartas, como el truco, el tute, o el chinchón, es importante que la distribución de las mismas en el mano sea aleatoria. Para esto, al comienzo de cada mano, antes de repartir las mismas se realizan mezclan sucesivas. Una técnica de mezclado es la denominada "mezcla americana" que consiste en separar el mazo en (aproximadamente) dos mitades e intercalar las cartas de ambas mitades. Implementar la función intercalar que dadas dos listas s1 y s2 con igual cantidad de elementos devuelva una lista con los elementos intercalados. Esto es, las posiciones pares de res tendrán los elementos de s1 y las posiciones impares los elementos de s2, respetando el orden original.

# problema intercalar (in s1: seq⟨Z⟩, in s2: seq⟨Z⟩) : seq⟨Z⟩ {
#   requiere: {|s1| = |s2| }
#   asegura: {|res| = 2 * |s1|}
#   asegura: {res[2*i] = s1[i] y res[2*i+1] = s2[i], para i entre 0 y |s1|-1}
# }

# TIP: realizar la iteración mediante índices y no mediante elementos

# Por ejemplo, dadas
s1 = [1, 3, 0, 1]
s2 = [4, 0, 2, 3]
# se debería devolver res = [1, 4, 3, 0, 0, 2, 1, 3]



def intercalar (s1: list, s2: list) -> list:

    s: list = s1 + s2
    res: list = []

    for i in range(len(s)):
        if i % 2 == 0:
            res.append(s1[0])
            s1.remove(s1[0])
        else:
            res.append(s2[0])
            s2.remove(s2[0])

    return res

# print(intercalar(s1,s2))

# 2) Posición de n-ésima aparición [2 puntos]

# Guido y Marcela son dos estudiantes de IP, nervioses con el parcial de Python. Con el objetivo de tener un rato antes del parcial para preguntarse 
# algunas dudas deciden encontrarse en el colectivo y viajar juntes. Para poder coordinar de forma exacta en qué colectivo se tienen que subir,
# Marcela usa sus habilidades de programación aprendidas en IP para acceder de forma poco legítima a la base de datos de colectivos de todas 
# las empresas. Con esto, arma una lista de todos los colectivos que van a pasar por la parada de Guido alrededor del horario acordado
# y le indica a Guido que se tiene que subir en el 3er colectivo de la línea 34. Por desgracia, Guido se olvida sus lentes antes de salir y no 
# es capaz de distinguir a qué línea pertenece cada colectivo que llega a la parada. Por lo que solo puede contar cantidad total de colectivos que pasan.

# Implementar la función pos_nesima_aparicion que dada una secuencia de enteros s, y dos enteros n y elem devuelve la posición en la cual elem 
# aparece por n-ésima vez en s. En caso de que elem aparezca menos de n veces en s, devolver -1.

# problema pos_nesima_aparicion (in s: seq⟨Z⟩, in n: Z, in elem: Z) : Z {
#   requiere: {n>0}
#   asegura: {Si el elemento aparece menos de n veces en la secuencia, res= -1 }
#   asegura: {Si el elemento aparece al menos n veces en la secuencia, s[res] = elem }
#   asegura: {Si el elemento aparece al menos n veces en la secuencia, elem aparece n-1 veces en s entre las posiciones 0 y res-1 }
# }

# Por ejemplo, dadas
s = [-1, 1, 1, 5, -7, 1, 3]
n = 2
elem = 1

# se debería devolver res = 2

s2 = [4,2,7,5,0,1,2]
n2 = 3
elem2 = 2

def pos_nesima_aparicion (s: list, n: int, elem: int) -> int:

    contador: int = 0

    for i in range(len(s)):
        if s[i] == elem:
            contador += 1

        if contador >= n:
            return i
        
    return -1       

# print(pos_nesima_aparicion(s2,n2,elem2))

# 3) Matriz espejada [3 puntos]
# Implementar la función matriz_espejada que dada una matriz devuelve True si cada una de sus filas es capicúa. Es decir, si cada fila
# es igual leída de izquierda a derecha o de derecha a izquierda. Definimos a una secuencia de secuencias como matriz si todos los elementos
# de la primera secuencia tienen la misma longitud.

# problema matriz_espejada(in m:seq⟨seq⟨Z⟩⟩ ) : Bool {
#   requiere: {todos los elementos de m tienen igual longitud (los elementos de m son secuencias)}
#   asegura: {(res = true) <=> todos los elementos de m son capicúa}
# }

# Por ejemplo, dada la matriz
m = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
# se debería devolver res = true 

def es_capicua (l: list) -> bool:

    l_al_reves: list = []

    for i in range(len(l)-1,-1,-1):
        l_al_reves.append(l[i])

    return l == l_al_reves

# print(es_capicua([2,1,2,1,2]))

def matriz_espejada (m: list) -> bool:

    for fila in m:
        if not(es_capicua(fila)):
            return False
        
    return True

# print(matriz_espejada([[1,2,2,1],[0,1,1,0],[3,1,1,3]]))

# 4) En el hipódromo: posiciones de los caballos [3 puntos]

# Además de recitales de artistas de renombre internacional (ej: Bizarrap), en el hipódromo de Palermo se realizan cotidianamente carreras de caballos. 
# Por ejemplo, durante el mes de Octubre se corrieron 10 carreras. En cada una de ellas participaron alrededor de 10 caballos.

# Implementar la función cuenta_posiciones_por_caballo que dada la lista de caballos que corrieron las carreras, y el diccionario que tiene los 
# resultados del hipódromo en el formato carreras:posiciones_caballos, donde carreras es un String y posiciones_caballos es una lista de strings 
# con los nombres de los caballos, genere un diccionario de caballos:#posiciones, que para cada caballo devuelva la lista de cuántas veces salió 
# en esa posición.
# Tip: para crear una lista con tantos ceros como caballos se puede utilizar la siguiente sintaxis lista_ceros = [0]*len(caballos)

# problema cuenta_posiciones_por_caballo(in caballos: seq⟨String⟩, in carreras: dict⟨String,seq⟨String⟩⟩: dict⟨String,seq⟨Z⟩⟩ {
#   requiere: {caballos no tiene repetidos}
#   requiere: {Los valores del diccionario carreras son permutaciones de la lista caballos (es decir, tienen exactamente los mismos elementos que 
# caballos, en cualquier orden posible)}
#   asegura: {res tiene como claves los elementos de caballos}
#   asegura: {El valor en res de un caballo es una lista que indica en la posición i cuántas veces salió ese caballo en la i-ésima posición.}
# }

# Por ejemplo, dados
caballos= ["linda", "petisa", "mister", "luck" ]
carreras= {"carrera1":["linda", "petisa", "mister", "luck"], "carrera2":["petisa", "mister", "linda", "luck"]}
# se debería devolver res = {"petisa": [1,1,0,0],
#                                           "mister": [0,1,1,0],
#                                           "linda": [1,0,1,0],
#                                           "luck": [0,0,0,2]}

def posicion (caballo: str, lista: list):

    for i in range(len(lista)):
        if lista[i] == caballo:
            return i

# print(posicion('mister',['linda','petisa','mister','luck']))

def cuenta_posiciones_por_caballo (caballos: list, carreras: dict) -> dict:

    res: dict = {}

    for caballo in caballos:
        res[caballo] = [0]*len(caballos)

    for carrera in carreras:
        for caballo in carreras[carrera]:
            if caballo in carreras[carrera]:
                pos = posicion (caballo,carreras[carrera])
                res[caballo][pos] += 1

    return res

# print(cuenta_posiciones_por_caballo(caballos,carreras))
 
# Ejercicio 1:
# Dada una matriz M de n x n números naturales,
# devolver una lista con las tuplas que indican los índices de las posiciones que
# tienen el valor más bajo en su columna.

# Problema posiciones_chiquita (in M: seq<seq<int>>) out: <(int,int)>
# requiere: M tiene n filas de n posiciones cada una
# asegura: cada tupla en res es una coordenada en M (los valores están entre 0 y n)
# asegura: El valor de M indexado en cada tupla de res es menor que el valor de M indexado en cualquier otro elemento de la misma columna

# def posiciones_chiquita (M: list) -> list:


# print(posiciones_chiquita([[1,2,3],[5,4,2],[9,1,7]]))

def posiciones_chiquita(M: list) -> list:

    n = len(M)
    res = []

    # Iterar sobre cada columna
    for j in range(n):
        # Encontrar el valor mínimo en la columna
        min_valor = M[0][j]

        for i in range(1, n):
            if M[i][j] < min_valor:
                min_valor = M[i][j]

        # Buscar las posiciones con el valor mínimo en la columna
        for i in range(n):
            if M[i][j] == min_valor:
                res.append((i, j))

    return res

# Ejemplo de uso
matriz_ejemplo = [
    [1, 2, 3],
    [5, 4, 2],
    [9, 1, 7]
]

# print(posiciones_chiquita(matriz_ejemplo))

# Ejercicio 2:

# Dado un diccionario del español, devolver un diccionario que tiene una única definición
# para cada palabra. La definición tiene que ser la más larga de todas las que había en el diccionario original.

# Problema diccionario_no_ambiguo (in D: dict<String,seq<String>>) out: dict<String, String>

# requiere: True
# asegura: las claves de res son exactamente las mismas que las de D
# asegura: para una clave c, el valor de c en res es un elemento de la lista que es el valor de c en D.
# asegura: para una clave c, no hay un string en la lista que es el valor de c en D que sea mas largo que el valor de c en res.


def texto_mas_largo (textos: list) -> str:
    longitud_textos: list = []

    for texto in textos:
        longitud_textos.append(len(texto))

    for texto in textos:
        if len(texto) == max(longitud_textos):
            return texto

# print(texto_mas_largo(['hola','hola que onda','hola gente que onda']))

D = {'casa':['lugar donde vive la gente','vivienda'],
     'boludo':['tonto','persona con poca capacidad mental']}

def diccionario_no_ambiguo (D: dict) -> dict:

    res: dict = {}

    for palabra in D:
        res[palabra] = texto_mas_largo(D[palabra])

    return res

# print(diccionario_no_ambiguo(D))
