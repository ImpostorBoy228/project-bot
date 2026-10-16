f = open("15.lol", "r").readlines()
c=0
for s in f:
    a = [int(g) for g in s.split()]
    ne=[]
    da=[]
    for i in a:
        if a.count(i)==2:
            da.append(i)
        if a.count(i)==1:
            ne.append(i)
    if len(ne)==2 and len(da)==4 and (sum(da)/2)<sum(ne):
        c+=1
print(c)

