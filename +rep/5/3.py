def f(n) -> int:
    s = bin(n)[2:]
    t = [int(x) for x in s]
    rem = sum(t)%2
    g = s+str(rem)
    t = [int(x) for x in g]
    rem = sum(t)%2
    y = g+str(rem)
    return int(y,2)

jeez=99999
for i in range(99999):
    o = f(i)
    if o>97:
        jeez = min(jeez,o)


print(jeez)
    
