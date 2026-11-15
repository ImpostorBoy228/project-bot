f = open("./9.dih","r").readlines()

deez=[]

for s in f:
    a = s.strip().split()
    deez.append(a)

c=0
for g in deez:
    a=[int(x) for x in g if g.count(x)!=1]
    b=[int(x) for x in g if g.count(x)==1]
    al=[int(x) for x in g]
    k=1
    for x in b:
        k*=x
    if len(a)==3 and len(b)==3 and max(al)**3>k:
        c+=1
print(c)
