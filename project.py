#Rock,paper,scissor game
#0 for rock,1 for paper,2 for scissor
import random

user_choice = int(input("Enter 0 ,1 or 2:"))
if user_choice > 2 or user_choice < 0:
    print("Invalid choice")
else:
    computer_choice = random.randint(0,2)
    print("Computer chose: ")
    print(computer_choice)
    if user_choice == computer_choice:
        print("It's a draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice > user_choice:
        print("You lose")
