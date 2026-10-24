import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green", "cyan", "purple"]

for i in range(144):
    t.color(colors[i % 6])
    t.forward(i * 3)
    t.right(120)

turtle.done()