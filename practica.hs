sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

longitud :: [Int] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)

invertir :: (a,b) -> (b,a)
invertir (a,b) = (b,a)

-- problema sumaUltimosDosDigitos (x: Z) : Z {
-- requiere: {True}
-- asegura: {res = (x mod 10) + ((x/10) mod 10)}

sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x = (mod x 10) + (mod (div x 10) 10)

sumaDigitos :: Int -> Int
sumaDigitos 0 = 0
sumaDigitos x = (mod x 10) + sumaDigitos (div x 10)

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece n [] = False
pertenece n (x:xs) = n == x || pertenece n xs

quitarRepetidos :: (Eq t) => [t] -> [t]
quitarRepetidos [] = []
quitarRepetidos (x:xs) | pertenece x xs = quitarRepetidos xs
                       | otherwise = x : quitarRepetidos xs

reverso :: (Eq t) => [t] -> [t]
reverso (x:xs) | xs == [] = [x]
               | otherwise = reverso xs ++ [x]

-- pares :: [Integer] -> [Integer] seg´un la siguiente especificaci´on:
-- problema pares (s: seq〈Z〉) : seq〈Z〉 {
-- requiere: { T rue }
-- asegura: {resultado s´olo tiene los elementos pares de s en el orden dado, respetando las repeticiones}

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs

-- mismosElementos :: (Eq t) => [t] -> [t] -> Bool, que dadas dos listas devuelve verdadero s´ı y solamente s´ı
-- ambas listas contienen los mismos elementos, sin tener en cuenta repeticiones, es deci

esta_incluido :: (Eq t) => [t] -> [t] -> Bool
esta_incluido [] _ = True
esta_incluido (x:xs) l | pertenece x l = esta_incluido xs l
                       | otherwise = False

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos a b = (esta_incluido a b) && (esta_incluido b a)

quitar :: (Eq t) => t -> [t] -> [t]
quitar n (x:xs) | n == x = xs
                | not (pertenece n (x:xs)) = (x:xs)
                | otherwise = x : quitar n xs

-- quitarRepetidos :: (Eq t) => [t] -> [t]
-- quitarRepetidos [] = []
-- quitarRepetidos (x:xs) | pertenece x xs = quitarRepetidos xs
--                        | otherwise = x : quitarRepetidos xs


quitarRepetidos' :: (Eq t) => [t] -> [t]
quitarRepetidos' [] = []
quitarRepetidos' (x:xs) | pertenece x xs = quitar x xs
                        | otherwise = x : quitarRepetidos' xs

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos n [] = []
quitarTodos n (x:xs) | n == x = quitarTodos n xs
                     | otherwise = x : quitarTodos n xs

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n (x:xs) = (x + n) : (sumarN n xs)

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar (x:xs) = minimum (x:xs) : ordenar (quitarTodos (minimum (x:xs)) (x:xs))
