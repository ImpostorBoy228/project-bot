def g(s1,s2,x):
    if s1+s2>=133 or x>4:
        return x==4 or x==2
    m=[g(s1,s2+4,x+1), g(s1+4,s2,x+1), g(s1,s2*2,x+1), g(s1*2,s2,x+1)]
    if x%2==0:
        return all(m)
    return any(m)

for s in range(2532):
    if g(17,s,0):
        print(s)

# 19: 29
# 20: 28
# 21: 44
