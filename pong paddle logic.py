from turtle import Turtle , Screen

screen = Screen()
screen.setup(500,500)
screen.bgcolor("black")
ball = Turtle(shape="square")
ball.color("white")
ball.penup()
ball.goto(0,40)
paddle = Turtle(shape="square")
paddle.color("white")
paddle.penup()
paddle.turtlesize(stretch_wid=1,stretch_len=5)
paddle.goto(0,-50)

a=5
def move_left():
    paddle.goto( paddle.xcor() - 50,-50)
def move_right():
    paddle.goto(paddle.xcor() +  50, -50)

screen.listen()
screen.onkey(move_left,"Left")
screen.onkey(move_right,"Right")

game = True

while game:
    ball.goto(ball.xcor(),ball.ycor()+a)
    if ball.ycor()==200:
        a=-a
    if ball.ycor()==-40:
        a=-a

screen.exitonclick()