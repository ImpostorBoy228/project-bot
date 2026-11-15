from turtle import *

screensize(2000,2000)
tracer(0)
m=20
down()

for _ in range(2):
    fd(m*28)
    rt(90)
    fd(18*m)
    rt(90)

up()
fd(m*14)
rt(90)
fd(10*m)
lt(90)
down()

for _ in range(2):
    fd(30*m)
    rt(90)
    fd(m*7)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3)
done()
