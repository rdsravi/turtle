import turtle

def draw_petal(t):
    for i in range(2):
        t.forward(30)
        t.left(45)
        t.forward(30)
        t.left(135)

def draw_red_rose(t):
    t.color("red")
    for i in range(36):
        draw_petal(t)
        t.left(10)

t = turtle.Turtle()
draw_red_rose(t)
t.right(90)
t.forward(150)
t.right(90)
t.forward(50)
t.color("green")
t.begin_fill()
t.circle(20)
t.end_fill()
turtle.done()