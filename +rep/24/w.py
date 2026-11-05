f = open("24_6.txt", "r").readline()

d=[]
for t in f:
    d.append(t)

c=0
m=0
for u in range(len(d)-1):
    c+=1
    m=max(c,m)
    if d[u] == 'P' and d[u+1] == 'P':
        c=0

print(m)
