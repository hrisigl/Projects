from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "orange", "brown", "blue", "purple"]
y_positions = [-150, -90, -30, 30, 90, 150]

all_turtles = []

for t_idx in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t_idx])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[t_idx])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} turtle is the winner!")
            else:
                print(f"You've lost!, {winning_color} turtle won the race!")
            is_race_on = False

        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)

screen.exitonclick()
