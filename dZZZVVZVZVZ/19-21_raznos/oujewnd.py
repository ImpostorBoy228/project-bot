def mo(n):
    return [n+1, n*4]

for s in range(1,58):
    pm = mo(s)
    pw = [x>=61 for x in pm]

    
    vm = [mo(x) for x in pm]
    vw=[]
    for f in vm:
        for j in f:
            vw.append(j>=61)
        
    if not all(pw) and any(vw):
        print(s)
