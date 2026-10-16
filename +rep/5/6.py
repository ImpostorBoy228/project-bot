def f(n):
    s = bin(n)[2:]
    if n%3==0:
        s = s+s[-3]+s[-2]+s[-1]
    else:
        s = s+bin(n%3 * 3)[2:]
    return int(s,2)

nuts=0
for i in range(4,666):
    o=f(i)
    if o<=137:
        nuts=max(nuts, o)

print(nuts)
