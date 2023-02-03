import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def winner(player, computer):
    if (player.lower() == "rock") or (player.lower() == "paper") or (player.lower() == "scissors"):
        print(f"Computer chooses: {computer}")
        if player == computer:
            return "Draw\n"
        elif player.lower() == "rock":
            if computer.lower() == "paper":
                return "Computer wins\n"
            else:
                return "Player wins\n"
        elif player.lower() == "paper":
            if computer.lower() == "scissors":
                return "Computer wins\n"
            else:
                return "Player wins\n"
        elif player.lower() == "scissors":
            if computer.lower() == "rock":
                return "Computer wins\n"
            else:
                return "Player wins\n"
    else:
        return "Please enter a valid choice\n"


def start():
    print("Type \"exit\" to return\n")
    x = True
    while x:
        choices = get_choices()
        if choices["player"].lower() == "exit":
            x = False
        else:
            win = winner(choices["player"], choices["computer"])
            print(win)


start()
