from turtle import *

screensize(2000,2000)
tracer(0)
lt(90)
down()
m=10

for _ in range(2):
    fd(21*m)
    rt(90)
    fd(27*m)
    rt(90)
up()
fd(9*m)
rt(90)
fd(10*m)
lt(90)
down()

for _ in range(2):
    fd(86*m)
    rt(90)
    fd(47*m)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3)

done()
