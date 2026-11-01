f = open("24_1.lol", "r").readline()
c=0
m=0
for s in range(len(f)-1):
    if f[s]!=f[s+1]:
        c+=1
        m=max(m,c)
    else:
        c=0
print(m)

