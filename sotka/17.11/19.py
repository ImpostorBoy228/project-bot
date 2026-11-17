def g(s1,s2,x):
    if s1+s2>=115 or x>4:
        return x==2 or x==4
    m=[g(s1+1, s2, x+1), g(s1,s2+1, x+1), g(s1*3,s2,x+1), g(s1,s2*3,x+1)]
    if x%2==0:
        return all(m)
    return any(m)

for s in range(1, 199):
    if g(15,s,0):
        print(s)
