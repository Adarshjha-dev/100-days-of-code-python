from turtle import Turtle, Screen
import random

race_in_progress = False
game_screen = Screen()
game_screen.setup(width=500, height=400)

turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

user_bet = game_screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple):",
)

for index in range(6):
    racer = Turtle(shape="turtle")
    racer.color(turtle_colors[index])
    racer.penup()
    racer.goto(x=-230, y=-100 + (index * 40))
    all_turtles.append(racer)

if user_bet:
    race_in_progress = True
else:
    print("No bets were placed.")

while race_in_progress:
    for racer in all_turtles:
        if racer.xcor() > 230:
            race_in_progress = False
            winning_color = racer.pencolor()

            result_turtle = Turtle()
            result_turtle.hideturtle()
            result_turtle.penup()
            result_turtle.goto(0, 160)

            if winning_color == user_bet.lower():
                result_message = f"You won! The {winning_color} turtle is the winner!"
            else:
                result_message = f"You lost. The {winning_color} turtle won the race."

            result_turtle.write(result_message, align="center", font=("Arial", 16, "bold"))
            break

        distance = random.randint(0, 10)
        racer.forward(distance)

game_screen.exitonclick()
