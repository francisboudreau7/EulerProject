import math
puissance=10000
liste=[2]
def mult(x):
    x*=2
    return x

for x in range(puissance-1):
    liste=map(mult,liste)
    for i in range(len(liste)):
        if(liste[i]!=0):
            if math.log10(liste[i])>=1:
                if len(liste)>i+1:
                    liste[i+1]+=int(math.floor(math.log10(liste[i])))
                    liste[i]-=10*int(math.floor(math.log10(liste[i])))
                else:
                    liste.append(int(math.floor(math.log10(liste[i]))))
                    liste[i]-=10*int(math.floor(math.log10(liste[i])))

        
print(reduce(lambda x,y:x+y,liste))



        
      


