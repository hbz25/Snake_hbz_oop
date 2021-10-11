from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
has_collided = False

while game_on:
    if not has_collided:
        snake.move()
    # TODO 4: Detect collision with food
    if food.distance(snake.head) < 20:
        food.refresh()
        snake.add_segments()
        scoreboard.scorer()
    # TODO 6: Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -310:
        has_collided = True
        scoreboard.game_over()

    # TODO 7: Detect collision with tail
    for snake_segment in snake.body[1:]:
        if snake.head.distance(snake_segment) < 10:
            has_collided = True
            scoreboard.game_over()
