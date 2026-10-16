def f(n):
    s=bin(n)[2:]
    o=s.count("1")%2
    s = s+str(o)
    o=s.count("1")%2
    s=s+str(o)
    return int(s,2)
a=[]
for i in range(23432):
    g=f(i)
    if g>253:
        a.append(i)
a.sort()
print(a)
