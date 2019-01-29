# A Pixelation's iteration of Ship, Captain, Crew inspired by Life is Strange 2 - Episode 2
# After playing this episode, I was inspired to recreate the game in Python - the current programming language I am self-learning.

import random

# This will roll the n number of dice available.
def roll(dice) :
    dice_rolls = []
    for i in range(dice) :
        output = random.randint(1, 6)
        i += 1
        dice_rolls.append(output)
    return dice_rolls

# This checks if you rolled a ship or 6.
def ship_check(roll) :
    for n in roll :
        if n == 6 :
            return True
    return False

# This checks if you rolled a captain or 5.
def captain_check(roll) :
    for n in roll :
        if n == 5 :
            return True
    return False

# This checks if you rolled a crew or 4.
def crew_check(roll) :
    for n in roll :
        if n == 4 :
            return True
    return False

# This consolidates all three checks together for a streamlined return.
def scc_check(roll) :
    hs = ship_check(roll)
    hc = captain_check(roll)
    hcr = crew_check(roll)
    return hs, hc, hcr

# After you've rolled a 'pirate ship' aka 6, 5, 4; this will remove them from your loot list.
def remove_pirate_ship(roll) :
    if len(roll) == 6 :  
        roll.remove(6)
        roll.remove(5)
        roll.remove(4)
    elif len(roll) == 5 :
        roll.remove(5)
        roll.remove(4)
    elif len(roll) == 4 :
        roll.remove(4)
    return roll

# This function will find the loot in the list, and determine if it is valid or not.
def find_dice(roll, player_choice) :
    for n in roll :
        if player_choice == n :
            score.append(n)
            return score
    print("That is not one of the dice!")
    return False

# Game prompt that also increases the counter.
def game_prompt(i) :
    i += 1
    input("> ")
    return i

# If you have not rolled a pirate ship, then this function will run and end the game.
def final_roll_notice(i) :
    if i == 3 :
        print("You did not roll enough to collect, thanks for playing!")

# This is the overall comprehensive loot selector function
# It takes your roll 'roll' and current score 'current_score'
# First it will run the rool through the remove_pirate_ship function
# Second it will print the loot list, and receive an input for loot.
# Third it will take the input from the user and run it through find_dice
# Fourth it will append the selected integer to the user's current_score list.
# Finally, it will return the score.
def select_score(roll, current_score) :
    final_sorted_list = remove_pirate_ship(roll)
    print(f"Loot: {final_sorted_list}")
    player_selection = int(input("> "))
    score = find_dice(final_sorted_list, player_selection)
    current_score.append(score)
    return current_score

game_intro = """\n---Welcome to A Pixelation's Ship, Captain, and Crew dice game!---\n
You have 6 dice and roll a total of 3 times. 
The person with the highest score after 3 rolls is the winner."""

game_rules = """
---Quick Rules---
6 = Ship
5 = Captain
4 = Crew

You must have a Ship, before you can have a Captain.
You must have a Captain before you can have a Crew.
You must have a Ship, Captain, and Crew before you can collect loot. 

You do not have to collect all dice on a roll and choose to roll again.
By default, you will pick up everything on your last roll."""

has_ship = False
has_captain = False
has_crew = False
pirate_ship = False

prompt = "> "
score = []
pr = []
nDice = 6
i = 1

print(game_intro)
print(game_rules)
print("Press any key to begin.")
input(prompt)

while i <= 3 :
    if pirate_ship == False :
        pr = roll(nDice)
        if has_ship == False :
            has_ship, has_captain, has_crew = scc_check(pr)
        elif has_ship == True and has_captain == True :
            has_crew = crew_check(pr)
        elif has_ship == True :
            has_captain = captain_check(pr)
            has_crew = crew_check(pr)

        print(f"You rolled: {pr}.")

        if has_ship == True and has_captain == True and has_crew == True :
            pirate_ship = True
            if i == 3 :
                print("\nYou rolled a full stack on the final toss. Your loot will be automatically collected.") 
            
            print("\nYou rolled a full stack! You may select your loot or re-roll.")
            loot_or_roll = input("(L/R) :").upper()
            nDice = 3

            if loot_or_roll == "L" :
                score = select_score(pr, score)
                i += 1
            else :
                print("Rerolling...\n")
                i = game_prompt(i)

        elif has_ship == True and has_captain == True and has_crew == False :
            final_roll_notice(i)
            nDice = 4

            print("\nYou do not have a crew. Please roll again.")
            i = game_prompt(i)

        elif has_ship == True and has_captain == False and has_crew == True :
            final_roll_notice(i)
            nDice = 5

            print("\nYou do not have a captain for the crew. Please roll again.")
            i = game_prompt(i)
        
        elif has_ship == True and has_captain == False and has_crew == False :
            final_roll_notice(i)
            nDice = 5

        elif has_ship == False :
            print("\nYou do not have a ship to claim a captain or crew. Please roll again.")
            i = game_prompt(i)

    elif pirate_ship == True :
        pr = roll(nDice)
        print(f"You rolled: {pr}.")
        if i == 3 :
            print("\nYou rolled a full stack on the final toss. Your loot will be automatically collected.") 
            
        loot_or_roll = input("(L/R) :").upper()
        if loot_or_roll == "L" :
            score = select_score(pr, score)
            i += 1
        else :
            i += 1

