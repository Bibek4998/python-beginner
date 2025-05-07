import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Fractal Tree")

tree = turtle.Turtle()
tree.color("green")
tree.left(90)
tree.speed(0)
tree.hideturtle()

def branch(length):
    if length > 5:
        tree.forward(length)
        tree.left(30)
        branch(length - 15)
        tree.right(60)
        branch(length - 15)
        tree.left(30)
        tree.backward(length)

tree.penup()
tree.goto(0, -250)
tree.pendown()
branch(100)

turtle.done()
