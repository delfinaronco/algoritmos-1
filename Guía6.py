import math

# Ejercicio 1

# 1)
def imprimir_hola_mundo ():
	print ("Hola mundo")

# 2)
def imprimir_un_verso () -> str:
	print ("and i was running far awar,\nwould i run off the world someday")

# 3)
def raizDe2() -> float:
    return round (math.sqrt(2), 4)

# 4)
def factorial_de_dos() -> int:
	return math.factorial(2)

# 5)
def perimetro () -> float:
	return 2 * math.pi

# Ejercicio 2

# 1)

def imprimir_saludo (name:str) -> str:
	res: str = f"Hola {name}"
	print (res)

# 2) 
def raiz_cuadrada_de (n:int):
	return math.sqrt(n)

# 3) 
def farenheit_a_celsius (t:float) -> float:
    res = round (((t - 32) * 5)/9)
    print(res)

# 4)
def imprimir_dos_veces(e:str) -> str:
	print(e)
	print(e)

# 5)
def es_multiplo_de (n:int, m:int) -> bool:
	return n % m == 0

# 6) 
def es_par(n:int) -> bool:
	if es_multiplo_de(n,2):
		return True
	else: 
		return False

# 7)
def cantidad_de_pizzas(comensales:int, min_cant_porciones:int) -> int:
	if (comensales * min_cant_porciones) <= 8: 
		return 1
	else:
		return ((math.ceil((comensales * min_cant_porciones) // 8)) + 1)

# Ejercicio 3

# 1)
def alguno_es_0 (n1:float, n2:float) -> bool:
	return n1 == 0 or n2 == 0 

# 2)
def ambos_son_0 (n1:float, n2:float) -> bool:
	return n1 == 0 and n2 == 0

# 3)
def es_nombre_largo (s:str) -> bool:
	return len (s) >= 3 and len (s) <= 8

# 4)
def es_bisiesto (año: int) -> bool:
    return es_multiplo_de (año,4) and not (es_multiplo_de (año,100))

# Ejercicio 4

# 1)
def peso_pino (metros:int) -> int:
	if metros <= 3:
		return 3 * metros * 100
	else: 
		return 900 + (2 * (metros - 3) * 100)

# 2)
def es_peso_util (peso_pino) -> bool:
	return peso_pino >= 400 and peso_pino <= 1000

# 4)
def sirve_pino2 (metros: int) -> bool:
	return peso_pino (metros) >= 400 and peso_pino (metros) <= 1000

# Ejercicio 5

# 1)
def devolver_el_doble_si_es_par (n:int) -> int:
	if es_multiplo_de (n,2):
		res = 2 * n
	else: 
		res = n 

	return res  

# 2)
def devolver_valor_si_es_par_sino_el_que_sigue (n: int) -> int:
	if es_par (n): 
		res = n
	else: 
		res = n + 1
	return res

# 3) 
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (n: int) -> int:
	if es_multiplo_de (n,3) and not(es_multiplo_de (n,9)):
		res = n * 2
	elif es_multiplo_de (n,9):
		res = n * 3
	else: 
		res = n
	return res

# 4)
def lindo_nombre (nombre: str) -> str:
	if len (nombre) >= 5:
		print ("Tu nombre tiene muchas letras")
	else:
		print ("Tu nombre tiene menos de 5 caracteres")

# 5)
def el_rango (n: int) -> str:
	if n < 5:
		print ("Menor a 5")
	elif n >= 10 and n <= 20:
		print ("Entre 10 y 20")
	elif n > 20:
		print ("Mayor a 20")

# 6)
def vacaciones_o_trabajar (sexo: str, edad: int) -> str:
	if sexo == "F" and (edad < 18 or edad >= 60):
		print ("Andá de vacaciones")
	elif sexo == "F" and (edad >= 18 or edad < 60):
		print ("Te toca trabajar")
	elif sexo == "M" and (edad < 18 or edad >= 65):
		print ("Andá de vacaciones")
	elif sexo == "M" and (edad >= 18 or edad < 65):
		print ("Te toca trabajar") 
	
# Ejercicio 6/7

# 1)
def imprime_1_a_10 ():
	n: int = 1
	while n <= 10:
		print(n)
		n = n + 1

def imprime_1_a_10_for ():
	for n in range (1,11,1):
		print(n)

# 2)
def imprime_pares_10_40():
	n: int = 10
	while n <= 40:
		print(n)
		n = n + 2

def imprime_pares_10_40_for():  
	for n in range(10,42,2):
		print(n)

# 3)
def eco_10_veces():
	n = 1
	while n <= 10:
		print ("eco")
		n = n + 1
	
def eco_10_veces_for():
	n = 1
	for n in range(n,11):
		print("eco")

# 4)
def cuenta_regresiva(n:int):
	while n > 0:
		print (n)
		n = n - 1
	print ("Despegue")

def cuenta_regresiva_for(n:int):
	for i in range (0,n,1):
		print(n-i)
	print ("Despegue")

def cuenta_regresiva_for2(n:int):
	for i in range (n,0,-1):
		print(i)
	print ("Despegue")

# 5)
def viaje_en_el_tiempo(partida: int, llegada: int):
    while partida != llegada:
        partida = partida - 1
        print("Viajó un año al pasado, estamos en el año:", partida)

def viaje_en_el_tiempo_for (partida: int, llegada: int):
	for i in range (partida - 1, llegada - 1, -1):
		print ("Viajó un año al pasado, estamos en el año:",i)

# 6)
def viaje_aristoteles(año_partida: int)-> str:
        año_aristoteles = -384
        i = 20
        while año_partida > año_aristoteles:
            print(f"viajaste {i} años en el tiempo, estamos en el año {año_partida-20}")
            año_partida -= 20
            i += 20

def viaje_aristoteles_for (año_partida: int) -> str:
	año_aristoteles = -384
	for i in range (año_partida, año_aristoteles,-20):
		print (f"viajaste 20 años en el tiempo, estamos en el año {i}")
		
# Ejercicio 8
# 1)
x = 5
y = 7		
x = x + y

# 2)
x = 5
y = 7
z = x + y
y = z * 2

# 3)
x = 5
y = 7
x = "hora"
y = x * 2

# 4)
x = False
res = not(x)

# 5)
x = True
y = False
res = x and y
x =  res and x

# Ejercicio 9

def rt (x: int, g: int) -> int:
	g = g + 1
	return x + g

g: int = 0
def ro (x: int) -> int:
	global g
	g = g + 1
	return x + g

"""
 # 1) nos da 2 3 4

print (ro(1))
print (ro(1))
print (ro(1))

# 2) nos da 2 2 2
print (rt(1,0))
print (rt(1,0))
print (rt(1,0))
 """
