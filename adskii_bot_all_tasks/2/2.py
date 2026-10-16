print("w,x,y,z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (w==(not (z==y))) and (z==(y<=x))
                if f:
                    print(w,x,y,z)

