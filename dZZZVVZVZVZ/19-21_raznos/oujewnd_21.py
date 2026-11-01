def g(s,x):
    if s>=61 or x>2:
        return x==2 or x==4
    m = [g(s+1, x+1), g(s*4, x+1)]
    if x%2==0:
        return all(m)
    return any(m)
    
for s in range(1,58):
    if g(s,0):
        print(s)
