#Importing the programme that will choose the random number
import random
#Defining guess_the_number
def guess_the_number():
    guess_number = random.randint(1, 100)
    attempts = 0
#Here 'while true' will run the code indefinately till the guess number is = to the number you have guesses
    while True:
        try:
            user_guess = int(input("Guess the number between 1 and 100: "))
            attempts += 1
#Here it will output different outputs depending on what you inputed.
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
            elif user_guess < guess_number:
                print("Number is too low!Try again.")
            elif user_guess > guess_number:
                print("Number is too high!Try again.")
            #Here the code will output how many times you guessed the and the correct number.
            else:
                print(f"Well done! You guessed the number {guess_number} in {attempts} attempts.")
                break
        #When you input a number that is not an interger this will output.        
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 100.")
#The below code is what will make the code to run successfully.
if __name__ == "__main__":
    guess_the_number()


