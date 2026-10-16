f = open("7.lol", "r")
deez=[]
for s in f:
    deez.append(int(s.strip()))

nuts=deez.copy()
while True:
    if str(max(nuts))[-2:]=="29":
        maxel=max(nuts)
        break
    else:
        nuts.remove(max(nuts))

cd=0
maxi=-99999999
for h in range(len(deez)-2):
    a=deez[h]
    b=deez[h+1]
    c=deez[h+2]

    if ((abs(a)>=10000 and abs(a)<100000) + (abs(b)>=10000 and abs(b)<100000) + (abs(c)>=10000 and abs(c)<100000))==2 and a+b+c<=maxel:
        cd+=1
        maxi=max(maxi, a+b+c)

print(cd,maxi)
