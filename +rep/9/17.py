f = open("17.lol", "r").readlines()
c=0
for s in f:
    qw=[int(x) for x in s.split()]
    da=[]
    ne=[]
    for i in qw:
        if qw.count(i)==1:
            da.append(i)
        else:
            ne.append(i)
    alll=da+ne
    alll.sort()
    blll=da+ne
    blll.sort()
    alll.pop(0)
    alll.pop(-1)
    if len(da)==5 and ((3*(min(blll)+max(blll)))<=(2*(sum(alll)))):
        c+=1

print(c)
