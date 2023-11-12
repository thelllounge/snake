from turtle import Screen, Turtle
import snake
import time
import food
import scoreboard

snake_is_hungry = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Score()

screen.listen()
screen.onkey(snake.face_north, "Up")
screen.onkey(snake.face_south, "Down")
screen.onkey(snake.face_east, "Right")
screen.onkey(snake.face_west, "Left")

screen.update()

while snake_is_hungry:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    if (snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or
            snake.head.ycor() < -290):
        scoreboard.reset()
        snake.reset()

    for piece in snake.snake_body_pieces[1:]:
        if snake.head.distance(piece) < 10:
            scoreboard.reset()
            snake.reset()

    if food.distance(snake.head) <= 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()


# scoreboard.reset()

screen.exitonclick()
