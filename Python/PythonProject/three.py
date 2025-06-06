import random

def guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 3

    print("Welcome to the Number Guessing Game!")
    print("You have 3 attempts to guess the number between 1 and 10.")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            if guess == number_to_guess:
                print("Congratulations! You guessed the correct number.")
                return
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

            attempts -= 1
            print(f"Attempts remaining: {attempts}")

        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")

if __name__ == "__main__":
    guessing_game()
