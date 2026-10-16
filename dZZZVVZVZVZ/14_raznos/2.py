a=729**6 - 3**20 + 90
b=0
s=""
while a>b:
    s=str(a%9)+s
    a//=9
print(s.count("0"))
