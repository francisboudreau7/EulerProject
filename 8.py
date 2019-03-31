import math
found=True
for x in range(1000):
    for y in range (1000):
        z=math.sqrt(x*x+y*y)
        if z==math.floor(z):
            if x+y+z==1000:
                print(x*y*z)
                