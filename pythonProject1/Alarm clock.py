import time

def get_alarm_time():
    while True:
        try:
            alarm_time = input("Enter the alarm time (in HH:MM format): ")
            hours, minutes = map(int, alarm_time.split(":"))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                return hours, minutes
            else:
                print("Invalid time. Please enter a valid 24-hour time.")
        except ValueError:
            print("Invalid input. Please use the HH:MM format.")

def main():
    alarm_hours, alarm_minutes = get_alarm_time()
    print(f"Alarm set for {alarm_hours:02}:{alarm_minutes:02}.")

    while True:
        current_time = time.localtime()
        current_hours, current_minutes = current_time.tm_hour, current_time.tm_min

        if current_hours == alarm_hours and current_minutes == alarm_minutes:
            print("Alarm ringing! Wake up!")
            # You can add additional actions here (e.g., play a sound).
            break

        # Check every minute
        time.sleep(60)

if __name__ == "__main__":
    main()




