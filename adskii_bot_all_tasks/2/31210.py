print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                bro = ((y<=w)<=x) or (not z)
                if not bro:
                    print(w,x,y,z)
