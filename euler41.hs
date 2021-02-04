import Data.List

isPrime:: Integer -> Bool
isPrime n = n > 1 &&
              foldr (\p r -> p*p > n || ((n `rem` p) /= 0 && r))
                True primes
primes = 2 : filter isPrime [3,5..]

allpandigitals = (concatMap (\y -> permutations [1..y]) [1..9])


permuCandidates = reverse (sort (map reconcatdig (allpandigitals)))

reconcatdig (x:xs) = x*10^(length (x:xs)-1) + reconcatdig xs
reconcatdig [] = 0

euler = head $ filter isPrime permuCandidates