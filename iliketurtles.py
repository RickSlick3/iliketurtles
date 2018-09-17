from turtle import Turtle

t = Turtle()

t.shape("triangle")

for x in range(50):
    t.forward(50)
    t.right(50)

input("pres any key to exit")