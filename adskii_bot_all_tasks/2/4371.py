print("a b c d")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                bro = x<=(w and y or z and (not w))
                if not bro:
                    print(w,x,y,z)
