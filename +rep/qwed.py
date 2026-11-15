f = open("./24_11", "r").readline()
deez =[]
for u in f:
    deez.append(u)

state=""
dig=[x for x in "06789"]

m=0
c=0

s=0
while s < len(deez)-1:
    match state:
        case "left":
            while deez[s] == '0':
                s+=1

            if deez[s+1] in dig:
                c+=1
            else:
                state = "op"

        case "right":
            while deez[s] == '0':
                s+=1

            if deez[s+1] in dig:
                c+=1
            else:
                state = ""

        case "":
            while deez[s] not in dig:
                s+=1
            state="left"

        case "op": 
            if deez[s+1] not in dig:
                m=max(c,m)
                c=0
            else:
                c+=1
                state="right"
    s+=1

print(m)
