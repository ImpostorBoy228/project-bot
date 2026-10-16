def f(n):
    s=str(n)
    a = int(s[0]) + int(s[1])
    b = int(s[1]) + int(s[2])
    c = int(s[2]) + int(s[3])
    res = [a,b,c]
    res.sort()
    return int(str(res[0])+str(res[1]))

mi=999999999
for i in range(1000,10000):
    o = f(i)
    if o==1215:
        mi=min(mi,i)
print(mi)

