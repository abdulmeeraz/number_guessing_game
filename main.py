import random

def number_guessing_game():
    while True:
        print("\n**********************************")
        print("* Welcome to Number Guessing Game *")
        print("***********************************")
        secret_number = random.randint(1, 100)
        attempts = 0

        limit = int(input("In how many attempts can you guess the number: "))
        print("Guess a number between 1 and 100")

        while attempts < limit:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low")
            elif guess > secret_number:
                print("Too high")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                return
        else:
            print("Guess limit reached! YOU lose the game.")
            print(f"The correct number was: {secret_number}")
        play_again = input("Play again? (Y/N): ").strip().lower()
        if play_again != 'y':
            print("Thank you for playing!🙏")
            break

number_guessing_game()
