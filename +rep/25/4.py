def nah(n):
    for t in range(2,n):
        if n%t==0:
            return 0
    return 1

def bro(g):
    huh=[]
    for i in range(1,g+1):
        if g%i==0:
            huh.append(i)
    huh = sorted(set(huh))
    c=0
    for b in huh:
        if b%2==1:
            c+=1
    if c!=6:
        return 1337
    #return huh
    return [b for b in huh if b%2==1]

for u in range(95632, 95651):
    j = bro(u)
    if j!=1337:
        print(j)
