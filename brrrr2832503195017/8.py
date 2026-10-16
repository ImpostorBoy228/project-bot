import itertools
w = itertools.product("АКЦЕНТ", repeat=5)
c=0
for i in w:
    word = ''.join(i)
    c+=1
    if c%2==1: continue
    if word[0] in "АЕК" or word.count("Т")==0: continue
    print(f"{c}       {word}")
