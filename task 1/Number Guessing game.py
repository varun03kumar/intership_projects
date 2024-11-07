import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Try to guess it!")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

guess_number()
