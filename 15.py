def lat(n):
    if n==0:
        return 1
    if n==1:
        return 2
    sortie=3*lat(n-1)
    somme=0
    for k in range(1,n-1):
        somme+=lat(k)*lat(n-k-1)
    return (sortie+somme)
print(lat(20))
