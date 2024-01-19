import turtle

def mover_para_frente():
    turtle.forward(10)

def mover_para_tras():
    turtle.backward(10)

def virar_esquerda():
    turtle.left(10)

def virar_direita():
    turtle.right(10)

turtle.onkey(mover_para_frente, "w")
turtle.onkey(mover_para_tras, "s")
turtle.onkey(virar_esquerda, "a")
turtle.onkey(virar_direita, "d")

turtle.listen()
turtle.done()
