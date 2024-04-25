import random

times_guessed = 0
lifes = 0

def pick_difficulty(choice):
    if choice == "easy":
        lifes = 10
        return lifes
    else:
        lifes = 5
        return lifes

    
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
number = random.randint(1,100)
lifes = pick_difficulty(choice)

while times_guessed < lifes:
    guess = int(input("Make a guess: "))
    if guess < number:
        print('Too low!')
    elif guess > number:
        print('Too high!')
    elif guess == number:
        print('\nYou got it!')
        print(f"It only took you {times_guessed} guesses!")
        break

    times_guessed += 1

if times_guessed == lifes:
    print("\nYou lose!")
    print(f"The correct number was {number}")















