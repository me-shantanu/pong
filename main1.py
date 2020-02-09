import turtle
win = turtle.Screen()
win.title("pong by @soldiersupreme")
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0)


#score
score_1 = 0
score_2 = 0


#paddle one
padle_1 = turtle.Turtle()
padle_1.speed(0)
padle_1.shape("square")
padle_1.color("black")
padle_1.shapesize(stretch_wid=5,stretch_len=1)
padle_1.penup()
padle_1.goto(-350,0)
#paddle two
padle_2 = turtle.Turtle()
padle_2.speed(0)
padle_2.shape("square")
padle_2.color("black")
padle_2.shapesize(stretch_wid=5,stretch_len=1)
padle_2.penup()
padle_2.goto(350,0)

#ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx =.2# wvery time ball move it move eith two pixul when x is positive x move otherwise y move 
ball.dy =-.2# it will also difine the speed of the ball beacause we all know the speed is basically apixul moveing


#pen
pen = turtle.Turtle()
pen.speed(0)# this speed is a animation speed it is not a movment speeed
pen.color("black")
pen.penup()
pen.hideturtle()#we not see pen we see only the number will change and pen is hideingg in behaind 
pen.goto(0, 260)
pen.write("Player A: 0 And Player B: 0 ",align="center", font=("Courier", 24, "bold"))


#for moving the ball and padle_2 and pafle 1
def padle_1up():
    y = padle_1.ycor()#is from tuterl module it return the y cordnate
    y += 20
    padle_1.sety(y)



def padle_1down():
    y = padle_1.ycor()#is from tuterl module it return the y cordnate
    y -= 20
    padle_1.sety(y)



def padle_2up():
    y = padle_2.ycor()#is from tuterl module it return the y cordnate
    y += 20
    padle_2.sety(y)



def padle_2down():
    y = padle_2.ycor()#is from tuterl module it return the y cordnate
    y -= 20
    padle_2.sety(y)

#ball movement function



#keyboard bindinf
win.listen()
win.onkeypress(padle_1up, "w")
win.onkeypress(padle_1down, "s")
win.onkeypress(padle_2up, "Up")
win.onkeypress(padle_2down, "Down")

#main loop
while True:
    win.update()
    #move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border checking
    if ball.ycor() > 290:
        ball.sety(290) #290 ispixul from where the ball is going to return to the
        ball.dy *= -1


    if ball.ycor() < -290:
        ball.sety(-290)# cordnate of takarav of ball
        ball.dy *= -1 #use to return the direction 

    if ball.xcor() >390:
        ball.goto(0,0) #comming ball in center
        ball.dx *= -1
        #fromhere to start update score
        score_1 += 1
        pen.clear()
        pen.write("Player A: {} And Player B: {}".format(score_1,score_2),align="center", font=("Courier", 24, "bold"))
        # update the score
    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        #fromhere to start update score
        score_2 += 1
        pen.clear()
        pen.write("Player A: {} And Player B: {}".format(score_1,score_2),align="center", font=("Courier", 24, "bold"))
        # update the score
    
    #ball colide with paddle
    if (ball.xcor() >340 and ball.xcor() < 350) and (ball.ycor() < padle_2.ycor() + 40 and ball.ycor() > padle_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() <-340 and ball.xcor() > -350) and (ball.ycor() < padle_1.ycor() + 40 and ball.ycor() > padle_1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
