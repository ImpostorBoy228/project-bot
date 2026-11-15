import itertools
al = [x for x in "ДРСЩЭ"]

c=0
for t in itertools.product(al,repeat=4):
    c+=1
    a="".join(t)
    print(c, a)

