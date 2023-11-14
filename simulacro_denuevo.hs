pertenece :: (Eq t) => t -> [t] -> Bool
pertenece n [] = False
pertenece n (x:xs) = n == x || pertenece n xs

-- Ejercicio 1
relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [(a,b)] = a /= b 
relacionesValidas ((a,b):xs) = a /= b  && not(pertenece (a,b) xs) && not(pertenece (b,a) xs) && (relacionesValidas xs)

-- Ejercicio 2
personas :: [(String,String)] -> [String]
personas [] = []
personas ((a,b):xs) = sacarRepetidos (a : b : personas xs)

sacarRepetidos :: [String] -> [String]
sacarRepetidos [] = []
sacarRepetidos (x:xs) | pertenece x xs = sacarRepetidos xs
                      | otherwise = x : sacarRepetidos xs

-- Ejercicio 3

amigosDe :: String -> [(String,String)] -> [String]
amigosDe persona [] = []
amigosDe persona ((a,b):xs) | persona == a = b : amigosDe persona xs 
                            | persona == b = a : amigosDe persona xs 
                            | otherwise = amigosDe persona xs

-- Ejercicio 4

personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos relaciones = personaConMasAmigosAux (personas relaciones) relaciones

cantDeAmigos :: String -> [(String,String)] -> Int
cantDeAmigos persona relaciones = longitud (amigosDe persona relaciones)

longitud :: [t] -> Int
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

personaConMasAmigosAux :: [String] -> [(String,String)] -> String
personaConMasAmigosAux [x] relaciones = x
personaConMasAmigosAux  (x:y:xs) relaciones | cantDeAmigos x relaciones > cantDeAmigos y relaciones = personaConMasAmigosAux (x:xs) relaciones
                                            | otherwise = personaConMasAmigosAux (y:xs) relaciones
