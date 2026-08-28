import random

CHOICES = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(CHOICES)

def get_winner(player, computer):
    if player == computer:
        return "tie"
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if beats[player] == computer:
        return "player"
    return "computer"

def main():
    player = input("Choose rock, paper, or scissors: ").lower()
    if player not in CHOICES:
        print("Invalid choice. Try again.")
        return

    computer = get_computer_choice()
    print(f"Computer chose: {computer}")

    winner = get_winner(player, computer)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    main()