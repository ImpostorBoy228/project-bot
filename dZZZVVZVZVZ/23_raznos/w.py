def f(n: int, y: int) -> int:
    if y == 1:
        return n+1
    if y == 2:
        if int(str(n)[1])<int(str(n)[2]):
            return int(f"{str(n)[0]}{str(n)[2]}{str(n)[1]}")
        else:
            return -1

w=""
# for i in range(1606938044258990275541962092341162602522202993782792835301375):
#     b = bin(i)[2:]
#     b.replace("1","2")
#     b.replace("0","1")
#     w.append(b)

c=[]
# for u in w: # w - список строк типа 12221211121212
u="11"
while len(u)<=200:
    num: int=101
    deep = 0
    for j in u: # прогон f() на последовательности команд
        deep+=1
        k=int(j)
        h: int = f(num, k)
        if h == -1:
            break
        num = h
        if h==154: 
            c.append(u[:deep])
            break

    if u[-1]=="1":
        u=u[:-1]+"2"
    elif u[-1]=="2":
        u=u+"1"

u="2"
while len(u)<=200:
    num: int=101
    deep = 0
    for j in u: # прогон f() на последовательности команд
        deep+=1
        k=int(j)
        h: int = f(num, k)
        if h == -1:
            break
        num = h
        if h==154: 
            c.append(u[:deep])
            break

    if u[-1]=="1":
        u=u[:-1]+"2"
    elif u[-1]=="2":
        u=u+"1"

print(len(set(c)))
