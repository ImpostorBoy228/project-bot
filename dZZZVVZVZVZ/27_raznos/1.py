from math import dist

f = open("./271B.txt").readlines()
d=[]
for s in f:
    a = s.strip().split()
    d.append([float(a[0]), float(a[1])])

c1=[u for u in d if u[1]>14]
c2=[u for u in d if 14>u[1]>10]
c3=[u for u in d if 9>u[1]>5]
c4=[u for u in d if u[1]<4 and u[0]<10]
c5=[u for u in d if u[0]>12]
clusters=[c1,c2,c3,c4,c5]
centroids=[]

def ce(c):
    b=20943049
    res=0
    for u in c:
        b = min(b, sum([dist(u,p) for p in c]))
        if b==sum([dist(u,p) for p in c]):
            res=u
    return res

sry=0
srx=0
for k in clusters:
    sry+=ce(k)[1]
    srx+=ce(k)[0]
sry/=5
srx/=5

print([len(s) for s in clusters], srx*10000,sry*10000)
