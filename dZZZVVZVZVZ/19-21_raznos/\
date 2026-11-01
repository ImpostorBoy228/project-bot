def f(s,x):
    if s >= 61 or x > 3:
        return x == 3
    m=[f(s+1, x+1),f(s*4, x+1)]
    if x % 2 == 0:
        return any(m)
    return any(m)

for s in range(61, 300):
    if f(s,0):
        print(s)
