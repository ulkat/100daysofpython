import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color


tim.shape("turtle")
tim.color("DarkOrchid")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


"""def draw_shape(i):
    angle = 360/i
    for j in range(i) :
        tim.forward(100)
        tim.right(angle)

for i in range (3,11):
    tim.color(random.choice(colours))
    draw_shape(i)
    """
"""
angles = [0,90,180,270]
tim.pensize(10)
tim.speed("fastest")

for i in range(250):
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(random.choice(angles))
    
"""
"""
tim.speed("fastest")

for  i in  range(90):
    tim.color(random_color())
    tim.left(4)
    tim.circle(100, 360, 200 )
    """
s
































screen = t.Screen()
screen.exitonclick()