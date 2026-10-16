def g(s,x):
    if x<0:
        return False
    if s>=29:
        return True
    m=[g(s+1,x-1),g(s*2,x-1)]
    if x%2==0:
        return all(m)
    else:
        return any(m)
        
# 19
for s in range(1,30):
    if g(s,1)!=True and g(s,2)==True:
        print(s) # 14

# 20
def g2(s,x):
    if x<0:
        return False
    if s>=29:
        return True
    m=[g(s+1,x-1),g(s*2,x-1)]
    if x%2==0:
        return any(m)
    else:
        return all(m)

for s in range(1,30):
    if g(s,1)!=True and g2(s,3)==True:
        print(s)

