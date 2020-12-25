import threading
import turtle
import random
import time

class Player(turtle.Turtle):
    def __init__(self, color, shape):
        turtle.Turtle.__init__(self)
        self.speed_of_turtle = random.uniform(1, 1.5)

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
        self.setheading(self.head)

    def race(self):

        self.speed(self.speed_of_turtle)
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

run = False
def start_race():

    thread1 = threading.Thread(target=t1.race)
    thread2 = threading.Thread(target=t2.race)
    thread3 = threading.Thread(target=t3.race)
    thread1.start()
    thread2.start()
    thread3.start()

    T = threading.Timer(5.5 * min_speed, result)
    T.start()


speed_list = [t1.speed_of_turtle, t2.speed_of_turtle, t3.speed_of_turtle]
max_speed = max(speed_list)
min_speed = min(speed_list)

def result():
    print(t1.speed_of_turtle)
    print(t2.speed_of_turtle)
    print(t3.speed_of_turtle)



    for speed in speed_list:
        if max_speed == speed:
            print('the max speed is for', speed_list.index(speed) + 1)




turtle.listen()
turtle.onkey(start_race, "Up")





turtle.Screen().exitonclick()
