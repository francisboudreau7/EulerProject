def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
max = 0

for i in range(1000):
    for j in range(1000):
    
        nb=(str(i*j))
        inverse = reverse(nb)
        if nb == inverse:
            nombre=i*j
             
            if nombre>max and nombre != 0:
                max=nombre

print max

