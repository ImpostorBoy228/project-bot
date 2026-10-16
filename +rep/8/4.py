import itertools

c=0
jeez=[x for x in "01234567"]
for i in list(itertools.product(jeez, repeat=5)):
    if i[0]=='0': continue
    if i.count("1")!=0: continue
    k=True
    for a in i:
        if i.count(a)!=1:
            k=False
    if not all(int(i[x])%2!=int(i[x+1])%2 for x in range(4)): k=False


    if k: c+=1

print(c)
