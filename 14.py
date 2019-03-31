max=[0,1]

for n in range(1,10000000):
    i=0
    x=n
    while x!=1:
        if x%2==0:
            x=x/2
        else:
            x=3*x+1
        i+=1

    if max[0]<i:
        max[0]=i
        max[1]=n
print(max)
