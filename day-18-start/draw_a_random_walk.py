import turtle as t
import random

tim = t.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

for _ in range(200):
    # tim.color(random.choice(colors))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))