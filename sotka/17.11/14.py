def pt(n):
    rs=""
    while n>1:
        rs=str(n%5)+rs
        n//=5
    return rs

ma=0
for t in range(1,2031):
    a = pt(5**150+5**100-t)
    ma=max(ma, a.count("0"))
    if ma == a.count("0"):
        print(t,ma)
