def g(s,x):
    if s<=30 or x>3:
        return x==2
    m=[g(s-3,x+1), g(s-5, x+1), g(s//4, x+1)]
    if x%2==0:
        return all(m)
    return any(m)
for s in range(31,666):
    if g(s,0): print(s)
