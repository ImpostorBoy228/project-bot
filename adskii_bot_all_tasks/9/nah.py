f = open("./nah.lol", "r").readlines()

d=[]
for t in f:
    d.append([int(x) for x in t.strip().split()])
c=0
for u in d:
    c+=1
    deez=[x for x in u if u.count(x)==1]
    nuts=[x for x in u if u.count(x)==3]

    if ( len(deez)==4 and len(nuts)==3 ) and (2*(max(u)+min(u)))>=(sum(u)-max(u)-min(u)):
        print(c)
