module Main where
import System.IO
meets_distance :: Int -> Int -> Int -> Bool
meets_distance pause time distance = distance < (time-pause)*pause
distances :: Int -> Int -> Int 
distances time distance = distances' 0 time distance where
    distances' i time distance 
        | not (meets_distance i time distance) = distances' (i+1) time distance
        | otherwise = time-2*i+1

main = do
    let time = 58996469
    let distance = 478223210191071
    putStrLn $ show $ distances time distance 