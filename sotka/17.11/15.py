b=range(70,91)



for a in range(1,10934):
    k=1
    for x in range(1,14124):
        f = x%a==0 or ((x in b) <=( not (x%16==0)))
        if not f:
            k=0
            break

    if k:
        print(a)
