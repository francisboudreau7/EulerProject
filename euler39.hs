
import Data.List

triples :: [(Integer, Integer, Integer)]
triples = [(k*(m^2-n^2),2*m*n*k,k*(m^2+n^2))|m<-[1..500],n<-[1..500],
                                             m > n,
                                             not(odd m && odd n),
                                             coprime m n,
                                             k<-[1..100],
                                             (k*(m^2-n^2)+2*m*n*k+k*(m^2+n^2))<1000]

coprime :: Integral a => a -> a -> Bool
coprime a b = gcd a b == 1

addTriple (a,b,c) = (a+b+c,(a,b,c))


compareTriples (sum1,(_,_,_)) (sum2,(_,_,_)) | sum1 < sum2 = GT
                                             | otherwise = LT

compareLength a b = if  (length a) > (length b) then GT else LT

grouping (sum1,(_,_,_)) (sum2,(_,_,_)) = sum1 == sum2

euler =  (head (reverse (sortBy (compareLength) ((groupBy grouping . sortBy compareTriples) (map addTriple triples)))))


main = print (euler)