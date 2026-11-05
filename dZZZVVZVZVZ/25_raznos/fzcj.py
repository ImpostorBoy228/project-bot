def prime(n):
    fack=[]
    d=2
    while d**2<=n:
        while n%d==0:
            fack.append(d)
            n//=d
        d+=1
    if n>1:
        fack.append(n)
    if len(fack)!=2:
        return 0
    a,b=fack
    if "1" in str(a)+str(b) and "3" in  str(a)+str(b):
        return 0
    return max(fack)

for u in range(3000000, 22867365420):
    r = prime(u)
    if r!=0:
        print(u, r)
