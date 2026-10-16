from turtle import *

screensize(2000,2000)
tracer(0)
rt(315)
down()
m=20
for _ in range(7):
    fd(12*m)
    rt(45)
    fd(6*m)
    rt(135)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3)
done()
