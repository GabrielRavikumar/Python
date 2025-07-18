import random
print("ROCK PAPER SCISSORS GAME")
print()
print("r - Rock, p - Paper, s - Scissor")
user_input = input("Choose (r/p/s): ").lower()
input_map = {'r': 'Rock', 'p': 'Paper', 's': 'Scissor'}
if user_input not in input_map:
    print("Invalid input! Please choose r, p, or s.")
else:
    user_choice = input_map[user_input]
    options = ("Rock", "Paper", "Scissor")
    computer_choice = random.choice(options)
    print(f"You     : {user_choice}")
    print(f"Computer: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissor") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissor" and computer_choice == "Paper")
    ):
        print(f"{user_choice} beats {computer_choice}")
        print("You Win!")
    else:
        print(f"{computer_choice} beats {user_choice}")
        print("Computer Wins!")
