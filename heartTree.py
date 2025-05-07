import turtle
import math
import random
import time

# Setup screen
screen = turtle.Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.title("Stunning Heart & Fractal Tree")

# Turtles
heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)

tree = turtle.Turtle()
tree.hideturtle()
tree.speed(0)

sparkle = turtle.Turtle()
sparkle.hideturtle()
sparkle.speed(0)

star = turtle.Turtle()
star.hideturtle()
star.speed(0)

def draw_perfect_heart():
    heart.penup()
    heart.goto(150, -10)
    heart.pendown()
    heart.color("red")
    heart.begin_fill()

    for t in range(0, 360):
        x = 16 * math.sin(math.radians(t))**3
        y = 13 * math.cos(math.radians(t)) - 5 * math.cos(math.radians(2*t)) - 2 * math.cos(math.radians(3*t)) - math.cos(math.radians(4*t)
)
        heart.goto(150 + x*10, y*10 - 100)
        if t % 5 == 0:
            time.sleep(0.01)
    heart.end_fill()

    # Glow effect (draw outlines)
    for size in range(1, 6):
        heart.penup()
        heart.goto(150, -10)
        heart.pendown()
        heart.pensize(size)
        heart.color((1, 0, 0, 0.1 * size))
        for t in range(0, 360):
            x = 16 * math.sin(math.radians(t))**3
            y = 13 * math.cos(math.radians(t)) - 5 * math.cos(math.radians(2*t)) - 2 * math.cos(math.radians(3*t)) - math.cos(math.radians(4*t))
            heart.goto(150 + x*10, y*10 - 100)

def pulse_heart():
    for _ in range(5):
        heart.color("hot pink")
        time.sleep(0.2)
        heart.color("red")
        time.sleep(0.2)

def draw_tree(branch_length, t):
    if branch_length < 10:
        return
    else:
        if branch_length < 20:
            t.color("lime")
        elif branch_length < 40:
            t.color("forest green")
        else:
            t.color("sienna")

        t.pensize(branch_length / 10)
        t.forward(branch_length)
        time.sleep(0.02)

        angle = random.randint(20, 30)
        length_factor = random.uniform(0.7, 0.8)

        t.left(angle)
        draw_tree(branch_length * length_factor, t)
        t.right(angle * 2)
        draw_tree(branch_length * length_factor, t)
        t.left(angle)

        t.penup()
        t.backward(branch_length)
        t.pendown()

def twinkle_sparkles():
    colors = ["yellow", "white", "light blue", "magenta", "cyan"]
    for _ in range(40):
        x = random.randint(-450, 450)
        y = random.randint(-250, 300)
        sparkle.penup()
        sparkle.goto(x, y)
        sparkle.pendown()
        sparkle.color(random.choice(colors))
        sparkle.dot(random.randint(4, 10))
        time.sleep(0.03)

def shooting_star():
    for _ in range(5):
        x_start = random.randint(-500, -300)
        y_start = random.randint(100, 300)
        star.penup()
        star.goto(x_start, y_start)
        star.pendown()
        star.color("white")
        for i in range(20):
            star.forward(15)
            star.right(1)
            star.dot(6, "white")
            time.sleep(0.01)
        star.clear()

# --- Draw Sparkles ---
twinkle_sparkles()

# --- Shooting stars ---
for _ in range(3):
    shooting_star()

# --- Draw Tree ---
tree.penup()
tree.goto(-300, -200)
tree.left(90)
tree.pendown()
draw_tree(100, tree)

# --- Draw Heart ---
draw_perfect_heart()

# --- Pulse effect ---
pulse_heart()

turtle.done()
