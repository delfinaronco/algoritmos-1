-- clase 6 - parte 2 (taller de álgebra)

primerMultiplode45345 :: [Int] -> Int
primerMultiplode45345 l | mod (head l) 45345 == 0 = (head l)
                        | otherwise = primerMultiplode45345 (tail l)
                        
pertenece1 :: Int -> [Int] -> Bool
pertenece1 x l | l == [] = False 
              | otherwise = (x == head l) || pertenece1 x (tail l)

pertenecePM :: Int -> [Int] -> Bool
pertenecePM x [] = False
pertenecePM x l = (x == head l) || pertenecePM x (tail l)


-- ahora empezamos con la guía
-- Ejercicio 1
-- 1)
longitud :: [t] -> Integer 
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- 2)
ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

-- 3)
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio (xs)

-- 4)
reverso :: (Eq t) => [t] -> [t]
reverso (x:xs) | xs == [] = [x]
               | otherwise = reverso xs ++ [x]

-- Ejercicio 2
-- 1)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece n [] = False
pertenece n (x:xs) = n == x || pertenece n xs

-- 2)
todosIguales:: (Eq t) => [t] -> Bool
todosIguales [x] = True
todosIguales (x:y:xs)   | x == y = todosIguales(y:xs)
                        | otherwise = False

-- 3)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs)   | pertenece x xs = False
                        | otherwise = todosDistintos xs
                        
-- 4)
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs

-- 5)
quitar :: (Eq t) => t -> [t] -> [t]
quitar n [] = []
quitar n (x:xs) | n == x = xs
                | otherwise = x:(quitar n xs)

-- 6)
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos n [] = []
quitarTodos n (x:xs) | n == x = quitarTodos n (xs)
                     | otherwise = x:(quitarTodos n xs)

-- 7)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | hayRepetidos (x:xs) = x:(eliminarRepetidos(quitarTodos x xs))
                         | otherwise = (x:xs)

-- 8)
mismosElementos:: (Eq t) => [t] -> [t] -> Bool
mismosElementos a b = (mismosElementos' a b) && (mismosElementos' b a)


mismosElementos':: (Eq t) => [t] -> [t] -> Bool
mismosElementos' [] _ = True
mismosElementos' (x:xs) ys  | pertenece x ys = mismosElementos' xs ys
                            | otherwise = False

-- 9) 
capicua :: (Eq t) => [t] -> Bool
capicua xs = xs == reverso (xs)

-- Ejercicio 3
-- 1)
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- 2)
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

-- 3)
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:y:ys) | x >= y = maximo (x:ys)
                | otherwise = maximo (y:ys)
-- 4)
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n (x:xs) = n + x : (sumarN n xs)

-- 5)
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- 6)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

-- 7)
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x:(pares xs)
             | otherwise = pares xs

-- 8)
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x:(multiplosDeN n (xs))
                      | otherwise = multiplosDeN n (xs)

-- 9)
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar (x:xs) = ordenar (quitar max (x:xs)) ++ [max]
                where max = maximo (x:xs)

-- Ejercicio 4


