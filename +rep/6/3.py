from turtle import *

screensize(2000,2000)
tracer(0)
m=40


down()
for _ in range(4):
    fd(6*m)
    rt(90)
    fd(6*m)
    lt(90)
    fd(6*m)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3)
done()
