import turtle
s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor('yellow')
t.speed(0)
t.color('red')
t.penup()
t.goto(-200, 0)
t.pendown()
colors=['Blue', 'Brown', 'Chartreuse', 'DarkViolet', 'HotPink', 'Orange', 'Green']
t.pensize(5)
t.pencolor('black')
for j in range(1, 7):
    t.fillcolor(colors[j%7])
    t.begin_fill()
    for i in range(6):
        t.fd(50)
        t.lt(360/6)
    t.end_fill()
    t.penup()
    t.lt(360/6)
    t.fd(100)
    t.pendown()

    
    

s.exitonclick()