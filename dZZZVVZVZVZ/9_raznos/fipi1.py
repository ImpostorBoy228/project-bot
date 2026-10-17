f = open("9var01.csv", "r").readlines()
c=0
for s in f:
    a=s.strip().split()
    deez=[int(x) for x in a if a.count(x)==1]
    nuts=[int(x) for x in a if a.count(x)==3]
    if len(nuts)==3 and len(deez)==4 and sum(deez)>sum(nuts):
        c+=1

print(c)
