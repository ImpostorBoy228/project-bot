f = open("24var05.txt").readline().strip()
import re
ex= r"(?:0|[1234][01234]*)(?:[+-](?:0|[1234][01234]*))+"
print(max(map(len, re.findall(ex,f))))
