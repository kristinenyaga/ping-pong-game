from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time
screen = Screen()
screen.bgcolor("black")
screen.title("Ping Pong")
screen.setup(width=800,height=600)
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = ScoreBoard()
print(r_paddle.pos())

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")


screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s ")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.change_direction()

    if ball.distance(r_paddle) < 50 and ball.xcor() < 330 or ball.distance(l_paddle) <50 and ball.xcor() < -330:
        ball.bounce()
        ball.move_speed -=0.002

    if ball.xcor() > 380 :
        ball.reset()
        ball = Ball()
        ball.bounce()
        ball.move_speed = 0.04
        scoreboard.l_point()

    if ball.xcor() < -380 :
        ball.reset()
        ball = Ball()
        ball.change_direction()
        ball.move_speed = 0.04
        scoreboard.r_point()
 






screen.exitonclick()