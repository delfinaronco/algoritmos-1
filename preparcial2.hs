import System.Win32 (COORD(xPos))


-- Dado un número n devuelve una lista cuyos elementos sean los números comprendidos entre
-- n y 1 (incluidos). Si el número es inferior a 1, devuelve la lista vacía.

cuentaRegresiva :: Int -> [Int]
cuentaRegresiva n | n < 1 = [] 
                  | otherwise = n : cuentaRegresiva (n - 1)

-- Dado un número n y un elemento e devuelve una lista en la que el elemento e repite n veces
-- Precondicion: no se puede repetir n negativas veces

repetir :: Int -> t -> [t]
repetir 0 e = []
repetir n e = e : repetir (n-1) e

-- Dados un número n y una lista xs, devuelve una lista con los n primeros elementos de xs.
-- Si la lista es vacía, devuelve una lista vacía.

losPrimeros :: Int -> [Int] -> [Int]
losPrimeros 0 _ = []
losPrimeros n [] = []
losPrimeros n (x:xs) = x : losPrimeros (n-1) xs

-- Dados una edad y una lista de personas devuelve a las personas mayores a esa edad.

mayoresA :: Int -> [(String,Int)] -> [String]
mayoresA n [] = []
mayoresA n ((nombre,edad):xs) | edad >= n = nombre : mayoresA n xs
                              | otherwise = mayoresA n xs

-- Dada una lista de personas devuelve el promedio de edad entre esas personas. Precondición: la lista al menos posee una persona.

sumaEdades :: [(String,Int)] -> Int
sumaEdades [] = 0
sumaEdades ((persona,edad):xs) = edad + sumaEdades xs

promedioEdad :: [(String,Int)] -> Int
promedioEdad personas = div (sumaEdades personas) (length personas)

-- Dada una persona y una lista de personas con sus edades devuelve la edad de la persona.

edadDePersona :: String -> [(String,Int)] -> Int
edadDePersona persona [] = 0
edadDePersona persona ((nombre,edad):xs) | persona == nombre = edad 
                                         | otherwise = edadDePersona persona xs

-- Dada una lista de personas devuelve la persona más vieja de la lista.

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)

edades :: [(String,Int)] -> [Int]
edades [] = []
edades ((nombre,edad):xs) = edad : edades xs

elMasViejo :: [(String,Int)] -> String
elMasViejo ((nombre,edad):xs) | maximo (edades ((nombre,edad):xs)) == edad = nombre
                              | otherwise = elMasViejo xs

-- Contar las personas de un determinado equipo. 

contarHinchasDe :: String -> [(String,String)] -> Int
contarHinchasDe equipo [] = 0
contarHinchasDe equipo ((persona,cuadro):xs) | (equipo == cuadro) = 1 + contarHinchasDe equipo xs
                                             | otherwise = contarHinchasDe equipo xs

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

porcentajeHinchasDe :: String -> [(String,String)] -> Float
porcentajeHinchasDe equipo hinchas = (division (contarHinchasDe equipo hinchas) (length hinchas)) * 100

-- otro ejercicio

sumaPerros :: [(String,Int,Int)] -> Int
sumaPerros [] = 0
sumaPerros ((persona,perros,gatos):xs) = perros + sumaPerros xs

sumaGatos :: [(String,Int,Int)] -> Int
sumaGatos [] = 0 
sumaGatos ((persona,perros,gatos):xs) = gatos + sumaGatos xs

cantidadDePerrosYGatos :: [(String,Int,Int)] -> (Int,Int)
cantidadDePerrosYGatos personas = ((sumaPerros personas), (sumaGatos personas))

mayoria :: [(String,Int,Int)] -> String
mayoria personas | fst (cantidadDePerrosYGatos personas) > snd (cantidadDePerrosYGatos personas) = "perros"
                 | fst (cantidadDePerrosYGatos personas) < snd (cantidadDePerrosYGatos personas) = "gatos"
                 | otherwise = "ambos"
