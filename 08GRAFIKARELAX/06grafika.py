import turtle
s = turtle.Screen()
t = turtle.Turtle()

t.speed(0)
t.color('red')
t.penup()
t.goto(0, -300)
t.pendown()
colors=['Blue', 'Brown', 'Chartreuse', 'DarkViolet', 'HotPink', 'Orange', 'Green']
t.pensize(5)
for j in range(20, 2, -1):
    t.fillcolor(colors[j%7])
    t.pencolor(colors[(j+1)%7])
    t.begin_fill()
    for i in range(j):
        t.lt(360/j)
        t.fd(100)
    t.end_fill()



s.exitonclick()