somme=0
import math
def f(x):
    return {
        0: 0,
        1: 3,
        2: 3,
        3: 5,
        4: 4,
        5: 4,
        6: 3,
        7: 5,
        8: 6,
        9: 4,
        10: 3,
        11: 6,
        12: 6,
        13: 8,
        14: 8,
        15: 7,
        16: 7,
        17: 9,
        18: 8,
        19: 8,
    }[x]
def g(x):
    return {
        2:6,
        3:6,
        4:5,
        5:5,
        6:5,
        7:7,
        8:6,
        9:6,
    }[x]
def words(n):
    if n<20:
        return f(n)
    if n>=20 and n<100:
        return g(math.floor(n/10))+words(n-math.floor(n/10)*10)
    
    #if n>=100 and n<200:
    #    return 11+ words(n-100)
    if n>=200:
        valeur=words(math.floor(n/100))+7
        valif1=(float(n)/float(100))
        valif2=math.floor(n/100)
        if valif1 != valif2:
            valeur += 3


        valeur += words(n-(math.floor(n/100)*100))

        return valeur
for i in range(1,1000):
   somme+=words(i)
print(words(60))
