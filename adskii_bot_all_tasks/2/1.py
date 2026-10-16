print("u w x y z")
for u in range(2):    
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = ((z<=w) and (y== (not x)))<=(u==(y or z))
                    if f==False:
                        print(u,w,x,y,z)
