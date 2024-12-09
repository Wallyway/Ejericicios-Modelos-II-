module Main where
import Text.Printf (printf)


-- 1. Intercalar
merge :: [a] -> [a] -> [a]
merge (x:xs) (y:ys) = [x, y] ++ merge xs ys
merge (x:xs) [] =  x:xs
merge [] (y:ys) = y:ys
merge [] [] = []

-- 2. Aplicar a todos
forEach :: [a] -> (a -> a) -> [a]
forEach set f = [f x | x <- set]

-- 3. Tipos de datos
data Figure = Circle { radio :: Float } 
    | Redtangle { s1:: Float, s2:: Float } 
    | Triangle { base :: Float, hight ::Float }
                          
area :: Figure -> Float
area Circle {radio=_radio} = pi*_radio*_radio
area Redtangle {s1=_s1, s2=_s2} = _s1*_s2
area Triangle {base=_base, hight=_hight} = _base/2*_hight

main :: IO ()
main = do
    printf "\n1. Intercarlar [1,3,7] con [2,4,6]\nR: %s\n\n" (show (merge [1,3,7] [2,4,6]))
    printf "2. Aplicar *2 a todos en [1,2,3,4,5,6]\nR: %s\n\n" (show (forEach [1,2,3,4,5,6] (*2)))
    printf "3. Area de un círculo con radio de 5cm. R: %scm^2\n" (show (area Circle {radio=5}))
    printf "   Area de un cuadrado de lado 5cm. R: %scm^2\n" (show (area Redtangle {s1=5, s2=5}))
    printf "   Area de un triángulo de base 5 y altura 5. R: %scm^2" (show (area Triangle {base=5, hight=5}))

