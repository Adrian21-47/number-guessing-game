from datetime import datetime, timedelta

def convert_to_12h_format(time_str, city):
    try:
        # Convert input time to datetime object
        input_time = datetime.strptime(time_str, "%H%M")

        # Convert time to 12-hour format
        twelve_hour_time = input_time.strftime("%I:%M %p")

        # Output time for the given city
        print(f"{city}: {twelve_hour_time}")

    except ValueError:
        print("Invalid time format. Please enter a valid 24-hour time.")

def main():
    try:
        # Input time in 24-hour format
        input_time_str = input("Enter the time in 24-hour format (e.g., 0034): ")

        # Convert to 12-hour format for Kenya
        convert_to_12h_format(input_time_str, "Kenya")

        cities = {
            "Kamchatka": 9,
            "Pyongyang": 9,
            "Guwahati": 5.5,
            "Hawaii": -10,
            "Buenos Aires": -3
        }

        for city, time_difference in cities.items():
            city_time = datetime.strptime(input_time_str, "%H%M") + timedelta(hours=time_difference)
            city_time_12h = city_time.strftime("%I:%M %p")
            print(f"{city}: {city_time_12h}")

    except ValueError:
        print("Invalid input. Please enter a valid time.")

if __name__ == "__main__":
    main()
