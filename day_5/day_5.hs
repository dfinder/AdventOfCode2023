{-# LANGUAGE OverloadedStrings #-}
module Main where
import System.IO
import Data.List
import Data.List.Split
import Data.String.Utils
type Triplet = (Int, Int, Int)

range_translation :: [Triplet] -> Int -> Int

range_translation [] b = b 
range_translation a@((drange,srange,rlen):xs) b 
    | b<srange+rlen && (b>=srange) = b-srange+drange
    | otherwise = range_translation xs b

recursive_mapping :: [[Triplet]] -> Int -> Int 
recursive_mapping [] b = b 
recursive_mapping a@(x:xs) b= recursive_mapping xs $ range_translation x b

tripletfier :: [Int] -> Triplet
tripletfier x = (x!!0,x!!1,x!!2)
enumerate :: [Int] -> [(Int,Int)] 
enumerate x = Data.List.zip [0..] x
main = do 
    inp <- readFile "./input.txt"
    let my_lines = Data.List.Split.splitOn ":" inp 
    let processor = \x -> Data.List.Split.splitOn "\n" . strip . Data.List.head . Data.List.Split.splitOn "\n\n" x 
    my_lines_processed <- Data.List.tail Data.List.map processor my_lines
    let numerizer = \x -> tripletfier . read . splitOn " " x 
    seeds <- numerizer fst fst my_lines_processed
    maps <- Data.List.map.(Data.List.map) numerizer $ Data.List.tail my_lines_processed
    [starts,ranges] <- Data.List.transpose . Data.List.Split.chunksOf 2 $ seeds
    enum <- enumerate starts
    seed_ranges <- Data.List.map (\x -> [snd x..(snd x+ranges!!(fst x))]) enum
    seed_range <- Data.List.concat seed_ranges 
    putStrLn show $ min . Data.List.map recursive_mapping $ maps seed_range 