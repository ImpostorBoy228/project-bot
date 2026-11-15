f = open("d","r").readlines()

deez=[]
for s in f:
    deez.append(s.strip().split())

c=0
for a in deez:
    j = [int(x) for x in a if a.count(x)==1]
    k= [int(x) for x in a if a.count(x)==2]
    if not( len(k)==4 and len(j)==2):
        continue
    if not sum(k)>sum(j):
        continue
    
    c+=1

print(c)

