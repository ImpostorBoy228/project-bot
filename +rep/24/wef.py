f = open("./75", "r").readline()

s=[]
for t in range(len(f)-1):
    if f[t]+f[t+1]=="BC":
        s.append(t)
        
rust=[]
for u in range(len(s)-1):
    rust.append(s[u+1]-s[u])

ma=0
for y in range(len(rust)):
    x=sum(rust[y:y+191])
    ma=max(ma,x)

print(ma)
