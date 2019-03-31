liste=[]
for i in range(10,100):
    for j in range(10,100):
        fraction=i/j
        for k in range(len(str(i))):
            for l in range(len(str(j))):
                if int(str(j)[l])==int(str(i)[k]) and i!=j:
                    a=str(j).split(str(j)[l])
                    a.sort()
                    b=str(i).split(str(i)[k])
                    b.sort()
                    if b[1]!='' and a[1]!=''and int(a[1])!=0 and int(b[1])/int(a[1])==fraction and i%10!=0 and i/j<1:
                        liste.append([i,j,b[1],a[1]])
print(liste)

            
