import random
import re

user_choice = input("Choose your weapon : Rock,Paper,Scissors (Choose 'R'/'P'/'S'': ")
user_choice = user_choice.upper()

if re.match(r'\bR\w*',user_choice): #starts with R, can end with any letter,digit..
    user_full_choice = "Rock"
elif re.match(r'\bP\w*',user_choice):
    user_full_choice = "Paper"
elif re.match(r'\bS\w*',user_choice):
    user_full_choice = "Scissors"
else:
    print("Invalid choice.")
    exit()


print("You chose " + user_full_choice +",")
computers_weapon = ['Rock','Paper','Scissors']
computers_weapon = random.choice(computers_weapon)
print("Computer chose " + computers_weapon + ".")

if user_full_choice==computers_weapon:
    print("You and the computer both chose " + user_full_choice + ". It's a tie.")
elif user_full_choice=="R" and computers_weapon=="P":
    print("Paper beats rock. Computer wins!")
elif user_full_choice=="P" and computers_weapon=="R":
    print("Paper beats rock. You win!")
elif user_full_choice=="P" and computers_weapon=="S":
    print("Scissors cut papers. Computer wins, you LOSE!")
elif user_full_choice=="S" and computers_weapon=="P":
    print("Scissors cut papers. You win!")
elif user_full_choice=="S" and computers_weapon=="R":
    print("Rock beats scissors. Computer wins, you lose!")
elif user_full_choice=="R" and computers_weapon=="S":
    print("Rock beats scissors. You win!")









