elems1=["0","1","2"]
listper=[]
def permutation(elems,string,elemsInit):
    print("execution:"+str(len(elems)))
    if len(elems)==1:
        string+=elems[0]
        listper.append(string)
        print("ajout/")
        string=""
        
    else:
        for i in range(len(elems)):
            print("for"+str(i))
            string+=elems[i]
            print("pop!"+str(len(elems)))
            
            permutation(elems.copy().pop(i),string,elemsInit)

import math
E=[0,1,2,3,4,5,6,7,8,9]
k=10



def A(i,n):
    j=k-1-i
    if i==0:
        return E[int(math.floor(n/math.factorial(j)))]
    if i==1:
       D=E.copy()
       D.remove(A(0,n))
       return D[int(math.floor(n%(math.factorial(j+1))/math.factorial(j)))]
    else:
        B=E.copy()
        for x in range(i):
            B.remove(A(x,n))
        return B[int(math.floor(n%(math.factorial(j+1))/math.factorial(j)))]


def per(n,E):
    k=len(E)
    string=""
    for i in range(k):
        string+=str(A(i,n))
    return string


print(per(999999,[0,1,2,3,4,5,6,7,8,9]))



