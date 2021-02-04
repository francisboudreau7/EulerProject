digs :: Integral a => a -> [a]
digs 0 = []
digs x = digs (x `div` 10) ++ [x `mod` 10]

reconcatdig (x:xs) = x*10^(length (x:xs)-1) + reconcatdig xs
reconcatdig [] = 0


fromDecimal :: Int -> [Int]
fromDecimal 0 = [0]
fromDecimal n = go n []
    where go 0 r = r
          go k rs = go (div k 2) (mod k 2:rs)


isDecPal x = digs x == reverse (digs x)

isBinaryPal x = not ((last binary) == 0) && binary == reverse binary 
        where binary = fromDecimal x 

palindromes = filter isBinaryPal (filter (isDecPal) [1..1000000])

euler = foldl (+) 0 palindromes