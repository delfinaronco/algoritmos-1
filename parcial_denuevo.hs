-- Ejercicio 2

perteneceTuplas :: (String,String) -> [(String,String)] -> Bool
perteneceTuplas (a,b) [] = False
perteneceTuplas (a,b) ((x,y):xs) | a == x || a == y || b == x || b == y = True
                                 | otherwise = perteneceTuplas (a,b) xs

formulasValidas :: [(String,String)] -> Bool
formulasValidas [] = True
formulasValidas ((presi,vice):xs) | presi /= vice && (not(perteneceTuplas (presi,vice) xs)) = formulasValidas xs
                                  | otherwise = False

-- Ejercicio 1

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

votosEnBlanco :: [(String,String)] -> [Int] -> Int -> Int
votosEnBlanco formulas votos cantTotalVotos = cantTotalVotos - (sumatoria votos)

-- Ejercicio 3

porcentajeDeVotos :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeVotos presidente formulas votos = (division (votosDelPresidente presidente formulas votos) (sumatoria votos)) * 100

votosDelPresidente :: String -> [(String,String)] -> [Int] -> Int
votosDelPresidente presidente ((presi,vice):xs) (y:ys) | presidente == presi = y
                                                       | otherwise = votosDelPresidente presidente xs ys

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

-- Ejercicio 4 

proximoPresidente :: [(String,String)] -> [Int] -> String
proximoPresidente ((presi,vice):xs) (y:ys) | maximo (y:ys) == y = presi
                                           | otherwise = proximoPresidente xs ys

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)
