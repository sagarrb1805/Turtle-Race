import threading
import turtle
import random


class Player(turtle.Turtle):
    def __init__(self, color, shape):
        turtle.Turtle.__init__(self)

    def color_shape(self, color, shape):
        self.color(color)
        self.shape(shape)

    def set_possition(self, x, y, head):
        self.x = x
        self.y = y
        self.head = head
        self.penup()
        self.setpos((self.x, self.y))
        self.pendown()
        self.setheading((self.head))

    def race(self):
        self.speed(random.uniform(1, 1.5))
        self.forward(400)


t1 = Player("red", "turtle")
t2 = Player("red", "turtle")
t3 = Player("red", "turtle")
t1.color_shape("black", "turtle")
t2.color_shape("red", "turtle")
t3.color_shape("green", "turtle")
t1.set_possition(-200, -200, 90)
t2.set_possition(0, -200, 90)
t3.set_possition(200, -200, 90)

thread1 = threading.Thread(target=t1.race)
thread2 = threading.Thread(target=t2.race)
thread3 = threading.Thread(target=t3.race)

thread1.start()
thread2.start()
thread3.start()

turtle.Screen().exitonclick()
