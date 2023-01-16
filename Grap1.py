import turtle

#Pong by Andre

sandbox=turtle.Screen()
sandbox.title("Pong by Grade 8 and 9")
sandbox.bgcolor("black")
sandbox.setup(width=800, height=600)
sandbox.tracer(0) #allows for game t be faster


#Score
score_a = 0
score_b = 0
#Start with AI off
switch = -1

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #sets the speed to maximum
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #sets the speed to maximum
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #sets the speed to maximum
ball.shape("square")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.write("Jugador A:{}  Jugador B:{}".format(score_a,score_b),align="center", font=("Courier",24, "normal"))
pen.goto(0,230)
pen.write("Utiliza las teclas S y W. Juega contra la maquina pulsando G",align="center", font=("Courier",16, "normal"))


#Functions
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
def AI_Switch():
    global switch
    switch *= -1

# Keyboard input
sandbox.listen()
sandbox.onkeypress(paddle_a_up,"w")
sandbox.onkeypress(paddle_a_down,"s")
sandbox.onkeypress(paddle_b_up,"Up")
sandbox.onkeypress(paddle_b_down,"Down")
sandbox.onkeypress(AI_Switch,"g")

#Main game loop
while True:
    sandbox.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking

    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *=-1
        #winsound.PlaySound("plop.wav", winsound.SND_ASYNC)

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *=-1
        #winsound.PlaySound("plop.wav", winsound.SND_ASYNC)

    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a+=1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.goto(0,260)
        pen.write("Jugador A:{}  Jugador B:{}".format(score_a,score_b),align="center", font=("Courier",24, "normal"))
        pen.goto(0,230)
        pen.write("Utiliza las teclas S y W. Juega contra la maquina pulsando G",align="center", font=("Courier",16, "normal"))

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b+=1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.goto(0,260)
        pen.write("Jugador A:{}  Jugador B:{}".format(score_a,score_b),align="center", font=("Courier",24, "normal"))
        pen.goto(0,230)
        pen.write("Utiliza las teclas S y W. Juega contra la maquina pulsando G",align="center", font=("Courier",16, "normal"))

    #Paddle Bounce

    if ball.xcor()>340 and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
        ball.dx *=-1
        #winsound.PlaySound("plop.wav", winsound.SND_ASYNC)
    if ball.xcor()<-340 and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
        ball.dx *=-1
        #winsound.PlaySound("plop.wav", winsound.SND_ASYNC)

    #AI Player
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor())>70 and switch==1:
            paddle_b_up()        
    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor())>70 and switch==1:
            paddle_b_down()
