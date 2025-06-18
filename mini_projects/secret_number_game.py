import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Give the user 5 attempts to guess the number
for attempt in range(1, 6):
    guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed it right!")
        break
    elif guess < secret_number:
        print("Too low. Try a higher number.")
    else:
        print("Too high. Try a lower number.")
else:
    print(f"\nSorry! You've used all your attempts. The number was {secret_number}.")
