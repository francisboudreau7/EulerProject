def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
somme=0
for i in range(len(str(fact(100)))):
    somme+=int(str(fact(100))[i])
print(somme)