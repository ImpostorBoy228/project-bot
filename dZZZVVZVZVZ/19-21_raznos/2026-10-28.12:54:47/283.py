# 19
def mo(s):
    return [s-3,s-5,s//4]

for s in range(1,232352):
    xp=mo(s)
    wp = [x<=71 for x in xp]
    wv = [any(u<=71 for u in mo(x)) for x in xp]

    #if not any(wp) and all(wv):
    #    print(s)
    #    break
# 20
    wp2 = []
    for x in xp:
        u=mo(x)
        o=True # all
        for j in u:
            k = mo(j)
            m=False # any
            for t in k:
                if t<=71:
                    m=True
            if not m:
                o=False
        wp2.append(o)
    #if not any(wp) and any(wp2):
    #    print(s)
# 21

# p     не выигрывает
# v     может, но не гарантированно
# p2    любой
# v2    выигрывает гарантированно
    

