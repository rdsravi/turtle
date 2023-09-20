import turtle

def draw_red_rose(t):
    t.color("red")
    for i in range(36):
        t.left(10)
        for j in range(9):
            t.forward(100)
            t.right(160)

t = turtle.Turtle()
draw_red_rose(t)
turtle.done()