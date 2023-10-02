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

# imprimir_saludo("delfina")

# 2) 
def raiz_cuadrada_de (n:int):
	return math.sqrt(n)

# print(raiz_cuadrada_de(49))

# 3) 
def farenheit_a_celsius (t:float) -> float:
    res = round (((t - 32) * 5)/9)
    print(res)

# farenheit_a_celsius(75)

# 4)
def imprimir_dos_veces(e:str) -> str:
	print(e)
	print(e)

# imprimir_dos_veces("my name's Blurryface and I care what you think")

# 5)
def es_multiplo_de (n:int, m:int) -> bool:
	return n % m == 0

# 6) 
def es_par(n:int) -> bool:
	if es_multiplo_de(n,2):
		return True
	else: 
		return False

# print(es_par(4))

# 7)
def cantidad_de_pizzas(comensales:int,min_cant_porciones:int) -> int:
	if (comensales * min_cant_porciones) <= 8: 
		return 1
	else:
		return (((comensales * min_cant_porciones) // 8) + 1)

# print (cantidad_de_pizzas(2,8))


# Ejercicio 3

# 3)
def es_nombre_largo (s:str) -> bool:
	return len (s) >= 3 and len (s) <= 8

"""
print (es_nombre_largo ("ab"))
print (es_nombre_largo ("sdgfysgv"))

"""

# Ejercicio 5

# 1)
def devolver_el_doble_si_es_par (n:int) -> int:
	if es_multiplo_de (n,2):
		res = 2 * n
	else: 
		res = n 

	return res  

"""
print (devolver_el_doble_si_es_par(5))
print (devolver_el_doble_si_es_par(4))

"""

# Ejercicio 6

# 2)
def imprime_pares_10_40():
	n: int = 10
	while n <= 40:
		print(n)
		n = n + 2


def imprime_pares_10_40_for():   # hace lo mismo que el anterior
	for n in range(10,42,2):
		print(n)

# 4)
# varias maneras

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
