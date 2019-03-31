a=[1,2,5,10,20,50,100,200]
def f(n,k):
  if k<1 or n<0:
    return 0
  if n==0:
    return 1
  else:
    return (f(n,k-1)+ f(n-a[k-1],k))

print(f(200,8))  