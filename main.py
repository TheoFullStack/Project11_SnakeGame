from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
food = Food()
scoreboard = Scoreboard()
def exitprogram():
    screen.bye()

screen.setup(600,600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key='Up',fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left',fun=snake.left)
screen.onkey(key='Right',fun=snake.right)
screen.onkey(key='Escape', fun=exitprogram)








game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.gameover()

    #Detect collision with tail (if head collides with any segment):
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()