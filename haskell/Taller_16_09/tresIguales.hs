module Main where

main :: IO ()
main = do
    putStrLn "Ejercicio Tres iguales"

tresIguales :: Eq a => a -> a -> a -> Bool
tresIguales x y z = x == y && y == z