def nah(n):
    for t in range(2,n):
        if n%t==0:
            return 0
    return 1

def bro(g):
    huh=[]
    for i in range(2,g):
        if g%i==0:
            huh.append(i)
    huh = set(huh)
    #for b in huh:
    #    if not nah(b):
    #        return 1337
    if len(huh)!=4:
        return 1337
    return huh


for u in range(210235, 210301):
    j = bro(u)
    if j!=1337:
        print(j)
