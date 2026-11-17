f = open("9.lol").readlines()

for s in f:
    a = [int(x) for x in s.strip().split()]
    deez=[x for x in a if a.count(x)==1]
    if len(deez)==5 and 2*(max(deez)+min(deez))>(sum(deez)-max(deez)-min(deez)):
        print(sum(deez))
