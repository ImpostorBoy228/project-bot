from turtle import *

screensize(2000,2000)
tracer(0)
m=20

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3)
goto(0,0)
down()
for _ in range(2):
    fd(9*m)
    rt(90)
    fd(5*m)
    rt(270)
back(18*m)
lt(90)
fd(10*m)
rt(90)
up()
fd(5*m)
rt(90)
fd(4*m)
lt(90)
down()
for _ in range(4):
    fd(5*m)
    rt(90)

done()
