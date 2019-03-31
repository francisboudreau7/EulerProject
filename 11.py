import math
import functools
grid="08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748"
realgrid=[[],[],[],[],[],[],[]]
for x in range(0,len(grid),2):
    j=int(math.floor(x/40))
    if len(realgrid)<=j:
        realgrid.insert(30,[])
        if j>20:break
    realgrid[j].insert(30,int(grid[x]+grid[x+1]))



def vertical(grd):
    max=0
    produit=1
    for i in range(17):
        for j in range(20):
            produit=1
            for x in range(4):
                produit*=grd[i+x][j]
            if produit>max : max=produit
    return max

print(vertical(realgrid))

def horizontal(grd):
    max=0
    produit=1
    for i in range(20):
        for j in range(17):
            produit=1
            for x in range(4):
                produit*=grd[i][j+x]
            if produit>max : max=produit
    return max

print(horizontal(realgrid))
def diagonalA(grd):
    max=0
    produit=1
    for i in range(17):
        for j in range(17):
            produit=1
            for x in range(4):
                produit*=grd[i+x][j+x]
            if produit>max : max=produit
    return max

def diagonalB(grd):
    max=0
    produit=1
    for i in range(17):
        for j in range(3,17):
            produit=1
            for x in range(4):
                produit*=grd[i+x][j-x]
            if produit>max : max=produit
    return max
print(diagonalB(realgrid))