#-------------------------------------------------------------------------------
# Name:        Snake Game
# Purpose:     Fun
#
# Author:      nicolescu
#
# Created:     12/02/2022
# Copyright:   (c) nicol 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from snake import Snake
from turtle import Screen
from Food import Food
from Scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Gamme")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#     Detect collision with wall
    if (snake.head.xcor() > 280) or (snake.head.xcor() < -280) or (snake.head.ycor() > 280) or (snake.head.ycor() < -280):
        game_is_on = False
        scoreboard.game_is_over()

    # Detect colision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10  :
            game_is_on = False
            scoreboard.game_is_over()


screen.exitonclick()