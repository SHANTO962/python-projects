import random

exit = False
user_point = 0
computer_point = 0

while exit == False:
    options = ["rock","paper","scissors"]
    user_input = input("Choose rock,paper,scissors or exit")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("computer input is rock")
            print("It is a tie!")
        
        elif computer_input == "paper":
            print("Your input is rock")
            print("computer input is paper")
            print("computer wins")
            computer_point += 1

        elif computer_input == "scissors":
            print("Your input is rock")
            print("computer input is scissors")
            print("you win")
            user_point += 1


        