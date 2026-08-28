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
    while True:
        try:
            rounds = int(input("Best of how many rounds? (enter an odd number): "))
            if rounds > 0 and rounds % 2 == 1:
                break
            print("Please enter a positive odd number.")
        except ValueError:
            print("Please enter a valid number.")

    rounds_to_win = rounds // 2 + 1
    score = {"player": 0, "computer": 0, "tie": 0}

    while score["player"] < rounds_to_win and score["computer"] < rounds_to_win:
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

    if score["player"] >= rounds_to_win:
        print(f"You won the match {score['player']}-{score['computer']}!")
    elif score["computer"] >= rounds_to_win:
        print(f"Computer won the match {score['computer']}-{score['player']}.")
    else:
        print("Match ended early. Final score:", score)
if __name__ == "__main__":
    main()