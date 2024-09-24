module Main where

main::IO()

rectanguloMayor :: [Int] -> [Int] -> [Int]
rectanguloMayor [a, b] [c, d] 
    |   a >= c || b >= d = [a,b]
    |   a < c || b < d = [c,d]
    |   otherwise = []

main = print(rectanguloMayor [1, 2] [2,0])
