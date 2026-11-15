from turtle import *

screensize(2000, 2000)
m=20
tracer(0)

for _ in range(6):
    fd(17*m)
    rt(90)
    fd(26*m)
    rt(90)

up()

fd(3*m)
rt(90)
fd(9*m)
lt(90)

down()

for _ in range(6):
    fd(55*m)
    rt(90)
    fd(67*m)
    rt(90)

up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*m,y*m)
        dot(3)

done()
