import turtle
import random
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Fireworks")

firework = turtle.Turtle()
firework.hideturtle()
firework.speed(0)

colors = ["red", "yellow", "blue", "magenta", "cyan", "lime", "white"]

def explode(x, y):
    firework.penup()
    firework.goto(x, y)
    for i in range(36):
        firework.color(random.choice(colors))
        firework.setheading(i * 10)
        firework.forward(100)
        firework.pendown()
        firework.forward(20)
        firework.penup()
        firework.goto(x, y)

for _ in range(10):
    x = random.randint(-200, 200)
    y = random.randint(0, 200)
    explode(x, y)
    time.sleep(0.5)

turtle.done()
