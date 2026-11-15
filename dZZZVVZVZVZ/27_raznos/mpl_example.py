import matplotlib.pyplot as plt
import numpy as np
from math import dist

f = open("./271A.txt").readlines()
d=[]
for s in f:
    a = s.strip().split()
    d.append([float(a[0]), float(a[1])])

fig, ax = plt.subplots()
x,y = zip(*d)
ax.scatter(x,y,color="crimson", s=60)
fig.savefig("out.png", dpi=300, bbox_inches="tight")
