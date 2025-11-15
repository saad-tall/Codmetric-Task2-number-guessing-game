import random

def number_guessing_game():
    # Generate random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            user_input = int(input("Enter your guess: "))
            attempts += 1
            
            if user_input < number_to_guess:
                print("Too low! 📉 Try again.")
            elif user_input > number_to_guess:
                print("Too high! 📈 Try again.")
            else:
                print(f"🎉 Correct! The number was {number_to_guess}.")
                print(f"You guessed it in {attempts} attempts. 🧠")
                break

        except ValueError:
            print("🚫 Invalid input! Please enter a valid integer.")

# Run the game
number_guessing_game()