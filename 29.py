def f(a,b):
    liste=[]
    for i in range(2,a+1):
        for j in range(2,b+1):
            liste.append(i**j)
    return liste
print(len(set(f(100,100))))