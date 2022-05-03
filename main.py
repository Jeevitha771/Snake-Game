from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

s1 = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(s1.up,"Up")
screen.onkey(s1.down,"Down")
screen.onkey(s1.left,"Left")
screen.onkey(s1.right,"Right")

game_is_on = True
while(game_is_on):
    screen.update()
    time.sleep(0.1)
    s1.move()

    #Detect collision with food
    if s1.head.distance(food)<15:
        food.refresh()
        s1.extend()
        scoreboard.increase_score()
    #Detect collision with wall
    if s1.head.xcor()>280 or s1.head.xcor()<-280 or s1.head.ycor()>280 or s1.head.ycor()<-280:
        scoreboard.reset()
        s1.reset()
    #Detect collision with tail
    for segment in s1.segments[1:]:
        if segment == s1.head:
            pass
        elif s1.head.distance(segment)<10:
            scoreboard.reset()
            s1.reset()
    #if head collides with any segment in the tail:
        #trigger game_over


screen.exitonclick()