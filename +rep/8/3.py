import itertools
c=0
for i in list(itertools.product(["Л","Е","В","И","Й"], repeat=5)):
    a=True
    if i[0]=="Й": continue
    for u in range(4):
        if i[u]+i[u+1]=="ЕИ": a=False
    for s in i:
        if not i.count(s)==1:
            a=False
    if a:
        c+=1
print(c)
