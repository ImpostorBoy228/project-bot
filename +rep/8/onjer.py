a = ["А", "Е", "Л", "Р", "С", "Т"] 
c=0
import itertools
for i in itertools.product(a, repeat=5):
    j = ''.join(i)
    c+=1
    if j.count("Л")==2 and j.count("ЛЛ")==0 and i[0] not in "АСТ" and c%2==0:
        print(c, i)


