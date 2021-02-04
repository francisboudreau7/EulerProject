
digs :: Integral a => a -> [a]
digs 0 = []
digs x = digs (x `div` 10) ++ [x `mod` 10]


reconcatdig (x:xs) = x*10^(length (x:xs)-1) + reconcatdig xs
reconcatdig [] = 0

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

leadingdigits x = elem (last digits) [1,3,7,9] && elem (head digits) [1,3,7,9]
                where digits = digs x

 

rightTruncatPrime :: [Int] -> Bool
rightTruncatPrime (x:xs) =  isPrime (reconcatdig (x:xs)) && rightTruncatPrime xs
rightTruncatPrime [] = True

leftTruncatPrime :: [Int] -> Bool
leftTruncatPrime (x:xs) =  isPrime (reconcatdig (x:xs)) && leftTruncatPrime (init (x:xs))
leftTruncatPrime [] = True


euler = sum (map reconcatdig (filter leftTruncatPrime (filter rightTruncatPrime (map digs (filter isPrime [10..1000000])))))