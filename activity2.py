import random

options = ["Rock", "Paper", "Scissors"]

user_chioce = input ("choose either Rock, Paper or Scissors: ")
user_choice = user_chioce.capitalize()
computer_choice = random.choice(options)

print("You chose: ", user_choice)
print("Computer chose: ", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock smashes Scissors! You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("Paper covers Rock! You win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cuts Paper! You win!")
else:
    print("You lose!. ")