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
    score = {"player": 0, "computer": 0, "tie": 0}

    while True:
        player = input("Choose rock, paper, or scissors (or 'quit'): ").lower()
        if player == "quit":
            break
        if player not in CHOICES:
            print("Invalid choice. Try again.")
            continue

        computer = get_computer_choice()
        print(f"Computer chose: {computer}")

        winner = get_winner(player, computer)
        if winner == "tie":
            print("It's a tie!")
        else:
            print(f"{'You' if winner == 'player' else 'Computer'} win!")
        score[winner] += 1

        print(f"Score — You: {score['player']}, Computer: {score['computer']}, Ties: {score['tie']}\n")

    print("Final score:", score)
    print("Thanks for playing!")

if __name__ == "__main__":
    main()