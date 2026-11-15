f = open("9.lol", "r").readlines()
deez = []
for t in f:
    a=[int(z) for z in t.strip().split()]
    deez.append(a)

c=0
for y in deez:
    a=[x for x in y if y.count(x)==3]
    b=[x for x in y if y.count(x)==1]
    if len(a)==3 and len(b)==2 and sum(b)/2>min(a):
        c+=1

print(c)
