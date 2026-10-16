def p(n):
    res=''
    while n>0:
        res=str(n%5)+res
        n//=5
    return res

ma=0

for y in range(1001):
    u=5**50-y
    o=p(u)
    if o.count("4")==47:
        ma=max(ma,y)
print(ma)
