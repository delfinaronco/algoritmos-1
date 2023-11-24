-- Ej 1

segundosElementos :: [(String,String)] -> [String]
segundosElementos [] = []
segundosElementos ((a,b):xs) = sacarRepetidos (b : segundosElementos xs)

sacarRepetidos :: (Eq t) => [t] -> [t]
sacarRepetidos [] = []
sacarRepetidos (x:xs) | elem x xs = sacarRepetidos xs
                      | otherwise = x : sacarRepetidos xs
           
edad :: String -> [(String,Int)] -> Int
edad nombre [] = 0
edad nombre ((a,b):xs) | nombre == a = b
                       | otherwise = edad nombre xs 

-- Ej 2

menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde a n | mod n a == 0 = a 
                      | otherwise = menorDivisorDesde (a+1) n

menorDivisor :: Int -> Int
menorDivisor n = menorDivisorDesde 2 n

esPrimo :: Int -> Bool
esPrimo n = menorDivisor n == n

-- Ej 3

descomponerEnPrimos :: Int -> [Int]
descomponerEnPrimos n | esPrimo n = [n]
                      | otherwise = (menorDivisor n) : descomponerEnPrimos ((div n (menorDivisor n)))

cuentaRepeticiones :: Int -> [Int] -> Int
cuentaRepeticiones n [] = 0
cuentaRepeticiones n (x:xs) | n == x = 1 + cuentaRepeticiones n xs
                            | otherwise = cuentaRepeticiones n xs

pasarATuplas :: [Int] -> [(Int,Int)]
pasarATuplas [] = []
pasarATuplas (x:xs) = (x,cuentaRepeticiones x (x:xs)) : (pasarATuplas (quitar x xs))

quitar :: Int -> [Int] -> [Int]
quitar n [] = []
quitar n (x:xs) | n == x = quitar n xs
                | otherwise = x : quitar n xs

descomponerEnPrimosPotencias :: Int -> [(Int,Int)] 
descomponerEnPrimosPotencias n = pasarATuplas (descomponerEnPrimos n)
