import turtle

# Create a function that draws a petal
def draw_petal(t):
    for i in range(2):
        t.forward(30)
        t.left(45)
        t.forward(30)
        t.left(135)

def draw_flower(t, size):
    t.color("red")
    for i in range(36):
        draw_petal(t)
        t.left(10)
        t.forward(size)

# Create a turtle object
t = turtle.Turtle()

# Draw the flower
draw_flower(t, 30)

# Move the turtle to the center of the flower and draw the stem
t.penup()
t.goto(0, -100)
t.pendown()
t.color("green")
t.pensize(3)
t.forward(200)

# Keep the turtle window open until the user closes it
turtle.done()
