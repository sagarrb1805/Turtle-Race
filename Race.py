import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

t1.color("black")
t2.color("blue")
t3.color("red")
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t1.penup()
t2.penup()
t3.penup()
t1.setpos((-200, -200))
t2.setpos((0, -200))
t3.setpos((200, -200))
t1.setheading(90)
t2.setheading(90)
t3.setheading(90)
turtle.Screen().exitonclick()
