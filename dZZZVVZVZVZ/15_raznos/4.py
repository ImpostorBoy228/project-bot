for a in range(1,1000):
    fl = True
    for x in range(1,1000):
        for y in range(1,1000):
            f = (105!=(y+2*x)) or (a>x) or (a>y)
            if not f:
                fl=False
    if fl: print(a)
