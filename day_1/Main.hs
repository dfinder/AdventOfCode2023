module Main where
import System.IO
import System.Environment
import Data.Char
import Data.Int 
main :: IO ()
tf :: Bool -> Char
tf True = 't'
tf False = 'f'


--number_map :: String -> String 
--number_map _ -> _ 

--first_number :: String -> Num
--first_number str@(x:xs)
---    | 
--    | otherwise

filterNonDigits :: String -> String
filterNonDigits str = filter (\c -> isDigit c ) str

digitsToNumbers
--number_map "one"
main = do 
    inp <- readFile "./input.txt"
    putStrLn (map head $map filterNonDigits$lines inp)

