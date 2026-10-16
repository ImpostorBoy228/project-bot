from itertools import *

w='0123456'
c=0
for i in product(w,repeat=5):
    lol=''.join(i)
    if lol[0]!="0" and lol.count("0")==1 and lol.count("1")<3:
        c+=1
print(c)
