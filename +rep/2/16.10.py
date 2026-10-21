print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = x<=(not((y<=z) and (z== (not w))))
                if f==0:
                    print(w,x,y,z)

