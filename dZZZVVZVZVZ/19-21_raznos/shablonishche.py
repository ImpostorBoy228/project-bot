def f(a,n):
    if a <=60 or n > 3:
        return n == 3
    m=[f(a-3, n+1),f(a-5, n+1),f(a//4, n+1)]
    if n % 2 == 0:
        return any(m)
    return all(m)

for s in range(61, 300):
    if f(s,0):
        print(s)
