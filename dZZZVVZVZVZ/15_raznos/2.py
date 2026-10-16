def tre(a,b,c):
    if (a+b)>c and (a+c)>b and (b+c)>a:
        return True
    else:
        return False
k=[]
for i in range(6666):
    for x in range(6666):
        f = not((tre(x,11,16)==(not(max(x,5)>10))) and tre(4,i,x))
        k.append(f)
    k.sort()
    if k[0]==1:
        print(i)
    k=[]
        
