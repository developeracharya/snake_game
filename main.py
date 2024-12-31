import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(fun=snake.down,key='Down')
screen.onkey(fun=snake.right,key='Right')
screen.onkey(fun=snake.left,key='Left')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.listen()
screen.exitonclick()