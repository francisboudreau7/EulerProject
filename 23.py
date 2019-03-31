def d(n):
    sum=0
    for x in range(1,n):
        if n%x==0:
            sum+=x
    return sum

#estce que le nombre S peut etre forme d'une paire de nombre de arr
def twoSum(arr, S):

  sums = []
  hashTable = {}

  # check each element in array
  for i in range(0, len(arr)):

    # calculate S minus current element
    sumMinusElement = S - arr[i]

    # check if this number exists in hash table
    # if so then we found a pair of numbers that sum to S
    if sumMinusElement in hashTable:
      return True

    # add the current number to the hash table
    hashTable[arr[i]] = arr[i]

  # return all pairs of integers that sum to S
  return False

print twoSum([12,12, 18, 20, 24,], 24)     

nbAbondants=[]
nbNonSum=[]
for n in range(28200):
    if d(n)>n:
        nbAbondants.append(n)
        nbAbondants.append(n)

for n in range(28200):

    if not twoSum(nbAbondants,n):
        nbNonSum.append(n)
        

""" somme=0

for n in range(28123):
    if n%1000==0:
        print(n)
    condition=False
    for i in range(len(nbAbondants)):
        if nbAbondants[i]>n:
            break
        for j in range(len(nbAbondants)):
            if  nbAbondants[j]>n:
                break
            if nbAbondants[i]+nbAbondants[j]>n:
                break
            if nbAbondants[i]+nbAbondants[j]==n:
                condition=True
    if condition==False:
        somme+=n
print(somme) """
""" sommeAbon=[]
for i in range(len(nbAbondants)):
    for j in range(i,len(nbAbondants)):
        sommeAbon.append(nbAbondants[i]+nbAbondants[j])
sommeNat=0

def indexOf(n,liste):
    for i in range(len(liste)):
        if n==liste[i]:
            return True
        elif i==len(liste)-1:
            return False


def remDup(x):
  return list(dict.fromkeys(x))

sommeAbon=remDup(sommeAbon)

print(len(sommeAbon))


for i in range(sommeAbon[len(sommeAbon)-1]):
    sommeNat+=i

nblimite=[]

for i in range(len(sommeAbon)):
    if sommeAbon[i]>sommeAbon[i-1]+1:
        nblimite.append([i,sommeAbon[i],sommeAbon[i-1]]) """


print(reduce(lambda x, y:x+y, nbNonSum))
print(nbAbondants)

