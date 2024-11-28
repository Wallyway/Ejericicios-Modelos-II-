module Main where

main :: IO ()
main = do
    putStrLn "Ejercicio Ultima Cifra"

lastDigit :: Int -> Int
lastDigit n
    | -1 < n && n < 10 = n
    | n > 9 = n `mod` 10
    | otherwise = 0x0
