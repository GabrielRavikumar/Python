#NUMBER GUESSING GAME
import random
lowest = 0
highest = 100
answer = random.randint(lowest,highest)
guesses = 0
is_running = True
print("----- NUMBER GUESSING GAME -----")
print()
while is_running:
    num_input = input("Enter your guess : ")
    if num_input:
        num_input = int(num_input)
        guesses += 1
        if num_input < answer:
            print("Low! Try again")
        elif num_input > answer:
            print("High! Try again")
        elif num_input == answer:
            print("CORRECT GUESS!")
            print(f"You guessed it in {guesses} tries.")
            is_running = False
