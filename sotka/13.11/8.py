import itertools
al=[x for x in "АКНРЭ"]
c=0
for k in itertools.product(al,repeat=6):
    a="".join(k)
    c+=1
    print(c,a)
