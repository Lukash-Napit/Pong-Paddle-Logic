from turtle import Turtle , Screen
import random
import time

a = 5 #variable storing change of y value of ball temporarily
b = 0 #variable storing change of x value of ball temporarily
s = 0 #variable storing Score value temporarily
speed = 0.0175 #initial speed of ball
paddle_speed = 30 #speed of paddle
ALIGNMENT = "center"
FONT = ("Courier", 20 , "normal")

screen = Screen()
screen.setup(500,500)
screen.bgcolor("black")
screen.title("Simple Pong")
screen.tracer(0)

ball = Turtle(shape="square")
ball.color("white")
ball.penup()
ball.goto(0,40)

paddle = Turtle(shape="square")
paddle.color("white")
paddle.penup()
paddle.turtlesize(stretch_wid=1,stretch_len=5)
paddle.goto(0,-190)

with open("High-score.txt") as hs:
    high_score = int(hs.read())

score = Turtle()
score.hideturtle()
score.color("white")
score.penup()
score.goto(0,210)
score.write(f"Score = {s}  HighScore = {high_score}", align=ALIGNMENT, font=FONT)

game_over = Turtle()
game_over.hideturtle()
game_over.color("white")
game_over.penup()
game_over.goto(0,0)

horizontal_line = Turtle(shape="square")
horizontal_line.color("white")
horizontal_line.penup()
horizontal_line.goto(0,195)
horizontal_line.turtlesize(0.0125,25)

def move_left():
    paddle.goto( paddle.xcor() - paddle_speed,-190)
def move_right():
    paddle.goto(paddle.xcor() +  paddle_speed, -190)

screen.listen()
screen.onkey(move_left,"Left")
screen.onkey(move_right,"Right")

game = True

while game:
    speed_increasing_ratio = s
    time.sleep(speed)
    screen.update()
    ball.goto(ball.xcor()+b,ball.ycor()-a)

    #ball bounces from roof
    if ball.ycor()==180:
        a=-a


    #ball bounces from paddle
    if ball.ycor()==-180 and ball.distance(paddle)<60:
        a=-a
        s+=1
        score.clear()
        score.write(f"Score = {s}  HighScore = {high_score}", align=ALIGNMENT, font=FONT)
        if ball.distance(paddle)<20:
            b = int(random.choice(['1', '-1','0','1', '-1']))
            ball.goto(ball.xcor() + b, ball.ycor())

        elif ball.distance(paddle)<40:
            b = int(random.choice(['3', '-3']))
            ball.goto(ball.xcor() + b, ball.ycor())

        else:
            b=int(random.choice(['5','-5']))
            ball.goto(ball.xcor()+b, ball.ycor())


    #ball bounces from wall
    if ball.xcor()==-240 or ball.xcor()==240 or ball.xcor()>240 or ball.xcor()<-240:
        b=-b
        ball.goto(ball.xcor() + b, ball.ycor())


    #slowly increases speed of ball according to the score
    if  speed_increasing_ratio<s and speed > 0.0075:
        speed -= 0.0005
        speed_increasing_ratio = s


    #paddle couldn't reach ball resulting in GAME OVER
    if ball.ycor() == -240:
        game = False
        game_over.write("Game Over", align=ALIGNMENT, font=FONT)
        #saves the HighScore
        if s>high_score:
            with open("High-score.txt","w") as hs:
                hs.write(f"{s}")


screen.exitonclick()
