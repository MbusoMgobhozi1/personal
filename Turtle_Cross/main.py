import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize the player, cars and scoreboard
player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    # Detect collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect a successful crossing
    if player.at_finish_line():
        player.start()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()