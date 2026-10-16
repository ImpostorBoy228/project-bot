f = open("14.lol", "r")

yapping = list(map(int,f.read().split()))
c=0
# print(yapping)
for i in range(0, len(yapping),6):
    hell=[]
    for a in range(0, 6):
        hell.append(yapping[i+a])
    hell.sort()
    twice=[]
    last=hell[0]
    for k in range(1, 6):
        if last == hell[k]:
            twice.append(hell[k])
            twice.append(last)
        last=hell[k]
    ok1=False
    if len(twice)==2:
        ok1=True

    ok2=False
    sr=(sum(hell)-sum(twice))/4
    if sr<=sum(twice):
        ok2=True

    if ok1 and ok2:
        c+=1

print(c)
