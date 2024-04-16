import random

def game():
    moves = ["rock", "paper", "scissors"]
    user1 = input("Enter your move: rock, paper, or scissors: ")
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
    else:
        print("Invalid move! Please try again.")

def play_game():
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        return
    game()
    play_game()

game()
play_game()
              
