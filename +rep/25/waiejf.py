def nat(n):
    for t in range(2,n):
        if n%t==0:
            return 0
    return 1

def m(n):
    f=[]
    for u in range(2,n):
        if not n%u:
            f.append(u)
    for d in f:
        if not nat(d):
            f.remove(d)
    if len(f)==0:
        return 0
    return max(f)+min(f)

for l in range(452022, 8347209845):
    t = m(l)
    if t%7==3:
        print(l,t)
