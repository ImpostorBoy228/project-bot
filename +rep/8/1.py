import itertools

a=['Е', 'Г', 'Э']
c=0
for i in list(itertools.product(a,repeat=5)):
    if i[0]=='Е' or i[0]=='Э':
        c+=1
print(c)
