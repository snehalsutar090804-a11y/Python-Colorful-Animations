
import turtle
import math
import random

screen = turtle.Screen()
screen.setup(850, 800)
screen.bgcolor("#050014")
screen.title("💖 Snehal's Rainbow Heart 💖")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

colors = [
    "#ff0080", "#ff4500", "#ffff00",
    "#00ff88", "#00ffff", "#3399ff",
    "#bf00ff", "#ff00ff"
]

# Draw rainbow neon heart
for i in range(361):
    a = math.radians(i)
    x = 16 * math.sin(a) ** 3
    y = (13 * math.cos(a)
         - 5 * math.cos(2 * a)
         - 2 * math.cos(3 * a)
         - math.cos(4 * a))

    t.goto(x * 18, y * 18)
    t.dot(7, colors[i % len(colors)])

    if i % 4 == 0:
        screen.update()

# Write Snehal in rainbow colours
t.goto(-145, -15)
t.setheading(0)

for i, letter in enumerate("Harshu"):
    t.color(colors[i % len(colors)])
    t.write(letter, align="center",
            font=("Arial", 43, "bold"))
    t.forward(48)

# Add colourful stars
random.seed(10)

for i in range(65):
    x = random.randint(-360, 360)
    y = random.randint(-350, 350)

    # Keep decorations away from the name
    if -180 < x < 180 and -70 < y < 70:
        continue

    t.goto(x, y)
    t.dot(random.randint(3, 8),
          random.choice(colors))

# Small hearts around the design
for x, y in [(-260, 80), (260, 80),
             (-220, -180), (220, -180)]:
    t.goto(x, y)
    t.color("#ff1493")
    t.write("♥", align="center",
            font=("Arial", 24, "bold"))

# Greeting below the heart
t.goto(0, -300)
t.color("#00ffff")
t.write("Made with Love ❤️",
        align="center",
        font=("Arial", 19, "bold"))

screen.update()
screen.mainloop()
