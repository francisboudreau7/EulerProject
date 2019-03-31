somme=0
for x in range(0,1000000):
    nombre=0
    for y in range(len(str(x))):
       nombre+= int(str(x)[y])**5

    if(nombre==x):
        somme+=x
        print(x)      
print(somme-1) 
       