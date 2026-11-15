f = open("./29979_B", "r").readlines()
from math import dist
d=[]
for s in f:
    a = [float(x) for x in s.strip().split()]
    d.append(a)

clusters=[]
while d:
    y=d[0]
    clus=[]
    for u in d[:]:
        if dist(u,y)<10:
            clus.append(u)
            d.remove(u)
    clusters.append(clus)

print("кластеров", len(clusters))
for t in clusters:
    print(len(t))
