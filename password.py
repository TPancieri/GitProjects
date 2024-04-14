import random
letters = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q","R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
numbers = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
symbols = [ "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ",", ".", "<", ">", "/", "?", "~" ]

print("Welcome to the Password Generator!")

letters_choice = int(input("How many letters?\n"))
numbers_choice = int(input("How many numbers?\n"))
symbols_choice = int(input("How many symbols?\n"))

password = []

for character in range(1, letters_choice + 1):
    password += random.choice(letters)

for character in range(1, numbers_choice + 1):
    password += random.choice(numbers)

for character in range(1, symbols_choice + 1):
    password += random.choice(symbols)

# shuffle password
random.shuffle(password)

password_str = ""

for char in password:
    password_str += char

print(f"Your password is: {password_str}")


