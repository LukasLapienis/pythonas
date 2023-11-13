import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.speed(8) # 3 greitesnis, 5 normalus, 10 greitas, 0 greiciausias
t.color('blue')
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
for i in range(4):
    t.fd(100)
    t.rt(90)

t.color('red')
for i in range(5):
    t.fd(100)
    t.rt(72)

t.color('green')
for i in range(5):
    t.lt(72)
    t.fd(100)

t.clear()
t.circle(60)

t.dot(30)


s.exitonclick()