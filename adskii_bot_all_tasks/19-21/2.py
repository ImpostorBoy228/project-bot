def g(s,x,nah): # Vanya wins mf fr fr
    if s>=nah*4:
        return x%2==0
    m=[g(s+5,x+1,nah),g(s*3,x+1,nah)]
    if x%2==1:
        return any(m)
    else:
        return all(m)

c=0
for s in range(1,151):
    if s+5>=4*s or 3*s >= 4*s:
        continue
    f=True
    for t in [s+5,s*3]:
        if not (t+5>=4*s or t*3>=s*4):
            f=False
            break
    if f:
        c+=1
print(c) # grob
