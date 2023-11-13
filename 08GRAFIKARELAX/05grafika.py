import turtle
s = turtle.Screen()
t = turtle.Turtle()

t.speed(0)
t.color('red')
t.penup()
t.goto(0, -100)
t.pendown()
colors=['Blue', 'Brown', 'Chartreuse', 'DarkViolet', 'HotPink', 'Orange', 'Green']

for j in range(20,3):
    t.fillcolor(colors[j%7])
    t.begin_fill()
    for i in range(j):
        t.lt(360/j)
        t.fd(100)
    t.end_fill()



s.exitonclick()