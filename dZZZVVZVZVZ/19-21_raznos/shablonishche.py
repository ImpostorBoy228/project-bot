# 19
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
# 20
def f(a, n):
    if a <= 60:
        return n == 2
    if n == 2:
        return False

    m = [f(a-3, n+1), f(a-5, n+1), f(a//4, n+1)]

    if n % 2 == 0:
        return any(m)
    return all(m)

for s in range(61, 300):
    if not any(x <= 60 for x in [s-3, s-5, s//4]) and f(s, 0):
        print(s)

# 21
def f(a, n):
    if a <= 60:
        return n % 2 == 0
    if n == 3:
        return False

    m = [f(a-3, n+1), f(a-5, n+1), f(a//4, n+1)]

    if n % 2 == 0:
        return all(m)
    return any(m)

for s in range(61, 300):
    if f(s, 0):
        print(s)
