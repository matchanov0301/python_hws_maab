import random

while True:
    number = random.randint(1, 100)
    attempts = 10
    print("I have chosen a number between 1 and 100. Try to guess it!")

    for _ in range(attempts):
        try:
            guess = int(input("Enter your guess: "))

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("You guessed it right!")
                break  # Exit the loop if guessed correctly
        except ValueError:
            print("Invalid input! Please enter a number.")

    else:
        print("You lost. Want to play again? (Y/YES/y/yes/ok)")
        replay = input().strip().lower()
        if replay not in ['y', 'yes', 'ok']:
            break  # Exit the game if the user doesn't want to play again
