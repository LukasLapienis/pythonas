import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.speed(8) # 3 greitesnis, 5 normalus, 10 greitas, 0 greiciausias
s.bgcolor('yellow')
s.title('Pirmas kartas')


for i in range(5):
    t.fd(100)
    t.rt(72)

t.penup()
t.goto(150 ,150)
t.pendown()
t.fillcolor('green')
t.pen(pencolor='red', fillcolor='silver', pensize=1, speed=2)
t.begin_fill()

#t.color('green')
for i in range(5):
    t.fd(100)
    t.rt(72)
t.end_fill()

s.exitonclick()