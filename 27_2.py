import pickle
def isPrime(n):
    isPrime = True
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            isPrime = False
            return isPrime
        
    return isPrime

def comeOnPrimes(n):
    if n<10000000:
        return primes[n]
    else:
        return isPrime(n)
primes = pickle.load(open('mypicklefile', 'rb'))

maximum=[0,0,0]

for a in range(-1000,1000):
    for b in range(-1000,1000):
        for n in range(1000):
            f=n**2+a*n+b
            if comeOnPrimes(f):
                if n>maximum[0]:
                    print(maximum)
                    maximum=[n,a,b]
            else:break


            