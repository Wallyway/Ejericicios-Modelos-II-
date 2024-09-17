module Main where

main :: IO ()
main = do
    putStrLn "Ejercicio Mayor Rectangulo"

mayorRectangulo :: (Integer, Integer) -> (Integer, Integer) -> (Integer, Integer)
mayorRectangulo r1 r2
    | area r1 >= area r2 = r1
    | otherwise = r2
  where
    area (base, altura) = base * altura