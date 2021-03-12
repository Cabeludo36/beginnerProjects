"""
COBRINHA

Objetivo:
Pegar o maximo de comidas (pontos vermelhos) para 
conseguir a maior pontuação
"""

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Tela
wn = turtle.Screen()
wn.title("Jogo da cobra")
wn.bgcolor("purple")
wn.setup(width=600, height=600)
wn.tracer(0) # Tira os updates da tela

# Cabeça da cobra
cabeca = turtle.Turtle()
cabeca.speed(0)
cabeca.shape("square")
cabeca.color("black")
cabeca.penup()
cabeca.goto(0,0)
cabeca.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

segments = []

# Mostra score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Comandos dos controles
def go_up():
    if cabeca.direction != "down":
        cabeca.direction = "up"

def go_down():
    if cabeca.direction != "up":
        cabeca.direction = "down"

def go_left():
    if cabeca.direction != "right":
        cabeca.direction = "left"

def go_right():
    if cabeca.direction != "left":
        cabeca.direction = "right"

def move():
    if cabeca.direction == "up":
        y = cabeca.ycor()
        cabeca.sety(y + 20)

    if cabeca.direction == "down":
        y = cabeca.ycor()
        cabeca.sety(y - 20)

    if cabeca.direction == "left":
        x = cabeca.xcor()
        cabeca.setx(x - 20)

    if cabeca.direction == "right":
        x = cabeca.xcor()
        cabeca.setx(x + 20)

# Controles
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Loop do jogo
while True:
    wn.update()

    # Checa pela colisão com a borda
    if cabeca.xcor()>290 or cabeca.xcor()<-290 or cabeca.ycor()>290 or cabeca.ycor()<-290:
        time.sleep(1)
        cabeca.goto(0,0)
        cabeca.direction = "stop"

        # Esconde o caminho
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Limpa quando perde
        segments.clear()

        # Reseta o score para 0
        score = 0

        # Reseta o delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # checa se pega a comida
    if cabeca.distance(comida) < 20:
        # Muda a coordenada da comida
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x,y)

        # Adiciona pedaço
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Diminui o delay
        delay -= 0.001

        # Aumenta o score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move os pedaços finais em ordem reversa
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move o seguimento 0 para onde a cabeça esta
    if len(segments) > 0:
        x = cabeca.xcor()
        y = cabeca.ycor()
        segments[0].goto(x,y)

    move()    

    # checa se a cabeça bate no corpo
    for segment in segments:
        if segment.distance(cabeca) < 20:
            time.sleep(1)
            cabeca.goto(0,0)
            cabeca.direction = "stop"
        
            # Tira os pedaços do corpo
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Da clear na lista de pedaços
            segments.clear()

            # Reseta o score
            score = 0

            # Reseta o delay
            delay = 0.1
        
            # Atualiza a tela do score
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()