import threading
import turtle
import random
import time


class Player(turtle.Turtle):
    def __init__(self, color, shape):
        turtle.Turtle.__init__(self)
        self.speed_of_turtle = random.uniform(1, 1.5)
        self.color(color)
        self.shape(shape)

    def set_position(self, x, y, head):
        self.x = x
        self.y = y
        self.head = head
        self.penup()
        self.setpos((self.x, self.y))
        self.pendown()
        self.setheading(self.head)

    def race(self):
        self.speed(self.speed_of_turtle)
        self.forward(400)


t1 = Player("purple", "turtle")
t2 = Player("red", "turtle")
t3 = Player("green", "turtle")

t1.set_position(-300, -200, 90)
t2.set_position(0, -200, 90)
t3.set_position(300, -200, 90)

turtle.write(arg="Press up key", move=True, align="center",
             font=("Verdana", 20, "normal"))
time.sleep(1)
turtle.clear()


def start_race():
    thread1 = threading.Thread(target=t1.race)
    thread2 = threading.Thread(target=t2.race)
    thread3 = threading.Thread(target=t3.race)
    thread1.start()
    thread2.start()
    thread3.start()
    time_thread = threading.Timer(5.28 * 1.5, result)
    time_thread.start()


speed_list = [t1.speed_of_turtle, t2.speed_of_turtle, t3.speed_of_turtle]
max_speed_index = speed_list.index(max(speed_list))
color_list = ["Purple", "Red", "Green"]


def result():
    turtle.write(arg="The winner is {}".format(color_list[max_speed_index]), move=True, align="center",
                 font=("Verdana", 30, "normal"))
    turtle.color(color_list[max_speed_index].lower())


turtle.listen()
turtle.onkey(start_race, "Up")

turtle.Screen().exitonclick()
