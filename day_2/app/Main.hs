module Main where
import Dict exposing Dict
import Data.List.Split
data Pull = Dict Color Int
data Color = Red | Green | Blue
data Game = Int [Pull]
min_amount :: [Pull] -> Color -> Int
min_amount [] b = 0
min_amount a@(x:xs) b = max (get b x) (min_amount xs b)

eval :: Pull -> Boolean
eval a = (get Red a)<13 and (get Blue a)<15 and (get Green a)<14

create_game :: String -> Game 
create_game a = Get_ID a Get_Pulls a 

Get_ID :: String -> Int
Get_ID a = last $ splitOn " " (head $ splitOn ":" a)

get_Pulls :: String -> [Pull]
get_Pulls a = map parse_pull (splitOn ";" (tail $ splitOn ":" a))

parse_pull :: String -> Pull

main :: IO ()
main = putStrLn "Hello, Haskell!"
