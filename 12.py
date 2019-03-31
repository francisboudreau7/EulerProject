import math
n=0
i=0
somme=0
nbDiviseur=500
while n*2<nbDiviseur:
    n=2
    for x in range(1,int(math.sqrt(somme))):
        if somme%x==0:
            n+=1
            if n>nbDiviseur:
                resultat=somme
    i+=1
    somme+=i
    
print(somme-i)
print(somme)
print(somme-i-1)
print(n)

