import turtle
import os
import time


wn = turtle.Screen()
wn.title('Ping Pong ding dong')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

sa, sb = 0,0

title = turtle.Turtle()
title.speed(0)
title.color('white')
title.penup()
title.hideturtle()
title.goto(0,-20)
title.write('Pong: A Game to 12', align='center',font=('Courier',50,'normal'))
time.sleep(2)
title.clear()
title.write('Loading...',align='center',font=('Courier',50,'normal'))
time.sleep(1.5)
title.clear()




pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)



def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')


while True:
    wn.update()
    pen.clear()
    pen.write('Player A: %d Player B: %d'%(sa,sb), align='center',font=('Courier',24,'normal'))
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system('afplay bounce.wav&')
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        os.system('afplay bounce.wav&')
    if ball.xcor() > 390:
        sa += 1
        ball.goto(0,0)
        ball.dx = -2.5
        ball.dy = 2.5
        os.system('afplay win.wav&')
        
    if ball.xcor() < -390:
        sb += 1
        ball.goto(0,0)
        ball.dx = 2.5
        ball.dy = 2.5
        os.system('afplay win.wav&')

    if ball.xcor() > 330 and ball.xcor() < 340 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(330)
        ball.dx *= -1.1
        ball.dy *= 1.1
        os.system('afplay bounce.wav&')
    if ball.xcor() < -330 and ball.xcor() > -340 and ball.ycor() > paddle_a.ycor() - 40 and ball.ycor() < paddle_a.ycor() + 40:
        ball.setx(-330)
        ball.dx *= -1.1
        ball.dy *= 1.1
        os.system('afplay bounce.wav&')

