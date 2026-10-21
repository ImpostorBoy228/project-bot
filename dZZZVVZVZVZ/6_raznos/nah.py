from turtle import *

tracer(0)
screensize(2000,2000)
m=20
down()
for _ in range(4):
    fd(9*m)
    lt(180)
    back(10*m)
    rt(90)

up()
back(m*7)
lt(90)
fd(3*m)
rt(90)
down()
for _ in range(2):
    fd(17*m)
    lt(90)
    fd(20*m)
    lt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3)

done()
