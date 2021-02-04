
import Data.List ( permutations, sort )
import GHC.Types ()


permuCandidates = reverse (sort (map reconcatdig (permutations [1,2,3,4,5,6,7,8,9])))




reconcatdig (x:xs) = x*10^(length (x:xs) - 1) + reconcatdig xs
reconcatdig [] = 0

uncontProduct n = [n*x|x <- [1..]] 

testCandidate acc n 
            |acc < 5 = (digs n) == take 9 (concat (map digs (uncontProduct (reconcatdig (take acc (digs n)))))) || testCandidate (acc+1) n
            |otherwise = False

digs :: Integral a => a -> [a]
digs 0 = []
digs x = digs (x `div` 10) ++ [x `mod` 10]


euler = head (filter (testCandidate 1) permuCandidates)