import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()

width = wn.window_width()

x1 = 0.0-(width-40)/3
x2 = 0.0
x3 = 0.0+(width-40)/3

def drawTriangleAt(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    t1.rt(60)
    t1.fd(size)
    for i in range(2):
        t1.rt(120)
        t1.fd(size)

def drawPentagon(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    t1.fd(size)
    for i in range(4):
        t1.rt(72)
        t1.fd(size)

def drawStarAt(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    for i in range(5):
        t1.forward(size)
        t1.right(144)

drawTriangleAt(100,x1)
drawPentagon(100,x2)
drawStarAt(100,x3)

wn.exitonclick()

