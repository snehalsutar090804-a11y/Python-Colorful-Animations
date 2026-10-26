import turtle
import colorsys

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Colorful Spiral")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

n = 36
h = 0

for i in range(200):
    color = colorsys.hsv_to_rgb(h % 1, 1, 1)
    t.pencolor(color)
    h += 1 / n

    t.forward(i)
    t.left(135)
    t.forward(i)
    t.left(30)
    t.circle(i, 45)

turtle.done()