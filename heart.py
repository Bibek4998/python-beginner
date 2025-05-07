import turtle
import math

# Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Stunning Heart")

# Create turtle
heart = turtle.Turtle()
heart.speed(0)
heart.color("red")
heart.width(4)

# Move to starting position
heart.penup()
heart.goto(0, -200)
heart.pendown()

# Draw heart using parametric equation
heart.hideturtle()
for i in range(3):  # retrace multiple times for glow effect
    heart.penup()
    heart.goto(0, -200)
    heart.pendown()
    heart.setheading(0)
    
    heart.begin_fill()
    for t in range(0, 360):
        angle = math.radians(t)
        x = 16 * math.sin(angle) ** 3
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
        x *= 15  # scale up
        y *= 15
        heart.goto(x, y)
    heart.end_fill()

# Optional: Outline glow effect
for size in range(4, 0, -1):
    heart.penup()
    heart.goto(0, -200)
    heart.pendown()
    heart.width(size)
    heart.color("red")
    for t in range(0, 360):
        angle = math.radians(t)
        x = 16 * math.sin(angle) ** 3
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
        x *= 15
        y *= 15
        heart.goto(x, y)

turtle.done()
