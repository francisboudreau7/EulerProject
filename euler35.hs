digs :: Integral a => a -> [a]
digs 0 = []
digs x = digs (x `div` 10) ++ [x `mod` 10]


rotation x = take (len*2) (cycle (digs x))
             where len = length (digs x) 


lsrot len n (x:xs)
    |n == 0 = []
    |otherwise = take len (x:xs) : lsrot len (n-1) xs

fullrot x = lsrot len len (rotation x)
            where len = length (digs x) 

reconcatdig (x:xs) = x*10^(length (x:xs)-1) + reconcatdig xs
reconcatdig [] = 0

circular x = map reconcatdig (fullrot x)


isPrime:: Int -> Bool
isPrime n = n > 1 &&
              foldr (\p r -> p*p > n || ((n `rem` p) /= 0 && r))
                True primes

primeFactors n | n > 1 = go n primes   -- or go n (2:[3,5..])
   where                               -- for one-off invocation
     go n ps@(p:t)
        | p*p > n    = [n]
        | r == 0     =  p : go q ps
        | otherwise  =      go n t
                where
                  (q,r) = quotRem n p
    
primes = 2 : filter isPrime [3,5..]


islistprime x = foldl (&&) True (map (isPrime) x)

euler = 13 + length (filter id (map countainsNotPrimeDigits (map digs [100..1000000])))



countainsNotPrimeDigits num 
                 |2 `elem` num = False
                 |4 `elem` num = False
                 |6 `elem` num = False
                 |8 `elem` num = False
                 |0 `elem` num = False
                 |5 `elem` num = False
                 |otherwise =  islistprime (circular (reconcatdig num))


main = print euler
