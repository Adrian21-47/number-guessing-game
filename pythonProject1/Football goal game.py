def calculate_goals():
    try:
        # Get the number of matches played
        num_matches = int(input("Enter the number of matches played: "))

        total_goals = 0

        for match in range(1, num_matches + 1):
            goals_scored = int(input(f"Enter the number of goals scored in match {match}: "))
            total_goals += goals_scored

        average_goals = total_goals / num_matches if num_matches > 0 else 0

        print("\nTournament Summary:")
        print(f"Total goals scored: {total_goals}")
        print(f"Average goals per match: {average_goals:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")



calculate_goals()
