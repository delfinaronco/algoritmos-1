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
-- 1)
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:[]) = [x]
sacarBlancosRepetidos (x:y:xs)  | x == ' ' && y == ' ' = sacarBlancosRepetidos (y:xs)
                                | otherwise = x:sacarBlancosRepetidos (y:xs)

-- 2)
contarPalabras :: [Char] -> Int
contarPalabras xs = contarEspacios (sacarEspaciosIniFin (sacarBlancosRepetidos xs)) + 1

sacarEspaciosIniFin :: [Char] -> [Char]
sacarEspaciosIniFin [] = []
sacarEspaciosIniFin (x:xs) | x ==' ' = sacarEspacioFin xs
                           | otherwise = x:(sacarEspacioFin xs) 

sacarEspacioFin :: [Char] -> [Char]
sacarEspacioFin [] = []
sacarEspacioFin (x:[]) | x==' ' = []
                       | otherwise = [x] 
sacarEspacioFin (x:xs) = x:(sacarEspacioFin xs)

contarEspacios :: [Char] -> Int
contarEspacios [] = 0
contarEspacios (x:xs) | x==' '= 1 + contarEspacios xs
                      | otherwise = contarEspacios xs

-- 3)
palabras :: [Char] -> [[Char]]
palabras xs = palabrasAux (sacarEspaciosIniFin (sacarBlancosRepetidos xs))

palabrasAux :: [Char] -> [[Char]] -- hace lo mismo que hace palabras pero se rompe cuando le mandas espacios de más
palabrasAux [] = []
palabrasAux (x:xs) = primeraPalabra (x:xs):(palabrasAux (sacarPrimeraPalabra (x:xs)))

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | x == ' ' = []
                      | otherwise = x:(primeraPalabra xs)                     

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (x:xs) | x == ' ' = xs
                           | otherwise = sacarPrimeraPalabra xs 

-- 4)
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga xs = palabraMasLargaAux (sacarEspaciosIniFin (sacarBlancosRepetidos xs))

palabraMasLargaAux :: [Char] -> [Char]
palabraMasLargaAux xs | sacarPrimeraPalabra xs == [] = primeraPalabra xs
                      | length (primeraPalabra xs) > length (palabraMasLargaAux (sacarPrimeraPalabra xs)) = primeraPalabra xs
                      | otherwise = palabraMasLargaAux (sacarPrimeraPalabra xs) 

-- 5)
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (xs:xss) = xs ++ (aplanar xss)

-- 6)
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (xs:[]) = xs ++ []
aplanarConBlancos (xs:xss) = (xs ++ " ") ++ aplanarConBlancos xss

-- 7)
nBlancos :: Integer -> [Char]
nBlancos 0 = []
nBlancos n = " " ++ nBlancos (n-1)

aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] n = []
aplanarConNBlancos (xs:[]) n = xs ++ []
aplanarConNBlancos (xs:xss) n = (xs ++ nBlancos n) ++ aplanarConNBlancos xss n

