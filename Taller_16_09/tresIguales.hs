
module Main where

main::IO()

tresIguales :: Eq int => int -> int -> int -> Bool
tresIguales x y z = x == y && x == z && y == z
main = putStrLn "Hello, this is tresIguales"
