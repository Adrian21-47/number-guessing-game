def unlock_phone():
    password = "1234"  # Replace "1234" with your desired password
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        pin = input("Enter your password: ")
        if pin == password:
            print("Access granted")
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"Incorrect password. You have {remaining_attempts} attempts remaining.")

    if attempts == max_attempts:
        print("Maximum attempts reached. Phone locked.")

unlock_phone()