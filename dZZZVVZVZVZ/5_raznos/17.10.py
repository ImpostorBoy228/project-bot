def f(n):
    s=bin(n)[2:]
    if n%3==0:
        s=s+s[-3:]
    else:
        s=s+bin((n%3+1)*3)[2:]

    return int(s,2)

g=0
for n in range(133713):
    r=f(n)
    if r<=416:
        g=max(g,r)

print(g)
