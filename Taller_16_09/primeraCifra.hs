module Main where

main :: IO ()
main = do
    putStrLn "Ejercicio Primera Cifra"

firstDigit :: Int -> Int
firstDigit n
    | n >= 0 && n < 10 = n
    | n < 0 = firstDigit (-n)  -- Si el número es negativo, consideramos su valor absoluto
    | otherwise = firstDigit (n `div` 10)