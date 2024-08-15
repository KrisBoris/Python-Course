#Rock, paper, scissors game
import random

options = ["rock", "paper", "scissors"]

def get_choices():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def get_computer_choice():
    return random.choice(options)

def get_player_choice():
    player_choice = input("Enter your choice (rock, paper, scisseors): ")
    return player_choice

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}\n")
    if player == computer:
        return "It's a tie."
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors. You win."
        else:
            return "Paper covers rock. You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock. You win."
        else:
            return "Scissors cuts paper. You lose."
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors. You lose."
        else:
            return "Scissors cuts paper. You win."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)