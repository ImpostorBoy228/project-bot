def f(n):
    s=bin(n)[2:]
    if n%2==0:
        s="11"+s+"11"
    else:
        s="1"+s+"00"
    return int(s,2)

ma=0
for i in range(234234):
    if f(i)<=113:
        ma=max(ma, f(i))
print(ma)
