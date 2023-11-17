# Ejercicio 6

type Usuario = (Integer, String) -- (id, nombre)
type Relacion = (Usuario, Usuario) -- usuarios que se relacionan
type Publicacion = (Usuario, String, [Usuario]) -- (usuario que publica, texto publicacion, likes)
type RedSocial = ([Usuario], [Relacion], [Publicacion])

red1 = ([(1,"Delfina"),(2,"Nahuel"),(3,"Franco")],[((1,"Delfina"),(2,"Nahuel")),((1,"Delfina"),(2,"Franco"))],[((1,"Delfina"),"hola mundo",[(2,"Nahuel"),(3,"Franco")]),((2,"Nahuel"),"chau",[(2,"Nahuel")])])

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
