# 19
def g(s,x):
    if s>=125 or x>2:
        return x==2
    m=[g(s+2, x+1), g(s+4, x+1), g(s*2, x+1)]
    if x%2 == 0:
        return all(m)
    return any(m)

for x in range(1,125):
    if g(x,0):
        print(x)

# 20
def g2(s,x):
    if s>=125 or x>2:
        return x==2
    if x==2: return False
    m=[g2(s+2, x+1), g2(s+4, x+1), g2(s*2, x+1)]
    if x%2 == 0:
        return all(m)
    return any(m)

for x in range(1,125):
    if g2(x,0) and not all(p<125 for p in [x+2,x+4, x*2]):
        print(x)

