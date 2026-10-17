ha=["А","Е","Л","Р","С","Т"]
import itertools
c=1
for i in itertools.product(ha,repeat=5):
    c+=1
    print(c, i)
