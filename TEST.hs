doubleMe:: Int -> Int
doubleMe x = x + x

-- Ejercicio 1
--a)
f:: Int -> Int
f n | n==1 = 8
    | n==4 = 131
    | n==16 = 16

 --b)   
g:: Int -> Int
g n | n==8 = 16
    | n==16 = 4
    | n==131 = 1

--c)
h:: Int -> Int
h n=f(g(n))

--Ejercicio 2
--a)
absoluto :: Int -> Int 
absoluto x | x >= 0 = x
           | otherwise = (-x)

--Ejercicio 3
estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b | a == 0 && b == 0 = False
                      | mod a b == 0 = True 
                      | otherwise = False
                      
--Ejercicio 4
--a)
prodInt :: (Float,Float) -> (Float,Float) -> Float
prodInt (a,b) (c,d) = a * c + b * d

--b)
todoMenor :: (Float,Float) -> (Float,Float) -> Bool
todoMenor (a,b) (c,d) | a < c && b < d = True
                      | otherwise = False

--c)
distanciaPuntos :: (Float,Float) -> (Float,Float) -> Float
distanciaPuntos (a,b) (c,d) = sqrt(((c-a)**2)+((d-b)**2))

--d)
sumaTerna :: (Int,Int,Int) -> Int
sumaTerna (a,b,c) = a + b + c

--e)
sumarSoloMultiplos :: (Int,Int,Int) -> Int -> Int
sumarSoloMultiplos (a,b,c) k | mod a k == 0 && mod b k == 0 && mod c k == 0 = a + b + c
                             | mod a k == 0 && mod b k == 0 = a + b 
                             | mod a k == 0 && mod c k == 0 = a + c
                             | mod b k == 0 && mod c k == 0 = b + c
                             | mod a k == 0 = a 
                             | mod b k == 0 = b 
                             | mod c k == 0 = c
                             | otherwise = 0

--f)
posPrimerPar :: (Int,Int,Int) -> Int
posPrimerPar (a,b,c) | mod a 2 == 0 = 0
                     | mod b 2 == 0 = 1
                     | mod c 2 == 0 = 2
                     | otherwise = 4

--g)
crearPar :: a -> b -> (a,b)
crearPar a b = (a,b)

--h)
invertir :: (a,b) -> (b,a)
invertir (a,b) = (b,a)

--Ejercicio 5
todosMenores :: (Int,Int,Int) -> Bool
todosMenores (a,b,c) | f5 a > g5 a && f5 b > g5 b && f5 c > g5 c = True
                     | otherwise = False

--funciones auxiliares
f5 :: Int -> Int
f5 x | x <= 7 = x^2
    | otherwise= (2^x)-1

g5 :: Int -> Int
g5 n = if mod n 2 == 0 then div n 2 else 3*n+1

--Ejercicio 6
bisiesto :: Int -> Bool
bisiesto a | (mod a 4 /= 0) || (mod a 100 == 0 && mod a 400 /= 0) = False
           | otherwise = True

--Ejercicio 7
distanciaManhattan :: (Float,Float,Float) -> (Float,Float,Float) -> Float
distanciaManhattan (a,b,c) (d,e,f) = abs((a-d)+(b-e)+(c-f))

--Ejercicio 8
comparar :: Int -> Int -> Int
comparar a b | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
             | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
             | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0
              where sumaUltimosDosDigitos x = mod x 10 + mod (div x 10) 10


 --b)
maximoabsoluto :: Int -> Int -> Int       
maximoabsoluto x y | (absoluto x) >= (absoluto y) = x
                   | otherwise = y

--c)
maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = y
              | otherwise =z

--d)
--sin usar pattern matching
algunoEsO :: Float -> Float -> Bool
algunoEsO x y | x==0 || y==0 = True
              | otherwise = False

--usando pattern matching
algunoEsOp :: Float -> Float -> Bool
algunoEs0p 0 y = True
algunoEsOp x 0 = True
algunoEsOp x y = False

--e)
--sin usar pattern matching
ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y | x==0 && y==0 = True
              | otherwise = False

--usando pattern matching
ambosSon0p :: Float -> Float -> Bool
ambosSon0p 0 0 = True
ambosSon0p x y = False

--f)
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | x <= 3 && y <= 3 = True
                   | (x > 3 && x < 7) && (y > 3 && y < 7) = True
                   | x > 7 && y > 7 = True
                   | otherwise = False

--g)
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | (x == y) && (x == z) = x
                    | x == y = x + z
                    | x == z = x + y
                    | otherwise = x + y + z

--h)
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y | mod x y == 0 = True
                 | otherwise = False

--i)
digitoUnidades :: Int -> Int
digitoUnidades x = mod x 10

--j)
digitoDecenas :: Int -> Int
digitoDecenas x = mod (div x 10) 10

--Ejercicio 3
estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b | a == 0 && b == 0 = False
                      | mod a b == 0 = True 
                      | otherwise = False

















