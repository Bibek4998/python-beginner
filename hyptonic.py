import turtle
import colorsys

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Hypnotic Spiral")

spiral = turtle.Turtle()
spiral.speed(0)
spiral.hideturtle()

hue = 0
for i in range(300):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    spiral.color(color)
    spiral.pensize(2)
    spiral.forward(i * 0.5)
    spiral.left(59)
    hue += 0.005

turtle.done()
