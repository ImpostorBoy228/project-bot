# 19
for s in range(61,400):
    pm=[s-3,s-5,s//4]
    pmm = [x<=60 for x in pm]
    pw=any(pmm) # петя может выиграть своим 1 ходом
    vm = [[x-3,x-5,x//4] for x in pm]
    vmm = [any(f<=60 for f in x) for x in vm]
    vanya_raznosit=any(vmm)
    if not pw and vanya_raznosit:
        print(s)
        break
# 20
print("="*20)
for s in range(61,400):
    # xp1
    pm=[s-3,s-5,s//4] # 3
    pmm = [x<=60 for x in pm]
    pw=any(pmm)
    
    # xv1
    vm = [[x-3,x-5,x//4] for x in pm] # 3x3
    vmm = [any(f<=60 for f in x) for x in vm]

    # xp2
    pm2=[[[t-3,t-5,t//4] for t in x] for x in vm] # 3x3x3
    pmm2 = [all([any([k<=60 for k in f]) for f in x]) for x in pm2]
    pw2 = all(pmm2)
    if not pw and pw2 and not vw: # не оставляем шансов ване
        print(s)
    vw=any(vmm) 
