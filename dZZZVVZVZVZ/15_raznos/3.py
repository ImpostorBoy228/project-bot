a = range(3,61)
b = [ j for j in range(2,177) if 177%j==0]
m=0
for y in range(2,12344):
    f=True
    c = [ x for x in range(2,y) if y%x==0]
    if not c: continue

    for x in range(1,12434):
        q = ( x in c ) <= ((x in a) and (not(x in b))) 
        if q ==False:
            f=False
    if f:
        m=max(m,y)

print(m)
