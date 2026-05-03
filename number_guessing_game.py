import random

# Appends player name and attempts to a text file
def save_score(name, attempts):
    with open("high_scores.txt", "a") as f:
        f.write(name + "," + str(attempts) + "\n")

# Reads scores, sorts them, and displays the top 5
def show_leaderboard():
    try:
        with open("high_scores.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No scores yet!")
        return

    scores = []
    for line in lines:
        parts = line.strip().split(",")
        scores.append((parts[0], int(parts[1])))

    # Sort list by number of attempts (ascending)
    scores.sort(key=lambda x: x[1])
    
    print("\n--- LEADERBOARD (top 5) ---")
    for i, (name, score) in enumerate(scores[:5], 1):
        print(str(i) + ". " + name + " - " + str(score) + " attempts")
    print("---------------------------")

# --- Game Setup ---
print("=== Number Guessing Game ===")
player = input("Enter your name: ")

print("\nChoose difficulty:")
print("1. Easy (10 tries) | 2. Medium (7 tries) | 3. Hard (5 tries)")

# Set difficulty based on user input
choice = input("Enter 1, 2 or 3: ")
if choice == "1":
    max_tries = 10
elif choice == "2":
    max_tries = 7
else:
    max_tries = 5

number = random.randint(1, 100)
attempts = 0
guessed = False

print("\nI've picked a number between 1 and 100.")

# --- Main Logic Loop ---
while attempts < max_tries:
    guess = int(input("Your guess: "))
    attempts += 1
    remaining = max_tries - attempts

    if guess == number:
        print("Correct! You got it in " + str(attempts) + " attempt(s)!")
        guessed = True
        save_score(player, attempts)
        break
    elif guess > number:
        print("Too High! " + str(remaining) + " guesses left.")
    else:
        print("Too Low! " + str(remaining) + " guesses left.")

    # Provide Even/Odd hint after 3rd attempt
    if attempts == 3 and not guessed:
        if number % 2 == 0:
            print("Hint: The number is EVEN.")
        else:
            print("Hint: The number is ODD.")

# End of game feedback
if not guessed:
    print("Out of guesses! The number was " + str(number) + ".")

show_leaderboard()