print('''***********************************************************************
         __________
        /\____;;___\
            
      | /         /
      `. ())oo() .
      |\(%()*^^()^\
    
     %| |-%-------|
    % \ | %  ))   |
    %  \|%________|
    %%%%
*******************************************************************''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
choice1 = "-"

while choice1 != "0":
    choice1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \" right\" or \"0\" to leave \n -> ")
    if choice1.casefold() == "left":
        choice1 = input("choose swim or wait \n -> ")
        if choice1.casefold() == "swim":
            print("You're attacked by a trout! Game Over")
            break
        elif choice1.casefold() == "wait":
            choice1 = input("You see three doors! choose one, red, blue or yellow \n -> ")
            if choice1.casefold() == "red":
                print("You're burned by fire! Game Over")
                break
            elif choice1.casefold() == "blue":
                print("You're eaten by beasts! Game Over")
                break
            elif choice1.casefold() == "yellow":
                print("You found the treasure! Well Done")
                break
            else:
                print("Game Over!")
                break
        else:
            print("Game Over!")
            break
    elif choice1.casefold() == "right":
        print("You fall into a hole! Game Over")
        break
    else:
        print("Make a valid choice!")
