for a in range(324):
    n=True
    for x in range(1,345):
        k = ((72%x==0)<=(not (90%x==0))) or ((a-x)>80)
        if not k:
            n=False
            break
    if n==True:
        print(a)
