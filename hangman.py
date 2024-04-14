import random
possible_words = ["beekeeper", "fireman", "doctor", "animal", 'building', "potato", "goku"]

rand = random.randint(0, len(possible_words) - 1)
word = possible_words[rand]
guess = ""
counter = 0
guessed_chars = []

print(word)

while guess != word and counter < 6:
    print(f"You have {6 - counter} guesses left.")
    guess = input("Enter your guess: ").lower()
    counter += 1
    for char in word:
        if char in guess and char in word:
            guessed_chars.append(char)
            print(f"{char}", end=" ")
        elif char in guessed_chars:
            print(f"{char}", end="")
        else:
            print("_", end=" ")
    print()

if guess == word:
    print("You win!")
else:
    print("You lose!")
print(f"The word was {word}.")
print("It took you a total of {counter} guesses.")