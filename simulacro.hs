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

