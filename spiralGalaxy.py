import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Spiral Galaxy")

galaxy = turtle.Turtle()
galaxy.hideturtle()
galaxy.speed(0)
colors = ["white", "cyan", "lightblue", "lightpink", "violet"]

for i in range(300):
    angle = i * math.radians(137.5)  # golden angle
    radius = 4 * math.sqrt(i)
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    galaxy.penup()
    galaxy.goto(x, y)
    galaxy.dot(6, colors[i % len(colors)])

turtle.done()
