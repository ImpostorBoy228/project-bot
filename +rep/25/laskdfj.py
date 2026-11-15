import math
def bro(g):
    frac=[]
    for i in range(1,round(math.sqrt(g))+1):
        if g%i==0:
            frac.append(i)

    frac = set(frac)
    return [g/x - x for x in frac]

for r in range(2_000_000, 3_000_001):
    y=bro(r)
    if y==1337:
        continue
    u = [x<=115 for x in y]
    if u.count(1)>=3:
        print(r)
