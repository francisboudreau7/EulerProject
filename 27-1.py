import pickle

def approach3(givenNumber):  
    
    # Initialize a list
    primes = [False,False]
    for possiblePrime in range(2, givenNumber + 1):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                primes.append(False)
                break
        if isPrime:
            primes.append(True)
    
    return(primes)

hashTable=approach3(10000000)
pickle.dump(hashTable, open('mypicklefile', 'wb'))
print(hashTable[13])