
def d(n):
    sum=0
    for x in range(1,n):
        if n%x==0:
            sum+=x
    return sum

def indexOf(n,liste):
    for i in range(len(liste)):
        if n==liste[i]:
            return False
        elif i==len(liste)-1:
            return True
somme=0
liste=[]

for n in range(1,10001):
    b=d(n)
    if d(b)==n and b<10000 and n<10000 and n!=b:
    
        somme+=n

print(somme)
