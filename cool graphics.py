from turtle import *


bgcolor("black")
speed(0)
hideturtle()
for i in range(36):
    color("red")
    circle(i * 2)
    color("orange")
    circle(i* 4)
    color("yellow")
    circle(i* 6)
    color("green")
    circle(i* 8)
    color("blue")
    circle(i* 10)
    color("indigo")
    circle(i* 11)
    color("violet")
    circle(i* 12)
    right(10)
    forward(3)
done()
