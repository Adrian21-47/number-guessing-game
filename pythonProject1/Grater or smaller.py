import random

def guess_the_number():
    guess_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess the number between 1 and 100: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
            elif user_guess < guess_number:
                print("Number is too low!Try again.")
            elif user_guess > guess_number:
                print("Number is too high!Try again.")
            else:
                print(f"Well done! You guessed the number {guess_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 100.")

if __name__ == "__main__":
    guess_the_number()


