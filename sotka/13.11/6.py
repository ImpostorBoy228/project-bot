from turtle import *

tracer(0)
screensize(2000,2000)
m=10
down()
for _ in range(3):
    fd(44*m)
    lt(270)
    back(33*m)
    rt(90)

up()

fd(30*m)
rt(90)
back(7*m)
lt(90)
down()

for _ in range(3):
    fd(19*m)
    rt(90)
    fd(14*m)
    rt(90)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3)

done()
