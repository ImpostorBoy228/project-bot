f = open("31217.lol", "r").readlines()

c=0
for s in f:
    a = [int(x) for x in s.strip().split()]
    deez=[i for i in a if a.count(i)==2]
    nuts=[i for i in a if a.count(i)==1]
    if len(deez)==4 and len(nuts)==2:
        if sum(deez)>sum(nuts):
            c+=1

print(c)
