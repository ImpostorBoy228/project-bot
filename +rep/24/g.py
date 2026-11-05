f = open("24_8", "r").readline()

g=[x for x in "AO"]

d=[]
for t in f:
    d.append(t)

c=0
m=0
i=0
while i < len(d):
    if i==0:
        i+=1
        continue
    if i==1:
        i+=2
        continue
    if d[i-2] in g and d[i-1] in g and d[i] not in g:
        c+=1
        i+=3
        m=max(m,c)
    else:
        c=0
        i+=1

print(m)
