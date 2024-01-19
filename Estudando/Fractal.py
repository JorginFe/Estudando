import turtle

def fractal(tartaruga, comprimento, nivel):
    if nivel == 0:
        return
    tartaruga.forward(comprimento)
    tartaruga.left(30)
    fractal(tartaruga, comprimento/2, nivel-1)
    tartaruga.right(60)
    fractal(tartaruga, comprimento/2, nivel-1)
    tartaruga.left(30)
    tartaruga.backward(comprimento)

turtle.speed(2)
fractal(turtle, 200, 4)
turtle.done()
