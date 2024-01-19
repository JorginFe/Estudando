import turtle

def escrita():
    turtle.color("black")
    turtle.penup()
    turtle.goto(50, 20)
    turtle.pendown()
    turtle.write("Fluminense Football Club", align="left", font=("Arial", 14, "italic"))
    
def coracao():
    turtle.color("red")
    turtle.fillcolor('')
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()


turtle.speed(2)
turtle.pensize(2)
turtle.hideturtle()


coracao()
escrita()


turtle.done()
