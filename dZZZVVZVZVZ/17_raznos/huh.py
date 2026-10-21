f=open("fipi1","r").readlines()
deez = [int(s.strip()) for s in f]

nuts= [int(s.strip()) for s in f if abs(int(s.strip())) < 100]
ty=max(nuts)+min(nuts)

c=0
maxi=0
for u in range(len(deez)-2):
    one=[]
    a=[]
    for i in range(2):
        a.append(deez[u+i])
        if deez[u+i]<100:
            one.append(deez[u+i])
    maxi=max(maxi,sum(a))
    f=len(one)>=2 and sum(a)>ty
    if f: c+=1

print(c,maxi)
