
digs :: Integral a => a -> [a]
digs 0 = []
digs x = digs (x `div` 10) ++ [x `mod` 10]


chap = concatMap digs [1..10000000]

euler = chap!!(1-1) * chap!!(10-1) * chap!!(100-1) * chap!!(1000-1) * chap!!(10000-1) * chap!!(100000-1) *chap!!(1000000-1)
