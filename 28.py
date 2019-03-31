# import math
# def createSpinArray(n):
#     spinArray=[[0]]

#     for i in range(n-1):
#         spinArray[0].append(0)
#     for i in range(n-1):
#         spinArray.append(spinArray[0])
#     i=math.floor(n/2)
#     j=i
#     c=1
#     k=1
#     while k<n:
        
#         for x in range(k):
#             if k%2!=0:
#                 j+=1
#             else:
#                 j-=1
#             spinArray[i][j]=c
#             c+=1
#         for x in range(k):
#             if k%2!=0:
#                 i+=1
#             else:
#                 i-=1
#             spinArray[i][j]=c
#             c+=1    
#         k+=1
#     return spinArray
# print(createSpinArray(5))


n=1
step=2
somme=0
while n<1001**2:
    for x in range(4): 
        
        somme+=n
        n+=step
        
    step+=2
print(somme+1001**2)

