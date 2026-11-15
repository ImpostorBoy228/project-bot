def f(n):
    s=bin(n)[2:]
    if n%2==0:
        s="1"+s+"00"
    else:
        s=s+bin(sum([int(x) for x in s]))[2:]
    return int(s,2)

mi=242423424
for t in range(1,122331):
    r = f(t)
    if r>190:
        mi=min(t,mi)

print(mi)

print(f(16))
