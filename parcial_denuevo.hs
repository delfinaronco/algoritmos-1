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

--porcentajeDeVotos :: String -> [(String,String)] -> [Int] -> Float
--porcentajeDeVotos presidente formulas votos 

votosDelPresidente :: String -> [(String,String)] -> [Int] -> Int
votosDelPresidente presidente ((presi,vice):xs) votos | presidente == presi = votos[0]
                                                      | otherwise = votosDelPresidente presidente xs votos
