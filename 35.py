import pickle
primes = pickle.load(open('mypicklefile', 'rb'))
CicularPrimes=[]
indexes=[[0,1,2],[1,2,0],[2,0,1]]

for i in range(1000000):
    num=str(i)
    numTest=""
    succes=0
    for j in range((len(num))):
        for k in range(len(num)):
         numTest+=num[indexes[j][k]]
        if primes[int(numTest)]:
            succes+=1
    if succes==S3:
        CicularPrimes.append(num)

print(len(CicularPrimes))

    

            
        
