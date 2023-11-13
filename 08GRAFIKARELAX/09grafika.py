import turtle
s = turtle.Screen()
t = turtle.Turtle()

def langas():
    for i in range(4):
        t.fd(50)
        t.rt(90)
    t.lt(90)
    t.fd(20)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(20)
    t.backward(20)
    t.lt(90)
    t.fd(25)
    t.rt(90)
    t.fd(20)
    t.rt(90)
    t.fd(50)
    t.lt(180)

t.penup()
t.goto(-300, 250)
t.pendown()
t.speed(0)
for i in range(2):
    t.fd(500)
    t.rt(90)
    t.fd(550)
    t.rt(90)

t.penup()
t.goto(-325, 200)
t.pendown()
t.speed(0)

for i in range(5):
    for j in range(6):
        t.penup()
        t.fd(70)
        t.pendown()
        langas()
    t.penup()
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(420)
    t.lt(180)
    t.pendown()



s.exitonclick()