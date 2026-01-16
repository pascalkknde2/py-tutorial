import random

def get_hint(diff):
    """Returns a hint message based on difference."""
    if diff == 0:
        return ""
    elif diff <= 2:
        return "🔥 Very close!"
    elif diff <= 5:
        return "👍 Close!"
    elif diff <= 10:
        return "😐 Far."
    else:
        return "❄️ Very far."

def play_game():
    print("\n=== NUMBER GUESSING GAME Perfect ===")
    print("Select difficulty:")
    print("1. Easy   (1–10, 7 attempts)")
    print("2. Medium (1–20, 5 attempts)")
    print("3. Hard   (1–50, 5 attempts)")

    # Difficulty selection
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice in ("1", "2", "3"):
            break
        print("Invalid choice. Try again.")

    if choice == "1":
        max_num = 10
        attempts = 7
    elif choice == "2":
        max_num = 20
        attempts = 5
    else:
        max_num = 50
        attempts = 5

    secret = random.randint(1, max_num)
    score = 0

    print(f"\nI'm thinking of a number between 1 and {max_num}.")
    print(f"You have {attempts} attempts.\n")

    for trial in range(1, attempts + 1):
        # Input validation
        while True:
            guess_input = input(f"Attempt {trial}/{attempts} — Your guess: ")
            try:
                guess = int(guess_input)
                break
            except ValueError:
                print("⚠️ Please enter a valid number.")

        diff = abs(guess - secret)

        if guess == secret:
            print("🎉 Correct! You guessed the number!")
            score = attempts - trial + 1  # Higher score for fewer attempts
            break

        # Too high or too low
        if guess > secret:
            print("Too high!")
        else:
            print("Too low!")

        # Smart hints
        print(get_hint(diff))

        if trial < attempts:
            print("Try again...\n")

    else:
        print(f"\n❌ Out of attempts! The number was {secret}.")

    print(f"Your score this round: {score}\n")
    return score


# Game loop with replay and total score
total_score = 0

while True:
    total_score += play_game()
    again = input("Play again? (y/n): ").lower().strip()
    if again != "y":
        break

print(f"\n🎮 Total Score: {total_score}")
print("Thanks for playing!")
