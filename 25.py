import math
fiblist=[0,1,1]
i=2
while len(str(fiblist[i]))<1000:
    fiblist.append(fiblist[i]+fiblist[i-1])
    i+=1
print(i)
