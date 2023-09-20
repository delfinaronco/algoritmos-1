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

--Ejercicio 12
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (sucesionA n) - 1

sucesionA :: Integer -> Float
sucesionA n | n == 1 = 2
            | otherwise = 2 + (1 / sucesionA (n-1))

--Ejercicio 13
f :: Int -> Int -> Int
f 0 m = 0
f n m = (f (n-1) m) + round (f2 m (fromIntegral n))

--Ejercicio 14
sumaPotencias :: Float -> Int -> Int -> Float
sumaPotencias q n 0 = 0
sumaPotencias q n m = (sumaPotencias q n (m-1)) + (q^m * (f2 n q))

--Ejercicio 15
sumaRacionales :: Int -> Int -> Float
sumaRacionales n 0 = 0
sumaRacionales n m = (sumaRacionales n (m-1)) + (fromIntegral (sumatoria n)) / (fromIntegral m)

sumatoria :: Int -> Int
sumatoria 0 = 0
sumatoria n = n + sumatoria (n-1)

--Ejercicio 16
--a)
menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer 
menorDivisorDesde n q | mod n q == 0 = q
                      | otherwise = menorDivisorDesde n (q+1)

--b)
esPrimo:: Integer-> Bool
esPrimo 1 = False
esPrimo n = menorDivisor n == n

--c)
sonCoprimos:: Integer -> Integer -> Bool
sonCoprimos _ 1 = True
sonCoprimos 1 _ = True
sonCoprimos a b | (a > b) && mod a (menorDivisor b) == 0 = False
                | (a > b) && mod a (menorDivisor b) /= 0 = sonCoprimos a (div b (menorDivisor b))
                | (b > a) && mod b (menorDivisor a) == 0 = False
                | (b > a) && mod b (menorDivisor a) /= 0 = sonCoprimos b (div a (menorDivisor a))

--d) 
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = minimoPrimoDesde (1 + nEsimoPrimo (n-1))

--Ejercicio 17
esFibonacci :: Integer -> Bool
esFibonacci n = esFibonacciAux n 0

esFibonacciAux :: Integer -> Integer -> Bool
esFibonacciAux n i | n == fibonacci i = True
                   | fibonacci i > n = False
                   | otherwise = esFibonacciAux n (i+1)

minimoPrimoDesde :: Integer -> Integer
minimoPrimoDesde n | esPrimo n = n
                   | otherwise = minimoPrimoDesde (n+1)

--Ejercicio 18
mayorDigitoPar :: Integer ->Integer
mayorDigitoPar n | n < 10 && par n = n
                 | n < 10 = -1
                 | par ultimoDigito = max ultimoDigito resultadoRecursion
                 | otherwise = resultadoRecursion
            where
                  ultimoDigito = mod n 10
                  par a = mod a 2 == 0
                  resultadoRecursion = mayorDigitoPar (div n 10)

--Ejercicio 19
esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSumaInicialDePrimosAux n 2

esSumaInicialDePrimosAux :: Integer -> Integer -> Bool
esSumaInicialDePrimosAux n q | n == sumaPrimosHasta 2 q = True
                             | n < sumaPrimosHasta 2 q = False
                             | otherwise = esSumaInicialDePrimosAux n (q+1)

sumaPrimosHasta :: Integer -> Integer -> Integer
sumaPrimosHasta m n  | esPrimo n && n == m = m
                     | n == m = 0
                     | esPrimo m = m + sumaPrimosHasta (m+1) n
                     | otherwise = sumaPrimosHasta (m+1) n

-- Ejercicio 20
sumaDivisoresDesde :: Integer -> Integer -> Integer
sumaDivisoresDesde n m | n == m = m
                       | n > m = 0
                       | n < m && mod m n == 0 = n + sumaDivisoresDesde (n+1) m
                       | otherwise = sumaDivisoresDesde (n+1) m

sumaDivisores :: Integer -> Integer
sumaDivisores m = sumaDivisoresDesde 1 m 

tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax n m     | (n == m) = sumaDivisores m
                     | otherwise = max (sumaDivisores m) (tomaValorMax (n+1) m)

