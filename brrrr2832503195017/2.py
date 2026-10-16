c=0
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                c+=1
                
                f = ((x == (not y))<=((not (w<=x))) and (not z))
                if f!=False: continue
                print(f"{c} : {w,x,y,z} == {f}")
