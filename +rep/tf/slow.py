from string import printable


f = open("24_5.txt").readlines()

lma=0
for s in f:
    if s.count('A') >= 25: continue
    c=0
    for j in printable:
        lma = max(lma, s.rfind(j) - s.find(j))

print(lma)
