-- Ejercicio 1

esMin :: Char -> Bool
esMin letra = (letra == 'a') || (letra == 'b') || (letra == 'c') || (letra == 'd') || (letra == 'e') || (letra == 'f') || (letra == 'g') || (letra == 'h') || (letra == 'i') || (letra == 'j') || (letra == 'k') || (letra == 'l') || (letra == 'm') || (letra == 'n') || (letra == 'o') || (letra == 'p') || (letra == 'q') || (letra == 'r') || (letra == 's') || (letra == 't') || (letra == 'u') || (letra == 'v') || (letra == 'w') || (letra == 'x') || (letra == 'y') || (letra == 'z') 

cantMinuscula :: String -> Int
cantMinuscula [] = 0
cantMinuscula (x:xs) | esMin x = 1 + cantMinuscula xs
                     | otherwise = cantMinuscula xs

-- Ejercicio 2

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)


cantCambios :: String -> Int
cantCambios [] = 0
cantCambios (x:xs) | x == ' ' = cantCambios xs
                   | (esMin x == False) = 1 + cantCambios xs
                   | otherwise = cantCambios xs

listaCambios :: [String] -> [Int]
listaCambios [] = []
listaCambios (x:xs)= cantCambios x : listaCambios xs

maximoCambios :: [String] -> String
maximoCambios [] = []
maximoCambios (x:xs) | (maximo (listaCambios (x:xs)) == cantCambios x) = x
                     | otherwise = maximoCambios xs


-- Ejercicio 3

charANat :: Char -> Int
charANat letra | letra == 'a' = 1
               | letra == 'b' = 2
               | letra == 'c' = 3
               | letra == 'd' = 4
               | letra == 'e' = 5
               | letra == 'f' = 6
               | letra == 'g' = 7
               | letra == 'h' = 8
               | letra == 'i' = 9
               | letra == 'j' = 10
               | letra == 'k' = 11
               | letra == 'l' = 12
               | letra == 'm' = 13
               | letra == 'n' = 14
               | letra == 'o' = 15
               | letra == 'p' = 16
               | letra == 'q' = 17
               | letra == 'r' = 18
               | letra == 's' = 19
               | letra == 't' = 20
               | letra == 'u' = 21
               | letra == 'v' = 22
               | letra == 'w' = 23
               | letra == 'x' = 24
               | letra == 'y' = 25
               | letra == 'z' = 26

-- natAChar :: Int -> Char recibe un número natural entre 0 y 25 y devuelve el caracter correspondiente

natAChar :: Int -> Char
natAChar n | n == 1 = 'a'
           | n == 2 = 'b'
           | n == 3 = 'c'
           | n == 4 = 'd'
           | n == 5 = 'e'
           | n == 6 = 'f'
           | n == 7 = 'g'
           | n == 8 = 'h'
           | n == 9 = 'i'
           | n == 10 = 'j'
           | n == 11 = 'k'
           | n == 12 = 'l'
           | n == 13 = 'm'
           | n == 14 = 'n'
           | n == 15 = 'o'
           | n == 16 = 'p'
           | n == 17 = 'q'
           | n == 18 = 'r'
           | n == 19 = 's'
           | n == 20 = 't'
           | n == 21 = 'u'
           | n == 22 = 'v'
           | n == 23 = 'w'
           | n == 24 = 'x'
           | n == 25 = 'y'
           | n == 26 = 'z'


desplazar :: Char -> Int -> Char
desplazar caracter n | (esMin caracter == False) = caracter
                     | (charANat caracter + n) > 26 = natAChar ((charANat caracter - 26) + n)
                     | (charANat caracter + n) < 1 = natAChar ((charANat caracter + 26) + n)
                     | otherwise = natAChar ((charANat caracter) + n)