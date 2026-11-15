al = [x for x in sorted("АБЕИЛРТФЦ")]
import itertools
c=0
for i in itertools.product(al, repeat=5):
    c+=1
    a = "".join(i)
    if c%2!=0:
        if a[0] in "РТЕ" or a.count("И")<2:
            continue

        print(c, a)
