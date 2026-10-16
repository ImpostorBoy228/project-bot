import itertools
c=0
for i in itertools.product('АПРЕЛЬ',repeat=5):
    c+=1
    w=''.join(i)
    print(c,w)
