import os
bidders = {}

def intro ():
    name = input("What's your name?: ")
    bid = int(input("What's  your bid?: "))
    bidders.update({name: bid})

def tally(bidders):
    highest_bid = max(bidders.values())
    highest_bidder = max(bidders, key=bidders.get)
    print(f"The winner of the auction is {highest_bidder} with a bid of {highest_bid}")


print("Welcome to the secret auction program") 
while True:
    intro()
    others = input("Are there any other bidders?: ")
    if others.lower() == "yes":
        os.system('cls')
        continue
    elif others.lower() == "no":
        print("The auction is now closed")
        tally(bidders)
        break
    else:
        print("Please answer with yes or no")
