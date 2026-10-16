import itertools
c=0
for i in list(itertools.product(["С","Л","О","Н"], repeat=5)):
    if i.count("С")==1:
        c+=1

print(c)
