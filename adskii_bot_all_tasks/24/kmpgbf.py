import re
f = open("24_17878.txt").readline().strip()
num = r"(?:0|[6789][06789]*)"
ex = rf"{num}(?:[-*]{num})+"

r = re.findall(ex, f)
print(max(map(len,r)))
