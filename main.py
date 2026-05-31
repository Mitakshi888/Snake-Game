import time
from turtle import Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightskyblue")
screen.title("Snake")
screen.tracer(0)
starting_pos = [(0,0), (-20, 0), (-40, 0)]
segments = []
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()  # Use the fixed scoring method

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset_score()
            snake.reset()  # Reset the snake to starting position (requires a reset method in your Snake class)

        # Detect collision with tail
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:  # Changed from > to <
                scoreboard.reset_score()
                snake.reset()  # Reset the snake here too
screen.exitonclick()