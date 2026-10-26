import turtle
import math
import colorsys

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Rainbow Flower Animation")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

h = 0

for i in range(720):
    color = colorsys.hsv_to_rgb(h % 1, 1, 1)
    t.pencolor(color)

    r = 220 * math.sin(math.radians(6 * i))
    x = r * math.cos(math.radians(i))
    y = r * math.sin(math.radians(i))

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(2)

    h += 0.003

t.penup()
t.goto(0, -20)
t.color("white")
t.write(
    "FOLLOW",
    align="center",
    font=("Arial", 24, "bold")
)

turtle.done()