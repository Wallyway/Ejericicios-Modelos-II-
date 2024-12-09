module Main where


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
data Figure = Circle { radio :: Double } 
  | Redtangle { s1:: Double, s2:: Double } 
  | Triangle { base :: Double, hight ::Double }
                          
area :: Figure -> Double
area Circle {radio=_radio} = pi*_radio*_radio
area Redtangle {s1=_s1, s2=_s2} = _s1*_s2
area Triangle {base=_base, hight=_hight} = _base/2*_hight

main :: IO ()
main = do print (area Redtangle {s1=5, s2=5})
