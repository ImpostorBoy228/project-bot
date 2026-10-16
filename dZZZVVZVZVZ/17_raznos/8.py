f = open("8.lol", "r")

deez=[]
for s in f:
    deez.append(int(s.strip()))

nuts=deez.copy()
while True:
    if max(nuts)%100==17:
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
    skibidi=any([a%5==0,b%5==0,c%5==0])

    if (1000 <= a <= 9999) + (1000 <= b <= 9999) + (1000 <= c <= 9999) == 2 and a+b+c>maxel and skibidi:
        cd+=1
        maxi=max(maxi, a+b+c)

print(cd,maxi)
