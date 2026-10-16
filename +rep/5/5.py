def f(n):
    s = bin(n)[2:]
    if n%2==0:
        s="10"+s
    else:
        s="1"+s+"01"
    return int(s,2)

ko=999999
for i in range(1337):
    o=f(i)
    if o >441:
        ko=min(ko,i)

print(ko)
