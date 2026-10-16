for x in "0123456789ABCDE":
    for y in "0123456789ABCDE":
        a = int(f"90{x}4{y}",15)
        b = int(f"91{x}{y}2",16)
        if (b+a)%56==0:
            print((b+a)/56)
