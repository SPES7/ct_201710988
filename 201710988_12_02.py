import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()

width = wn.window_width()

x1 = 0.0-(width-40)/3
x2 = 0.0
x3 = 0.0+(width-40)/3

def drawSquareAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for i in range(4):
        t1.fd(size)
        t1.rt(90)
        
def drawTriangleAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for i in range(3):
        t1.fd(size)
        t1.rt(120)

def drawStarAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for i in range(5):
        t1.fd(size)
        t1.rt(144)
        
drawSquareAt(x1,0,100)
drawTriangleAt(x2,0,100)
drawStarAt(x3,0,100)

wn.exitonclick()


