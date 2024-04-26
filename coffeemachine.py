MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Turn off the Coffee Machine by entering “off” to the prompt.
# ->End execution
def turn_off():
    print("Shutting down...")
    exit()


# turn_off() -> Working!


# Print report.
# ->Show the current resource values, e.g. Water: 0, Milk:0, Coffe:0, Money:0
def report():
    for resource, quantity in resources.items():
        print(f"{resource} : {quantity}")


# report() -> Working!


# Check if resources are sufficient.
# ->After drink is chosen check to see if it's possible to make that drink.
def check_resources(drink):
    needed_amount: dict = {}
    chosen_drink = MENU[drink]
    for key in chosen_drink:
        if key == 'ingredients':
            ingredient_list = chosen_drink[key]
            for item, amount in ingredient_list.items():
                needed_amount[item] = amount
    current_amount: dict = {}
    for item, quantity in resources.items():
        current_amount[item] = quantity
    # Up to here we have two dict, current_amount and needed_amount with the keys being the ingredient names and
    # the values being the amount (needed or in stock)

    # Now we compare to see if there are enough ingredients in the machine to make the drink
    for key in needed_amount.keys():
        item_needed = needed_amount[key]
        item_stocked = current_amount[key]
        if item_needed > item_stocked:
            print(f"Sorry, there's not enough {key}")
            enough = False
        else:
            enough = True
    return enough


# Process coins.
# ->Coin types: penny (1 cent), Nickel (5 cents), Dime(10 cents), Quarter(25 cents)
def process_coin(penny, nickel, dime, quarter):
    amount_paid = 0
    if penny != 0:
        amount_paid += 0.01 * penny
    if nickel != 0:
        amount_paid += 0.05 * nickel
    if dime != 0:
        amount_paid += 0.10 * dime
    if quarter != 0:
        amount_paid += 0.25 * quarter
    return amount_paid


# ->If there are sufficent resources, prompt the user to insert coins.
# ->Then calculate the monetary value of the coins inserted


# Check transaction successful.
# ->Check if the user inserted enough money for the coffe.
def check_transaction(amount_paid, drink_price):
    # ->If not enough: "Sorry that's not enough. Money refunded"
    if amount_paid < drink_price:
        payment_accepted = False
        print("Sorry that's not enough. Money refunded")
        return payment_accepted
    # ->If enough: drink cost gets added to profit
    elif amount_paid == drink_price:
        payment_accepted = True
        resources["Money"] = amount_paid
        return payment_accepted
    # ->If too much: machine offers change, rounded to 2 decimal places . drink cost gets added to profit
    elif amount_paid > drink_price:
        payment_accepted = True
        change = round(amount_paid - drink_price, 2)
        print(f"You have ${change} of change")
        return payment_accepted


# Make coffe
# ->If transaction is successful and there are enough resources
#TODO fix this function, can copy over some of the code from the check resources
def make_coffe(drink, payment):
    if payment:
        # ->Make the drink the user selected
        # ->Then the ingredients used should be deducted from the coffe machine resources
        to_remove = {}
        for item, values in MENU[drink]:
            to_remove[item] = values
        i = 0
        resources["water"] = resources["water"] - to_remove["water"]
        resources["milk"] = resources["milk"] - to_remove["milk"]
        resources["coffee"] = resources["coffee"] - to_remove["coffe"]
        # ->Once resources have been deducted, tell the user "Here is you {drink}. Enjoy!"
        print(f"Here is your {drink}. Enjoy!")


# Prompt user by asking "What would you like? (espresso/latte/cappuccino)"
def drink_menu():
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # -> Check the user input to see what's next.
    if drink_choice in MENU:
        enough = check_resources(drink_choice)
        drink_info = MENU[drink_choice]
        for key, value in drink_info.items():
            if key == 'cost':
                drink_cost = drink_info[key]
        if enough:
            print(f"The price for {drink_choice} is {drink_cost}")
            penny_amount = float(input(f"How many penny (s)?"))
            nickel_amount = float(input(f"How many nickel (s)?"))
            dime_amount = float(input(f"How many dime (s)?"))
            quarter_amount = float(input(f"How many quarter (s)?"))
            amount_paid = process_coin(penny_amount, nickel_amount, dime_amount, quarter_amount)
            payment_accepted = check_transaction(amount_paid, drink_cost)
            if payment_accepted:
                make_coffe(drink_choice, payment_accepted)
    elif drink_choice == "off":
        turn_off()
    else:
        print("Please choose a valid option")
    # ->Prompt should show everytime an action is completed


drink_menu()
