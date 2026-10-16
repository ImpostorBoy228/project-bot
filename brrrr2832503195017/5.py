def f(n):
    b = bin(n)[2:]
    if n%2==0:
        m = "11"+b+"11"
    else:
        m = "1"+b+"00"

    return int(m, 2)

a=[]
for i in range(94,909932):
    a.append(f(i))

a.sort()
print(a[0])
print(a[909932-94-1])


