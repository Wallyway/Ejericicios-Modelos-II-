module Primes where

main::IO()

isDividible:: Int -> [Int] -> Bool
isDividible n (x:xs) = (x < sqrt (fromIntegral n) && mod n x /= 0) && isDividible n xs
isDividible n [] = True

{-
prime is
given an n do
at i-nth element verify if is divisible by the i-nth elements before the i-nth position
if is divisible add to the primes list else omit it	
	-}




main = putStrLn "Hello"