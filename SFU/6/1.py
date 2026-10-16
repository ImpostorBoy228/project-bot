from turtle import *

screensize(2000,2000)
tracer(0)
lt(90)
down()
m = 50
for _ in range(2):
    fd(3*m)
    rt(90)
    fd(20*m)
    rt(90)
up()
back(8)
rt(90)
fd(9*m)
lt(90)
down()
for _ in range(2):
    fd(16*m)
    rt(90)
    fd(8*m)
    rt(90)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3)

done()
