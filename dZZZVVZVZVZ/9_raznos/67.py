f = open("03.lol", "r").readlines()

chef=0
for s in f:
    a = s.strip().split()
    deez = [int(x) for x in a if a.count(x)==2]
    nuts = [int(x) for x in a if a.count(x)==1]
    if len(deez)==4 and sum(deez)/2>=sum(nuts):
        chef=sum([int(x) for x in a])

print(chef)
