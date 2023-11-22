-- Ejercicio 6

type Usuario = (Integer, String) -- (id, nombre)
type Relacion = (Usuario, Usuario) -- usuarios que se relacionan
type Publicacion = (Usuario, String, [Usuario]) -- (usuario que publica, texto publicacion, likes)
type RedSocial = ([Usuario], [Relacion], [Publicacion])


usuarios :: RedSocial -> [Usuario]
usuarios (us, _, _) = us

relaciones :: RedSocial -> [Relacion]
relaciones (_, rs, _) = rs

publicaciones :: RedSocial -> [Publicacion]
publicaciones (_, _, ps) = ps

idDeUsuario :: Usuario -> Integer
idDeUsuario (id, _) = id 

nombreDeUsuario :: Usuario -> String
nombreDeUsuario (_, nombre) = nombre

usuarioDePublicacion :: Publicacion -> Usuario
usuarioDePublicacion (u, _, _) = u

likesDePublicacion :: Publicacion -> [Usuario]
likesDePublicacion (_, _, us) = us


publicacionesDe :: RedSocial -> Usuario -> [Publicacion]
publicacionesDe red usuario = aux usuario (publicaciones (red))

aux :: Usuario -> [Publicacion] -> [Publicacion]
aux usuario [] = []
aux usuario (x:xs) | usuario == (usuarioDePublicacion x) = x: (aux usuario (xs))
                   | otherwise = aux usuario xs

-- Ejercicio 7

--likesDePublicacion :: Publicacion -> [Usuario]
--likesDePublicacion (_, _, us) = us

--type Publicacion = (Usuario, String, [Usuario]) -- (usuario que publica, texto publicacion, likes)
-- type RedSocial = ([Usuario], [Relacion], [Publicacion])

publicacionesQueLeGustanA :: RedSocial -> Usuario -> [Publicacion]
publicacionesQueLeGustanA red usuario = aux2 usuario (publicaciones(red))

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece a (x:xs) = a == x || pertenece a xs

aux2 :: Usuario -> [Publicacion] -> [Publicacion]
aux2 usuario [] = []
aux2 usuario (x:xs) | pertenece usuario (likesDePublicacion x) = x : aux2 usuario xs
                    | otherwise = aux2 usuario xs

-- Ejercicio 8

estaIncluido :: (Eq t) => [t] -> [t] -> Bool
estaIncluido _ [] = False
estaIncluido [] _ = True
estaIncluido (x:xs) (y:ys) | pertenece x (y:ys) = estaIncluido xs (y:ys)
                           | otherwise = False

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos a b = estaIncluido a b && estaIncluido b a

lesGustanLasMismasPublicaciones :: RedSocial -> Usuario -> Usuario -> Bool
lesGustanLasMismasPublicaciones red usuario1 usuario2 = mismosElementos (publicacionesQueLeGustanA red usuario1) (publicacionesQueLeGustanA red usuario2)


-- type RedSocial = ([Usuario], [Relacion], [Publicacion])                          

-- Ejercicio 1

red1 = ([(1,"Delfina"),(2,"Nahuel"),(3,"Franco")],[((1,"Delfina"),(2,"Nahuel")),((1,"Delfina"),(2,"Franco"))],[((1,"Delfina"),"hola mundo",[(2,"Nahuel"),(3,"Franco")]),((2,"Nahuel"),"chau",[(3,"Franco"),(2,"Nahuel")])])

aux3 :: [Usuario] -> [String]
aux3 [] = []
aux3 ((a,b):xs) = b : aux3 xs

nombresDeUsuarios :: RedSocial -> [String]
nombresDeUsuarios red = aux3 (usuarios red)

-- Ejercicio 2

amigosDe :: RedSocial -> Usuario -> [Usuario]
amigosDe red usuario = amigosDeAux (relaciones red) usuario


amigosDeAux :: [Relacion] -> Usuario -> [Usuario]
amigosDeAux [] _ = []
amigosDeAux ((a,b):xs) usuario | usuario == a = b : amigosDeAux xs usuario
                               | usuario == b = a : amigosDeAux xs usuario
                               | otherwise = amigosDeAux xs usuario

user1 = (1,"Juan")
user2 = (2, "Maria")
user3 = (3,"Nahuel")
user4 = (4,"Delfina")

-- [(user1,user3),(user1,user2)]

-- Ejercicio 3

cantidadDeAmigos :: RedSocial -> Usuario -> Int
cantidadDeAmigos red usuario = length (amigosDe red usuario)

-- Ejercicio 4

usuarioConMasAmigosAux :: RedSocial -> [Usuario] -> Usuario
usuarioConMasAmigosAux red [x] = x
usuarioConMasAmigosAux red (x:y:xs) | (cantidadDeAmigos red x) >= (cantidadDeAmigos red y) = usuarioConMasAmigosAux red (x:xs)
                                 | otherwise = usuarioConMasAmigosAux red (y:xs)

usuarioConMasAmigos :: RedSocial -> Usuario
usuarioConMasAmigos red = usuarioConMasAmigosAux red (usuarios red)



