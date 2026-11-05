def g(s,x):
    if s>=313 or x>3:
        return x==3
    m = [g(s*2,x+1), g(s+2, x+1), g(s+3, x+1)]
    if x%2==0:
        return any(m)
    return all(m)

for t in range(1,313):
    if g(t,0):
        print(t)
