import itertools
w='ВЕКОТЦ'
c=0
f=0
for i in itertools.product(w,repeat=6):
    lol = ''.join(i)
    if (c%2==1) and (lol not in "ВЕК") and lol.count("Т")==2 and lol.count("Ц"):
        f+=1
    c+=1

print(f)
