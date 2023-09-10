--Ejercicio 1
fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = (fibonacci (n-1))+(fibonacci (n-2))

--Ejercicio 2
parteEntera :: Float -> Integer
parteEntera x | x < 1 && x >= 0 = 0
              | x > -1 && x <= 0 = -1
              | x >= 1 = 1 + parteEntera (x-1)
              | otherwise = (-1) + parteEntera (x+1)

--Ejercicio 3
esDivisible :: Integer -> Integer -> Bool
esDivisible _ 0 = False
esDivisible _ 1 = True
esDivisible 0 _ = True
esDivisible a b | b > a = False
esDivisible a b | a < 0 = False
esDivisible a b | otherwise = esDivisible (a-b) b 

--Ejercicio 4
sumaImpares :: Integer -> Integer
sumaImpares n = n^2

--con recursión
sumaImpares1 :: Integer -> Integer 
sumaImpares1 0 = 0
sumaImpares1 1 = 1
sumaImpares1 n = 2*n-1 + sumaImpares(n-1)

--Ejercicio 5
medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n*medioFact(n-2)

--Ejercicio 6
sumaDigitos :: Integer -> Integer
sumaDigitos 0 = 0
sumaDigitos n = mod n 10 + sumaDigitos (div n 10)

--Ejercicio 7
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n == mod n 10 = True
                      | mod (div n 10) 10 /= mod n 10 = False
                      | otherwise = todosDigitosIguales (div n 10)

--Ejercicio 8
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n (10^(cantDigitos n - i))) 10

cantDigitos :: Integer -> Integer
cantDigitos x | x == 0 = 0
              | otherwise = 1 + cantDigitos (div x 10)

--Ejercicio 9
esCapicua :: Integer -> Bool
esCapicua n | n <= 9 = True
            | otherwise = (esCapicuaAux n) && esCapicua (div (n - (iesimoDigito n (cantDigitos 1))*10^((cantDigitos n)-1)) 10)

esCapicuaAux :: Integer -> Bool
esCapicuaAux n = iesimoDigito n (cantDigitos n) == iesimoDigito n (cantDigitos 1)

--Ejercicio 10
--a)
f1 :: Int -> Int
f1 0 = 1
f1 n = 2^n + f1 (n-1)

--b)
f2 :: Int -> Float -> Float
f2 0 q = 0
f2 n q = q^n + f2 (n-1) q
       
--c) 
f3 :: Int -> Float -> Float
f3 0 q = 0
f3 n q = (f3 (n-1) q) + q^(2*n-1) + q^(2*n)

-- o sin recursión
f3' :: Int -> Float -> Float
f3' n q = f2 (2*n) q

--d)
f4 :: Int -> Float -> Float
f4 0 q = 1
f4 n q = q^(2*n-1) + q^(2*n) - q^(n-1) + (f4 (n-1) q)

-- sin recursión
f4' :: Int -> Float -> Float
f4' n q = (f3 n q) - (f2 (n-1) q)

--Ejercicio 11
--a)
fact :: Int -> Int
fact 1 = 1
fact n = n*(fact(n-1))

eAprox :: Int -> Float
eAprox 0 = 1
eAprox n = (eAprox (n-1)) + 1 / (fromIntegral (fact n))

--b)
e :: Float
e = eAprox 10

