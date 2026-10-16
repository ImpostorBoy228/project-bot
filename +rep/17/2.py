f = open("2.impo", "r")
op=[]
for l in f:
    op.append(int(l.strip()))
c=0
ma=0
for i in range(len(op)-1):
    su=op[i]+op[i+1]
    if op[i]%5==0 or op[i+1]%5==0:
        if su%7==0:
            c+=1
            ma=max(su,ma)

print(c,ma)
            
