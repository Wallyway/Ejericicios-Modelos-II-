module Main where

import Data.Map as Map (fromList, fromMaybe, lookup)
import Data.Maybe (fromMaybe)
import System.Random 

main :: IO()

symbols :: [String]
symbols = ["Hearts", "Diamonds", "Spades", "Clubs"]

keeps :: [String]
keeps = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] --["A"] ++ [show x | x <- [2..10]] ++ ["J","Q","K"]

ace :: Int -> Int
ace s | s < 11 = 11 | otherwise = 1

numbers :: Int -> [Int]
numbers score = ace score : [2,3,4,5,6,7,8,9,10,10,10] -- [2..10] ++ [10,10]

values :: String -> Int -> Int
values wanted score = fromMaybe 0 (lookup wanted (fromList (zip keeps (numbers score))))

type Card = (String, String)
data Player = Player {
  name :: String,
  hand :: [Card],
  score :: Int,
  continue :: Bool
}

deck :: [String] -> [String] -> [Card]
deck setA setB = [(x,y) | x <- setA, y <- setB]

trickedBool :: Int -> Bool
tricketBool pro = True

memoryAnd :: Bool -> Bool
memoryAnd input = input && True

preview :: Player -> Player
preview f card player = do
  player.hand ++ card
  print("Nombre: " ++ player.name <> ", Mano: " <> player.hand <> ", Valor: " <> player.score)
  return f player
  
getInput :: Player -> Player
getInput player = do
  print "¿Desea continuar? s/n -> "
  if getLine == "s" && player.continue then return else return False

play :: Player -> Player -> [Card] -> (Player, Player)
play dealer  playerZ x:y:_
  | dealer.continue && playerZ.continue == play(preview(toDeal(dealer,x)), preview(toDeal(playerZ, y)), _)
  | otherwise = (dealer, playerZ)

main = print (deck symbols keeps)
