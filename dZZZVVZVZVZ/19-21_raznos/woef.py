def g(s,x):
    if s<=31 or x>2:
        return x==2 or x==4
    m = [g(s-2, x+1), g(s//3, x+1), g(s-5, x+1)]
    if x%2==0:
        return all(m)
    return any(m)

for s in range(23242):
    if g(s,0): print(s)
