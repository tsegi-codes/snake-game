from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_up()
        snake.snake_grow()
    snake.move()
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_on = False
        score.game_over()

















screen.title("My Snake Game")










screen.exitonclick()
