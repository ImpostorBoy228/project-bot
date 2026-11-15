o = range(174457, 174506)
import math

def is_n(g):
    for u in range(2, g):
        if g%u==0:
            return 0
    return 1

def dl(n):
    dih = []
    for y in range(2, n):
        if n%y==0:
            dih.append(y)
    dih = set(dih)
    for e in dih:
        if not is_n(e):
            return 1337
    if len(dih)!=2:
        return 1337
    return dih

for t in o:
    j = dl(t)
    if j!=1337:
        k.append(j)

