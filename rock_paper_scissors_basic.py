

import random 

moves = ["rock", "paper", "scissors"]

user1 =input("Enter your move: rock, paper, or scissors: ")
user2 = random.choice(moves)

if user1 == user2:
    print("It's a tie!")

elif user1 == "rock":
    if user2 == "scissors":
        print("Rock crushes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")

elif user1 == "paper":
    if user2 == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")

elif user1 == "scissors":
    if user2 == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock crushes scissors! You lose.")
