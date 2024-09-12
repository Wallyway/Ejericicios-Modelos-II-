 module Main where

suml :: [Int] -> Int 
suml [] =  0
suml (x:xs) = x + suml xs


main :: IO ()
main = do print (suml [1,2,3])
