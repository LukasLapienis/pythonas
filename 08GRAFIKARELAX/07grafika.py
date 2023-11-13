import turtle
s = turtle.Screen()
t = turtle.Turtle()

t.speed(0)
t.color('red')
t.penup()
t.goto(-200, 0)
t.pendown()
colors=['Blue', 'Brown', 'Chartreuse', 'DarkViolet', 'HotPink', 'Orange', 'Green']
t.pensize(5)
for j in range(1, 6):
    t.pencolor(colors[j%7])
    t.penup()
    t.fd(100)
    t.pendown()
    for i in range(4):
        t.lt(360/4)
        t.fd(50)
    

s.exitonclick()