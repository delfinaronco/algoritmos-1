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
