def tr(n):
    res=""
    while n>1:
        res = str(n%3) + res
        n//=3
    return res


def f(n):
    s = tr(n)
    rs=""
    if n%7==0:
        rs= "10"+s + s[-2:]
    else:
        rs = s+ tr(sum([int(x) for x in s])*3)

    return int(rs,3)

mi=23984234

for u in range(2,30000):
    k=f(u)
    if k>906 and k%2==1:
        mi=min(mi,k)

print(mi)
