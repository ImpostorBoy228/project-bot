def f(n):
    s = bin(n)[2:]
    if n%2==0:
        s = "10"+s
    else:
        s = "1"+s+"01"
    return int(s,2)

ar=[]
for i in range(17,21412):
    a = f(i)
    ar.append(a)

print(min(ar))
