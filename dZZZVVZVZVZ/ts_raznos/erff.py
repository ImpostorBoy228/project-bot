f = open("27var01B.txt", "r").readlines()
import math
allp=[]
for s in f:
    a = s.strip().split()
    a = (float(a[0]), float(a[1]))
    allp.append(a)

clusters=[]
while allp:
    c=[x for x in allp if math.dist(x,allp[0]) < 5]
    h = list(set(c))
    for i in h:
        allp.remove(i)
    clusters.append(h)

mj=[]
for u in clusters:
    print("длина", len(u))

    mi=98902342342
    mik = ()
    for t in u:
        mi = min(mi, sum([math.dist(t, x) for x in u]))
        if mi == min(mi, sum([math.dist(t, x) for x in u])):
            mik = t

    mj.append(mik)

    if len(u) == min([len(x) for x in clusters if not len(x)==1]):
        a = sum([math.dist(x, mik) for x in u])/len(u)
        print("q1", a*10000)

    if len(u) == max([len(x) for x in clusters if not len(x)==1]):
            a = sum([math.dist(x, mik) for x in u])/len(u)
            print("q2", a*10000)
    print(mi)
