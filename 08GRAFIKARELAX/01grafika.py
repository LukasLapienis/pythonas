import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.speed(1) # 3 greitesnis, 5 normalus, 10 greitas, 0 greiciausias
t.right(90) #t.rt(90)
t.forward(100) #t.fd(90)
t.left(90) #t.lt(90)
t.backward(100) #t.bd(100)
t.home()
t.goto(200,250)
t.clear()

s.exitonclick()