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



















