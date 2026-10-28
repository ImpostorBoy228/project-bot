import itertools

w = list("АВКМОС")
for j,i in enumerate(itertools.product(w, repeat=6), start=1):
    a = ''.join(i)
    if j%2 or a[0] in "АВК" and a.count("К")!=2: continue
    br=False
    for t in range(5):
        if a[t]=="К" and a[t+1]=="К":
            br=True
    if br: continue
    print(j,i)
