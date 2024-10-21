import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")

choose_random = random.randint(1,100)
print(f"I'm thinking of a number between 1 and 100.")

attempts_easy = 10
attempts_hard = 5

choose_difficulty = input("Choose a Difficulty. Type 'easy' or 'hard': ").lower()

if choose_difficulty == "easy":
    attempts = 10
else:
    attempts = 5

game = False

while not game:
    print(f"You have {attempts} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    if guess < choose_random:
        print("Too low")
        print("Guess again")
    elif guess > choose_random:
        print("Too high")
        print("Guess again")
    elif guess == choose_random:
        print(f"You got it!, The answer was {choose_random}")
        game = True

    if guess != choose_random:
        attempts -= 1

        if attempts == 0:
            print("You've run out of guesses. You lose.")
            game = True

      
