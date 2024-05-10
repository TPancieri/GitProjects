import random, os
from higerlowerdata import data

logo = """
   ▄█    █▄     ▄█     ▄██████▄     ▄█    █▄       ▄████████    ▄████████       ▄██████▄     ▄████████       ▄█        ▄██████▄   ▄█     █▄     ▄████████    ▄████████ 
  ███    ███   ███    ███    ███   ███    ███     ███    ███   ███    ███      ███    ███   ███    ███      ███       ███    ███ ███     ███   ███    ███   ███    ███ 
  ███    ███   ███▌   ███    █▀    ███    ███     ███    █▀    ███    ███      ███    ███   ███    ███      ███       ███    ███ ███     ███   ███    █▀    ███    ███ 
 ▄███▄▄▄▄███▄▄ ███▌  ▄███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀      ███    ███  ▄███▄▄▄▄██▀      ███       ███    ███ ███     ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███▀▀▀▀███▀  ███▌ ▀▀███ ████▄  ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀        ███    ███ ▀▀███▀▀▀▀▀        ███       ███    ███ ███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    ███   ███    ███    ███   ███    ███     ███    █▄  ▀███████████      ███    ███ ▀███████████      ███       ███    ███ ███     ███   ███    █▄  ▀███████████ 
  ███    ███   ███    ███    ███   ███    ███     ███    ███   ███    ███      ███    ███   ███    ███      ███▌    ▄ ███    ███ ███ ▄█▄ ███   ███    ███   ███    ███ 
  ███    █▀    █▀     ████████▀    ███    █▀      ██████████   ███    ███       ▀██████▀    ███    ███      █████▄▄██  ▀██████▀   ▀███▀███▀    ██████████   ███    ███ 
                                                               ███    ███                   ███    ███      ▀                                               ███    ███ 
"""

print(logo)

# makes celeb_list a list of dicts containing the info of all accounts
celeb_list = data

# start player score at zero and game_over as False
score = 0
game_over = False


def information(celeb: dict):
    # since random.sample returned the dict we can just iterate over every item and assign it to a variable
    for key, value in celeb.items():
        if key == 'name':
            celeb_name = value
        elif key == 'follower_count':
            followers = value
        elif key == 'description':
            desc = value
        elif key == 'country':
            country = value
    # we then return this variables
    return celeb_name, followers, desc, country


def larger_following(follows_a, follows_b):
    # since the follower_count(or followers) is an int we can just compare them to see who has more
    if follows_a > follows_b:
        bigger_account = 'A'
    elif follows_a < follows_b:
        bigger_account = 'B'
    elif follows_a == follows_b:
        bigger_account = 'Either'
    # and return the answer, A is bigger, B is bigger, or they are the same (Either)
    return bigger_account


while not game_over:
    # picks at random, two different(can't be the same) dicts(account) from the celeb_list list
    # it picks a random key, and it will give the value back, so the return from this will be the dict we want to
    # iterate over later, not the index and the key, like enumerate would give
    choice_A, choice_B = random.sample(celeb_list, 2)

    # gets celeb name, follow count, description and country from the information function
    # assign them to variables _A and _B
    celeb_A, followers_A, desc_A, country_A = information(choice_A)
    celeb_B, followers_B, desc_B, country_B = information(choice_B)

    # start the game proper
    print("Which do you think has more followers?")
    print(f"{celeb_A} who is a {desc_A} from {country_A}")
    print("or")
    print(f"{celeb_B} who is a {desc_B} from {country_B}")

    # get user choice from input
    user_choice = input(f"Choose A for {celeb_A} and B for {celeb_B} \n >").upper()

    # see which account has a bigger following using the larger_following function
    bigger = larger_following(followers_A, followers_B)

    # if the user choose the bigger account, or they have the same amount of followers they get a point
    # and can keep going
    if bigger == user_choice or bigger == 'Either':
        print("You got it!")
        print(f"{celeb_A} has {followers_A} followers, while {celeb_B} has {followers_B} followers")
        score += 1
        print(f"\n Your score is: {score}\n")
    # else, if the user choose the smaller account they lose the game and can't keep going
    else:
        print("\nSorry! That's Wrong!")
        print(f"{celeb_A} has {followers_A} followers, while {celeb_B} has {followers_B} followers")
        game_over = True

# after the game ends we show the user their final score
os.system('cls')
print(f"\n Your final score is {score}")