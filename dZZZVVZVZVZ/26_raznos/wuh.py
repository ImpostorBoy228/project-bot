f = open("26var01.txt", "r").readlines()
n,m = f[0].strip().split()
n,m = int(n), int(m)
km = sorted([int(x) for x in f[1:n+1]])
sm = sorted([int(x) for x in f[n+1:]])
c=0
huh=0
dih=0
while not(len(km)==0 or len(sm)==0) :
    try:
        y=km[dih]
        u=sm[dih]
    except:
        break
    if y<=u:
        km.pop(dih)
        sm.pop(dih)
        c+=1
        huh=max(huh, y)
    else:
        dih+=1

print(c, huh)
