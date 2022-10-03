import random
from tkinter import messagebox
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

while True:
    user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
    if user_bet in colors:
        break
    messagebox.showerror(title="Error!", message=f"Please enter a valid color: {list(colors)}.")

print(f"You bet on {user_bet}.")
print(f"The colors are: {', '.join(colors)}.")
print()

y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for n in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[n])
    tim.penup()
    tim.goto(x=-230, y=y_pos[n])
    all_turtles.append(tim)

game_on = bool(user_bet)
while game_on:

    for t in all_turtles:
        if t.xcor() > 220:
            game_on = False
            if t.pencolor() == user_bet:
                messagebox.showinfo("You Won!", f"You have won! The {(t.pencolor()).title()} turtle is the winner")
            else:
                messagebox.showinfo("You Lost!", f"You have lost! The {(t.pencolor()).title()} turtle is the winner")
            screen.mainloop()
        distance = random.randint(0, 10)
        t.forward(distance)

screen.exitonclick()
