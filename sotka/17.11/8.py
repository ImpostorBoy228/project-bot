al="АЕКНТЦ"
import itertools
c=0
for u in itertools.product(al, repeat=5):
    c+=1
    print(c,u)
