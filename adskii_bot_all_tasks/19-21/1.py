def game(s,h):
    if s>=133:
        return h%2==0
    m = [game(s+4,h-1),game(s*2,h-1)]
    if h%2==0:
        return any(m)
    else:
        return all(m)

for i in range(1,200):
    if game(17,i):
        print(i)
