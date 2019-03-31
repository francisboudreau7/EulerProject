from collections import OrderedDict
def remDupl(t):
    return list(OrderedDict.fromkeys(t))

def checkPandigital(n):
    if ''.join(sorted(n))=='123456789':
        return True
    else:
        return False

liste=[]
for i in range(1,10000):
    for j in range(1,1000):
        product=i*j
        string=str(product)+str(i)+str(j)
        if checkPandigital(string):
                liste.append(product)
print(remDupl(liste))
print(sum(remDupl(liste)))


        
        
