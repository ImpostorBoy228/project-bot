f = open("17.lol").readlines()

mi=234234
for u in range(len(f)):
    if int(f[u])%33==0 and int(f[u])>0:
        mi=min(mi,int(f[u]))

c=0
ma=0
for u in range(len(f)-1):
    a = int(f[u])
    b= int(f[u+1])
    if a!=b and abs(a-b)%mi==0:
        c+=1
        ma=max(ma, a+b)
print(c,ma)
