def main():
    # Initialize player's score
    score = 101
    throws = 0

    print("Welcome to the Darts Game!")
    print("You start with 101 points.Enter your score after each throw.")
    # Game loop
    while score > 0:
        try:
            # Get the player's score for the throw
            throw_score = int(input("Enter your score for the throw: "))

            # Validate the input
            if throw_score < 0 or throw_score > 20:
                print("Invalid score. Please enter a valid score between 0 and 20.")
                continue

            # Update the player's score
            score -= throw_score
            throws += 1

            # Display the current score
            print(f"Points needed to reach zero: {score}")

        except ValueError:
            print("Invalid input. Please enter a valid integer score.")

    # Game over
    print(f"Congratulations! You reached zero or below in {throws} throws.")

if __name__ == "__main__":
    main()