import turtle
import math

def heart_curve(t, size):
    for i in range(360):
        angle = math.radians(i)
        x = 16 * math.sin(angle)**3
        y = 13 * math.cos(angle) - 5 * math.cos(2*angle) - 2*math.cos(3*angle) - math.cos(4*angle)
        t.goto(x*size, y*size)

def animate_heart(t, size, speed):
    t.color("red")
    t.pensize(3)
    for i in range(20):
        heart_curve(t, size+i/2)
        t.left(18)
        t.speed(speed)

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
animate_heart(t, 10, 20)
turtle.done()
