module Main where

main :: IO ()
main = do
    putStrLn "Ejercicio Primera Cifra"

tresIguales :: Eq a => a -> a -> a -> Bool
tresIguales x y z = x == y && y == z