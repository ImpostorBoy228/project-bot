a=2*(2187**567)+(729**566)-2*(243**565)+(81**564)-2*(27**563)-6561

def ts(n):
    al='0123456789ABCDEFGHIJKLMNOPQ'
    r=''
    while n>0:
        r=al[n%27]+r
        n//=27
    return r

c=0
for i in ts(a):
    if i not in "1234567890":
        c+=1

print(ts(a))
print(c)
