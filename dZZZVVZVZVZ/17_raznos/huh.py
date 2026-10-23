f=open("fipi1","r").readlines()
deez = [int(s.strip()) for s in f]

nuts= [int(s.strip()) for s in f if 9 < abs(int(s.strip())) < 100]
ty=max(nuts)+min(nuts)

c=0
maxi=0
for u in range(len(deez)-2):
    one=[]
    a=[]
    for i in range(0,3):
        a.append(deez[u+i])
        if 9 < abs(deez[u+i]) < 100:
            one.append(deez[u+i])
    f=len(one)>=2 and sum(a)>ty
    if f: 
        c+=1
        maxi=max(maxi,sum(a))

print(c,maxi)
