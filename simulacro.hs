relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas (x:xs) | incluido [x] (xs) || incluidoTuplas x xs || fst x == snd x = False
                         | otherwise = relacionesValidas xs

quitar :: (Eq t) => t -> [t] -> [t]
-- requiere x pertenece a y
quitar x (y:ys)
 | x == y = ys
 | otherwise = y : quitar x ys 

incluido :: (Eq t) => [t] -> [t] -> Bool
incluido [] l = True
incluido (x:c) l = elem x l && incluido c (quitar x l)

incluidoTuplas :: (String,String) -> [(String,String)] -> Bool
incluidoTuplas _ [] = False
incluidoTuplas (a,b) ((c,d):xs)  | (a == c && b == d) || (a == d && b == c) = True
                                 | otherwise = incluidoTuplas (a,b) xs

sonIguales :: (Eq t) => [t] -> [t] -> Bool
sonIguales xs ys = incluido xs ys && incluido ys xs 

personas :: [(String,String)] -> [String]
personas [] = []
personas ((a,b):xs) = a : b : (personas xs)

-- los hacemos en clase

relacionesValidas2 :: [(String,String)] -> Bool
relacionesValidas2 ((a,b):xs) = a /= b  && not(pertenece (a,b) xs) && not(pertenece (b,a) xs) && (relacionesValidas xs)

pertenece :: (String,String) -> [(String,String)] -> Bool
pertenece _ [] = False
pertenece t (x:xs) = t == x || pertenece t xs

personas2 :: [(String,String)] -> [String]
personas2 xs = sacarRepetidos (personasConRepetidos xs)

sacarRepetidos :: [String] -> [String]
sacarRepetidos (x:xs) | elem x xs = sacarRepetidos xs
                      | otherwise = x:(sacarRepetidos xs)

personasConRepetidos :: [(String,String)] -> [String]
personasConRepetidos [] = []
personasConRepetidos ((a,b):xs) = a:b:(personasConRepetidos xs)

amigosDe :: String -> [(String,String)] -> [String]
amigosDe _ [] = [] 
amigosDe p ((a,b):xs) | p == a = b:(amigosDe p xs)
                      | p == b = a:(amigosDe p xs)
                      | otherwise = amigosDe p xs

personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos xs = personaConMasAmigosAux (personas xs) xs

cantAmigos :: String -> [(String,String)] -> Int
cantAmigos p rel = length (amigosDe p rel)

personaConMasAmigosAux :: [String] -> [(String,String)] -> String
personaConMasAmigosAux [x] _ = x
personaConMasAmigosAux (x:y:xs) rel | cantAmigos x rel > cantAmigos y rel = personaConMasAmigosAux (x:xs) rel
                                    | otherwise = personaConMasAmigosAux (y:xs) rel
