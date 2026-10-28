f = open("17var03.txt", "r").readlines()
jeez=[]
for s in f:
    jeez.append(int(s.strip()))

mi=809809
for g in jeez:
    if str(g)[-3:]=="500":
        mi=min(mi, g)

c=0
mini=8032740
for i in range(len(jeez)-2):
    # tr = [jeez[i:i+3]]
    tr=[]
    for b in range(3):
        tr.append(jeez[i+b])
    br=False
    for f in tr:
        if not int(f)%2: br=True
    if sum(tr)>mi:
        br=True
    if br:
        continue
    c+=1
    mini=min(mini,sum(tr))

print(c, mini)
