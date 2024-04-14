def encode(shift):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    encoded = [(chr(((ord(message[i]) - ord('a') + shift) % 26) + ord('a'))) for i in range(len(message))]
    return "".join(encoded)

def decode(shift):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    decoded = [(chr(((ord(message[i]) - ord('a') - shift) % 26) + ord('a'))) for i in range(len(message))]
    return "".join(decoded)


choice = input("Type 'encode' to encrypt or 'decode' to decrypt: ")
if choice == None or choice == "":
    print("Please enter a valid choice.")
elif choice == "encode":
    message = input("Enter the message to encrypt: ")
    if message == None or message == "":
        print("Please enter a valid message.")        
    if not message.isalpha():
        print("Please enter a valid message.")    
    message = message.lower()
    num = int(input("Enter the shift amount (1-25): "))
    if num < 1 or num > 25:
        print("Please enter a valid shift amount (1-25).")  
    print("The encrypted message is: " + encode(num))
elif choice == "decode":
    message = input("Enter the encrypted message: ")
    num = int(input("Enter the shift amount (1-25): "))
    print("The decrypted message is: " + decode(num))
    
else:
    print("Please enter a valid choice.")
