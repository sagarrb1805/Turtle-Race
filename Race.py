import turtle
import threading
import random

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


def t1_forward():
    t1.speed(random.uniform(1, 1.5))
    t1.forward(400)


def t2_forward():
    t2.speed(random.uniform(1, 1.5))
    t2.forward(400)


def t3_forward():
    t3.speed(random.uniform(1, 1.5))
    t3.forward(400)


thread1 = threading.Thread(target=t1_forward)
thread2 = threading.Thread(target=t2_forward)
thread3 = threading.Thread(target=t3_forward)
thread1.start()
thread2.start()
thread3.start()

turtle.Screen().exitonclick()
