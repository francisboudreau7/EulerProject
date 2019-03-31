import math
somme=0
for x in range(0,10000000):
    nombre=0
    for y in range(len(str(x))):
       nombre+= math.factorial(int(str(x)[y]))

    if(nombre==x):
        somme+=x
        print(x)      
print(somme-3) 
       