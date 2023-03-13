import random

user_choice = input("Choose your weapon : Rock,Paper,Scissors (Choose 'R'/'P'/'S'': ")
user_choice = user_choice.upper()

if user_choice.startswith("R"):
    user_full_choice = "Rock"
elif user_choice.startswith("P"):
    user_full_choice = "Paper"
elif user_choice.startswith("S"):
    user_full_choice = "Scissors"
else:
    print("Invalid choice.")
    exit()

print(f"You chose {user_full_choice},")
computers_weapon = ('Rock', 'Paper', 'Scissors')
computers_weapon = random.choice(computers_weapon)
print(f"Computer chose {computers_weapon}.")

if user_full_choice == computers_weapon:
    print(f"You and the computer both chose {user_full_choice}. It's a tie.")
elif user_full_choice == "Rock":
    if computers_weapon == "Paper":
        print("Paper beats rock. Computer wins!")
    elif computers_weapon == "Scissors":
        print("Rock beats scissors. You win!")
elif user_full_choice == "Paper":
    if computers_weapon == "Rock":
        print("Paper beats rock. You win!")
    elif computers_weapon == "Scissors":
        print("Scissors cut papers. Computer wins, you LOSE!")
elif user_full_choice == "Scissors":
    if computers_weapon == "Paper":
        print("Scissors cut papers. You win!")
    elif computers_weapon == "Rock":
        print("Rock beats scissors. Computer wins, you lose!")







