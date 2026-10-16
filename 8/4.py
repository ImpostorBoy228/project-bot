import itertools
he=[]
s=36

def sh(n):
    a=n
    s=""
    while a>0:
        s=str(a%6)+s
        a=a//6
    return s


while(True):
    if len(sh(s))!=3: 
        break
    he.append(sh(s))
    s+=1

c=0
for i in he:
    if i[2]<=i[1] and i[1]<=i[0]:
        c+=1

print(c)
