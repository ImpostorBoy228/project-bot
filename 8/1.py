import itertools
lt=['А','Г','М','Н','С','Т','У']
c=0
for i in itertools.product(lt,repeat=6):
    w=''.join(i)
    c+=1
    if w[0] not in "У" and w.count("Г")<2 and w.count("М")==2:
        print(c)
