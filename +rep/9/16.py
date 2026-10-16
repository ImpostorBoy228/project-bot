f = open("16.lol", "r").readlines()
c=0
for s in f:
    p = [int(d) for d in s.split()]
    da=[]
    ne=[]

    odd=[]
    even=[]
    for i in p:
        if i%2!=0:
            odd.append(i)
        else:
            even.append(i)
        if p.count(i)>1:
            ne.append(i)
        else:
            da.append(i)
    if len(ne)==0 and len(odd)>len(even) and sum(odd)<sum(even):
        c+=1

print(c)
