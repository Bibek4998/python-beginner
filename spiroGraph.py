import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Spirograph")

spiro = turtle.Turtle()
spiro.speed(0)
spiro.width(2)
colors = ["red", "yellow", "cyan", "magenta", "white", "lime"]

for i in range(72):
    spiro.color(random.choice(colors))
    spiro.circle(100)
    spiro.left(5)

turtle.done()
