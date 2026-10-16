from itertools import *

w= 'АЕКНТЦ'
c=1
for i in product(w,repeat=5):
    print(c,''.join(i))
    c+=1
