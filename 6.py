import math

def is_prime_number(x):
    if x >= 2:
        for y in range(2,math.floor(sqrt(x)))
        :
            if not ( x % y ):
                return False
    else:
	return False
    return True
n=0
i=1
while n<10001:
    if(is_prime_number(i)):
        n=n+1
        print(n)
        print(i)
        
    i+=1
    
print i