def g(n):
    s = bin(n)[2:]
    if n%2==0:
        res = "11"+s+"11" 

    else:
        res = "1"+s+"00" 
    return int(res,2)

ma=0
for x in range(6666):
    if g(x)<=416:
        ma=max(ma,g(x))

print(ma)
