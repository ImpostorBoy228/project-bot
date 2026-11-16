f = open("26_67_sigma.txt", "r").readlines()
cap=13*3600+59*60+59
n,k=f[0].strip().split()
n,k=int(n), int(k)
d=[]
for u in f:
    a=u.strip().split()
    if u==f[0]:
        continue
    d.append([a[0], int(a[1]), int(a[2])])

a=[]
for b in d:
    a.append(b[1])

a=set(a)
b=[]

for h in a:
    acc=0
    for j in d:
        if j[1]==h:
            acc+=j[2]
    b.append([h, acc])

print(max(b, key=lambda x: x[1]))

dih=0
rc=[]
for n in d:
    if dih+n[2]<=k:
        dih+=n[2]
    else:
        time = [int(x) for x in n[0].split(":")]
        sec=time[0]*3600+time[1]*60+time[2]
        if sec<=cap:
            rc.append(dih)
        dih=0

print(sorted(rc))
