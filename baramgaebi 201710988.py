import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()

def giyuk(size):
    i=1
    while i<10:
        t1.fd(size)
        t1.rt(90)
        t1.fd(size)
        t1.penup()
        t1.home()
        t1.setheading(40*i)
        t1.pendown()
        i=i+1

giyuk(100)

