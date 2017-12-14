# Authors: Kevin Quijalvo and Erik Kozy
# Date: November 29 2017
# File Name: pokemon.py
# Description: Very small pokemon RPG

import random # Import the random library

# User stats
name = ''
money = 500   # Set the players money (They will start with 500)
inventory = ['Pokèball', 'Pokèball']  # Set user's inventory

# Stats of user's pokemon
userpartynames = [] # Create a list of the names of the pokemon that the user has
userpartytypes = [] # Create a list of the types of every pokemon that the user has
userpartyattacks = [] # Create a list of attacks for each pokemon that the user has
userpartydmg = [] # Create a list of the damage values for each move of every pokemon that the user has
userpartypp = [] # Create a list of PP values for each move of every pokemon that the user has
userpartymaxpp = [] # Create a list of the max PP values for each move of every pokemon that the user has
userpartyhp = [] # Create a list of the current hp values for each pokemon that the user has
userpartymaxhp = [] # Create a list of the max hp values for each pokemon that the user has

# Stats of enemy's pokemon
enemypartynames = [] # Create a list of the names of the pokemon that the enemy has
enemypartytypes = [] # Create a list of the types of every pokemon that the enemy has
enemypartyattacks = [] # Create a list of attacks for each pokemon that the enemy has
enemypartydmg = [] # Create a list of the damage values for each move of every pokemon that the enemy has
enemypartyhp = [] # Create a list of the current HP values fot each pokemon that the enemy has
enemypartymaxhp = [] # Create a list of the max HP values for each pokemon that the enemy has

# Stats of all pokemon
pokemonnames = ['Bulbasaur', 'Charmander', 'Squirtle', 'Rattata', 'Pidgey', 'Geodude', 'Onix', 'Staryu', 'Starmie', 'Rhyhorn', 'Nidoran♂', 'Nidoran♀', 'Caterpie'] # List of the names of every pokemon
pokemontypes = ['Grass', 'Fire', 'Water', 'Normal', 'Flying', 'Rock', 'Rock', 'Water', 'Water', 'Rock', 'Poison', 'Poison', 'Bug'] # List of every pokemon's type
pokemonattacks = [['Vine Whip', 'Razor Leaf'], ['Ember', 'Flame Burst'], ['Bubble', 'Water Gun'], ['Tackle'], ['Gust'], ['Rock Smash', 'Rock Slide'], ['Rock Slide', 'Earthquake'], ['Bubble', 'Water Gun'], ['Bubble', 'Surf'], ['Rock Smash', 'Earthquake'], ['Poison Sting', 'Poison Jab'], ['Poison Sting', 'Poison Jab'], ['Tackle']] # List of the attacks of every pokemon
pokemondmg = [[3, 5], [5, 7], [3, 5], [3], [3], [1, 3], [3, 4], [2, 4], [2, 5], [2, 5], [1, 4], [1, 4], [3]] # List of the default damage values for the attacks of every pokemon
pokemonpp = [[30, 10], [35, 20], [30, 10], [30], [40], [20, 10], [20, 10], [20, 20], [20, 10], [30, 10], [40, 15], [40, 15], [40]] # List of the default PP values for the attacks of every pokemon
pokemonhp = [65, 65, 65, 20, 20, 35, 45, 40, 50, 50, 20, 20, 15] # List of the default HP values of every pokemon

# Menu Options
battledecisions = ['Attack', 'Open Inventory', 'Change Pokemon', 'Flee'] # Create a list of decisions that the user can make during battle
verification = ['Yes', 'No'] # List of options when asking for the user to verify their decisions
shop = ['Pokèball', 'Potion', 'Elixir']   # List of items that the user can buy in the PokeMart by default

def setGender():   # Define setGender as a function
    genders = ['Boy', 'Girl'] # Create a list of available genders that the user can choose

    printTextBox('Are you a boy or a girl?') # Ask for the user's gender
    printOptionList(genders) # Print the list of gender that the user can choose
    choice = getUserDecision('Choose a gender', 'Press 1 if you are a boy, 2 if you are a girl', genders) # Ask for the index of the user's decision, then store it

    return genders[choice]   # Return the user's gender to the main code

def setName(): # Define setName as a function
    printTextBox('What is your name?') # Ask the user for their name
    alias = input('Enter a name: ')     # Print Oak's speech

    return alias    # Return the user's name to the main code

def starterPick():  # Define starterPick as a function
    starters = ['Bulbasaur', 'Charmander', 'Squirtle'] # Create a list of starter pokemon that the user can choose

    printTextBox('Choose your starter') # Ask the user for their starter
    printOptionList(starters) # Print the list of starter pokemon that the user can choose
    choice = getUserDecision('Choose a starter', 'Type 1, 2, or 3 to choose the pokemon that you will start the game with', starters) # Ask for the index of the user's choice, then store it

    return starters[choice] # Return the starter pokemon that the user chose

def buyItem(options, current_pokedollars):   # Define pokeMartGive as a function
    options.append('Quit the shop')  # Add quit the shop to the list to show
    items = [] # Create a list of items that the user will buy
    for index in range(0, len(options)):
        print(str(index + 1) + '. ' + str(options[index]), end='') # Print a list of the available items that the user can buy

        if options[index] == 'Pokèball':
            print(' - ¥200') # Print the price of a Pokèball beside the "Pokèball" listing

        elif options[index] == 'Potion':
            print(' - ¥150') # Print the price of a Potion beside the "Potion" listing

        elif (options[index] == 'Super Potion') or (options[index] == 'Elixir'):
            print(' - ¥300') # Print the price of a Super Potion / Elixir beside their listings

        elif options[index] == 'Super Elixir':
            print(' - ¥600') # Print the price of a Super Elixir beside the "Super Elixir" listing

    print('') # Print an empty line after all the listings

    shopflag = True
    while shopflag == True:
        print('Your Money: ' + str(current_pokedollars)) # Print the user's current pokedollar count
        buy = getUserDecision('What do you want to buy?', 'Pokèballs allow you to catch pokemon, Potions heal your current pokemon by 10 HP, Elixirs restore the PP values of all your pokemons attacks.', options)   # Take user's input on what to buy

        if (options[buy] == 'Pokèball') and (current_pokedollars < 200):  # Check if user bought a Pokèball
            print('You do not have enough money for a Pokèball!') # If the user tries to buy a Pokèball, but has less than ¥200, then tell the user that they can't buy it

        elif (options[buy] == 'Pokèball') and (current_pokedollars >= 200):
            current_pokedollars = decrementValue(current_pokedollars, 200)    # Subtract the cost from the user's balance
            items.append(options[buy]) # Add the item that the user chose to the list of bought shopping items
            print('You bought a Pokèball!')     # Tell user what they bought

        elif (options[buy] == 'Potion') and (current_pokedollars < 150):  # Check if user bought a potion
            print('You do not have enough money for a Potion!') # If the user tries to buy a Potion, but has less than ¥150, then tell the user that they can't buy it

        elif (options[buy] == 'Potion') and (current_pokedollars >= 150):  # Check if user bought a potion
            current_pokedollars = decrementValue(current_pokedollars, 150)    # Subtract the cost from the user's balance
            items.append(options[buy]) # Add the item that the user chose to the list of bought shopping items
            print('You bought a Potion!')   # Tell user what they bought

        elif (options[buy] == 'Super Potion') and (current_pokedollars < 300):  # Check if user bought a Super Potion
            print('You do not have enough money for a Super Potion!') # If the user tries to buy a Super Potion, but has less than ¥300, then tell the user that they can't buy it

        elif (options[buy] == 'Super Potion') and (current_pokedollars >= 300):  # Check if user bought a potion
            current_pokedollars = decrementValue(current_pokedollars, 300)    # Subtract the cost from the user's balance
            items.append(options[buy]) # Add the item that the user chose to the list of bought shopping items
            print('You bought a Super Potion!')   # Tell user what they bought

        elif (options[buy] == 'Elixir') and (current_pokedollars < 300):  # Check if user bought an elixir
            print('You do not have enough money for an Elixir!') # If the user tries to buy an Elixir, but has less than ¥300, then tell the user that they can't buy it

        elif (options[buy] == 'Elixir') and (current_pokedollars >= 300):  # Check if the user bought an elixir
            current_pokedollars = decrementValue(current_pokedollars, 300) # Subtract the cost from user's balance
            items.append(options[buy]) # Add the item that the user chose to the list of bought shopping items
            print('You bought an Elixir!')   # Tell the user what they bought

        elif (options[buy] == 'Super Elixir') and (current_pokedollars < 600):  # Check if user bought a super elixir
            print('You do not have enough money for a Super Elixir!') # If the user tries to buy a Super Elixir, but has less than ¥600, then tell the user that they can't buy it

        elif (options[buy] == 'Super Elixir') and (current_pokedollars >= 600):  # Check if the user bought an elixir
            current_pokedollars = decrementValue(current_pokedollars, 600)      # Subtract the cost from user's balance
            items.append(options[buy]) # Add the item that the user chose to the list of bought shopping items
            print('You bought a Super Elixir!')  # Print to user what they bought

        else:
            shopflag = False # Set the flag to False to exit the shop

    options.remove('Quit the shop') # Remove "Quit the shop" as an option when they leave the Pokemart
    results = [current_pokedollars] # Put the user's remianing currency into a list
    results.extend(items) # Add the items they bought into the list
    return results  # Return the user's money, and the items they bought to the main code

def printTextBox(message):
    textboxlength = 50 # Set all text boxes to be 50 characters long

    print('') # Print an empty line
    print('█' + '▀' * textboxlength + '█') # Print the left side of the text box, the top of the text box, and the right side of the text box
    print('█' + ' ' * textboxlength + '█') # Print the left side of the text box, and empty line, and the right side of the text box

    while len(message) > textboxlength:
        line = message[0:textboxlength] # Cut out a section of the message that is as long as the specified text box length
        line = line[0:line.rfind(' ')] # Cut the current line at the last instance of a space before it extends past the text box length
        message = message[len(line):] # Cut out the rest of the message
        message = message.lstrip(' ') # Strip any leading spaces from the message
        print('█' + line.center(textboxlength, ' ') + '█') # Print the left side of the text box, the current line of the message, and the right side of the text box

    print('█' + message.center(textboxlength, ' ') + '█') # Print the left side of the text box, the rest of the message, and the right side of the text box
    print('█' + ' ' * textboxlength + '█') # Print the left side of the text box, and empty line, and the right side of the text box
    print('█' + '▄' * textboxlength + '█') # Print the left side of the text box, the bottom of the text box, and the right side of the text box
    print('') # Print an empty line

def printOptionList(optionlist):
    for index in range(0, len(optionlist)):
        print(str(index + 1) + '. ' + optionlist[index]) # Print all of the variables in the given list

def getUserDecision(inputmessage, helpmessage, optionlist):
    while True:
        try:
            index = input(inputmessage + ' (Enter a number): ') # Ask for the user's decision as a number, then store it
            print('') # Print an empty line
            index = int(index) - 1 # Cast the integer value of the user's input, then store it
            optionlist[index] # Check to see if an option exists at the specified index
            break # Break the loop

        except ValueError:
            if (index == 'h') or (index == 'H'):
                printTextBox(helpmessage) # Print a help message if the user presses 'h'

            else:
                print('That is not a valid decision!') # If the user does not enter an integer, tell the user that their input is invalid

        except IndexError:
            print('There is no option at that index!') # If the user enters an index that does not exist within the decision list, tell the user that their input is invalid

    return index # Return the index of their decision

def getBotDecision(optionlist):
    index = random.randint(0, len(optionlist) - 1) # Select a random move by generating a random index between 0 and the number of options that the enemy has
    return index # Return the index of the enemy's decision

def decrementValue(currentvalue, decrementamount):
    if (currentvalue - decrementamount) < 0:
        currentvalue = 0 # If the current value goes below 0 after decrementing, then set the current value to 0

    else:
        currentvalue -= decrementamount # If the current value doesn't go below 0 after decrementing, then just subtract from the current value

    return currentvalue # Return the new value

def incrementValue(maximumvalue, currentvalue, incrementamount):
    if (currentvalue + incrementamount) > maximumvalue:
        currentvalue = maximumvalue # If the current value exceeds the max value after incrementing, then set the current value to the max value

    else:
        currentvalue += incrementamount # If the current value doesnt exceed the max value after incrementing, then just add to the current value

    return currentvalue # Return the new value

def printPokemonStats(pokemonname, maximumhp, currenthp):
    healthbar = 20 # Create a health bar with a length of 20 characters

    print('| ' + str(pokemonname)) # Print the name of the pokemon
    print('| HP: ' + str(currenthp) + ' / ' + str(maximumhp)) # Print the pokemon's current health

    print('| ', end='') # Print the beginning of the health bar
    bars = int(healthbar * (currenthp / maximumhp)) # Calculate how much of the health bar is filled, cast the integer value of it, then store it
    emptyspaces = healthbar - bars # Calculate the number of how much of the health bar is empty
    print('█' * bars, end='') # Print the calculated number of bars
    print(' ' * emptyspaces, end='') # Print the calculated number of emptyspaces
    print('|') # Print the end of the health bar

    print('|______________________') # Print the bottom of the stats box
    print('') # Print an empty line

def calculateBonusDamage(damagevalue, attackertype, defendanttype):
    criticalchance = random.random() # Generate a random number between 0 and 1

    if (attackertype == 'Grass') and (defendanttype == 'Fire'):
        damagevalue /= 2 # If the attacker's type is Grass, and the defendant's type is Fire, then cut the damage value of the attack in half

    elif (attackertype == 'Grass') and (defendanttype == 'Water'):
        damagevalue *= 2 # If the attacker's type is Grass, and the defendant's type is Water, then double the damage value of the attack

    elif (attackertype == 'Grass') and (defendanttype == 'Flying'):
        damagevalue /= 2 # If the attacker's type is Grass and the defendant's type is Flying, then cut the damage value of the attack in half

    elif (attackertype == 'Grass') and (defendanttype == 'Rock'):
        damagevalue *= 2 # If the attacker's type is Grass, and the defendant's typs is Rock, then double the damage value of the attack

    elif (attackertype == 'Grass') and (defendanttype == 'Poison'):
        damagevalue /= 2 # If the attacker's type is Grass, and the defendant's type is Poison, then cut the damage value of the attack in half

    elif (attackertype == 'Grass') and (defendanttype == 'Bug'):
        damagevalue /= 2 # If the attacker's type is Grass, then the defendant's type is Bug, then cut the damage value of the attack in half

    elif (attackertype == 'Grass') and (defendanttype == 'Grass'):
        damagevalue /= 2 # If the attacker and defendant's type is both Grass, then cut the damage value of the attack in half

    elif (attackertype == 'Fire') and (defendanttype == 'Grass'):
        damagevalue *= 2 # If the attacker's type is Fire and the defendant's type is Grass, then double the damage value of the attack

    elif (attackertype == 'Fire') and (defendanttype == 'Water'):
        damagevalue /= 2 # If the attacker's type is Fire, and the defendant's type is Water, then cut the damage value of the attack in half

    elif (attackertype == 'Fire') and (defendanttype == 'Rock'):
        damagevalue /= 2 # If the attacker's type is Fire, and the defendant's type is Rock, then cut the damage value of the attack in half

    elif (attackertype == 'Fire') and (defendanttype == 'Bug'):
        damagevalue *= 2# If the attacker's type is Fire, and the defendant's type is Bug, then double the damage value of the attack

    elif (attackertype == 'Fire') and (defendanttype == 'Fire'):
        damagevalue /= 2 # If the attacker and defendant's type is both Fire, then cut the damage value of the attack in half

    elif (attackertype == 'Water') and (defendanttype == 'Grass'):
        damagevalue /= 2 # If the attacker's type is Water, and the defendant's type is Grass, then cut the damage value of the attack in half

    elif (attackertype == 'Water') and (defendanttype == 'Fire'):
        damagevalue *= 2 # If the attacker's type is Water, and the defendant's type is Fire, then double the damage value of the attack

    elif (attackertype == 'Water') and (defendanttype == 'Rock'):
        damagevalue *= 2 # If the attacker's type is Water, and the defendant's type is Rock, then double the damage value of the attack

    elif (attackertype == 'Water') and (defendanttype == 'Water'):
        damagevalue /= 2 # If the attacker and the defendant's type is both Water, then cut the damage value of the attack in half

    elif (attackertype == 'Flying') and (defendanttype == 'Grass'):
        damagevalue *= 2 # If the attacker's type is Flying and the defendant's type is Grass, then double the damage value of the attack

    elif (attackertype == 'Flying') and (defendanttype == 'Rock'):
        damagevalue /= 2 # If the attacker's type is Flying, and the defendant's type is Rock, then cut the damage value of the attack in half

    elif (attackertype == 'Flying') and (defendanttype == 'Bug'):
        damagevalue *= 2 # If the attacker's type is Flying, and the defendant's type is Bug, then double the damage value of the attack

    elif (attackertype == 'Rock') and (defendanttype == 'Flying'):
        damagevalue *= 2 # If the attacker's type is Rock and the defendant's type is Flying, then double the damage value of the attack

    elif (attackertype == 'Rock') and (defendanttype == 'Fire'):
        damagevalue *= 2 # If the attacker's type is Rock and the defendant's type is Fire, then double the damage value of the attack

    elif (attackertype == 'Rock') and (defendanttype == 'Bug'):
        damagevalue *= 2 # If the attacker's type is Rock, and the defendant's type is Bug, then double the damage value of the attack

    elif (attackertype == 'Poison') and (defendanttype == 'Poison'):
        damagevalue /= 2 # If the attacker's type is Poison, and the defendant's type is Poison, then cut the damage value of the attack in half

    elif (attackertype == 'Poison') and (defendanttype == 'Rock'):
        damagevalue /= 2 # If the attacker's type is Poison, and the defendant's type is Rock, then cut the damage value of the attack in half

    elif (attackertype == 'Poison') and (defendanttype == 'Grass'):
        damagevalue *= 2 # If the attacker's type is Poison, and the defendant's type is Grass, then double the damage value of the attack

    elif (attackertype == 'Bug') and (defendanttype == 'Flying'):
        damagevalue /= 2 # If the attacker's type is Bug, and the defendant's type is Flying, then cut the damage value of the attack in half

    elif (attackertype == 'Bug') and (defendanttype == 'Poison'):
        damagevalue /= 2 # If the attacker's type is Bug, and the defendant's type is Poison, then cut the damage value of the attack in half

    elif (attackertype == 'Bug') and (defendanttype == 'Fire'):
        damagevalue /= 2 # If the attacker's type is Bug, and the defendant's type is Fire, then cut the damage value of the attack in half

    elif (attackertype == 'Bug') and (defendanttype == 'Grass'):
        damagevalue *= 2 # If the attacker's type is Bug, and the defendant's type is Grass, the double the damage value of the attack

    if criticalchance < 0.1:
        damagevalue += 0.5 * damagevalue # Increase the damage value of the current attack by 50% if the random number is below 0.1 (10% chance)

    damagevalue = int(damagevalue) # Cast the integer value of damage value, then store it

    return damagevalue # Return the amount of damage dealt

def chooseAttack(options, maximumpp, currentpp):
    options.append('Go Back')

    for index in range(0, len(options)):
        try:
            print(str(index + 1) + '. ' + options[index] + ' ' + str(currentpp[index]) + ' / ' + str(maximumpp[index]) + ' PP') # Print a list of attacks along with their PP values

        except IndexError:
            print(str(index + 1) + '. ' + options[index]) # If there are no more options with a PP value to display, then just display the option by itself

    flag = True
    while flag == True:
        attack = getUserDecision('Choose an attack', 'Choose which move you want to attack the enemy with. PP stands for Power Points, and represents how many times you can use it. Lower PP moves are usually stronger.', options)

        if options[attack] == 'Go Back':
            attack = 'Go Back' # If the user chooses to go back, store their decision
            flag = False # Exit the loop if they choose to go back

        elif currentpp[attack] == 0:
            print('You do not have enough PP for that move!') # If the PP value of the chosen attack is 0, then tell the user that they can't use it

        else:
            flag = False # Exit the loop if they choose a valid attack

    options.remove('Go Back')

    return attack # Return the index of the chosen attack (or return 'Go Back' if they chose to go back)

def chooseItem(options, maximumhp, currenthp, maximumpp, currentpp, trainerbattle):
    options.append('Go Back') # Add 'Go Back' as an option in the item menu
    printOptionList(options) # Print the list of options that the user can choose in the item menu

    flag = True
    while flag == True:
        item = getUserDecision('Choose an item', 'Choose an item to use. Elixirs restore PP, Potions restore HP, and Pokèballs allow you to capture a pokemon', options)

        if options[item] == 'Go Back':
            item = 'Go Back' # If the user chooses to go back, store their decision
            flag = False # Exit the loop if they choose to go back

        elif ((options[item] == 'Elixir') or (options[item] == 'Super Elixir')) and (currentpp == maximumpp):
            print('All attacks already have maximum PP!') # If the user tries to use a restoring item, but the attacks of the current pokemon already have max PP, then tell the user

        elif ((options[item] == 'Potion') or (options[item] == 'Super Potion')) and (currenthp == maximumhp):
            print('Your pokemon already has max HP!') # If the user tries to use a healing item, but their pokemon has max HP, then tell the user

        elif (options[item] == 'Pokèball') and (trainerbattle == True):
            print('You can not capture a pokemon owned by a trainer!') # If the user tries to capture a pokemon in a trainer battle, then tell the user that they can't use the Pokèball

        else:
            flag = False # Exit the loop if they choose a valid item

    options.remove('Go Back') # Remove 'Go Back' as an option when the user leaves the item menu

    return item # Return the index of the chosen item (or return 'Go Back' if they chose to go back)

def changePokemon(options, current):
    options.append('Go Back') # Add 'Go Back' as an option when the user enters the "Change Pokemon" menu
    printOptionList(options) # Print the list of options that the user can choose in the "Change Pokemon" menu

    flag = True
    while flag == True:
        new = getUserDecision('Which pokemon do you want to summon?', 'Summon another pokemon thats in your party. Choose one that is effective against your opponent.', options) # Get the user's input for the new pokemon they want to switch to

        if options[new] == 'Go Back':
            new = 'Go Back' # If the user chooses to go back, store their decision
            flag = False # Exit the loop if they choose to go back

        elif new == current:
            print(str(options[new]) + ' is already summoned!') # If the pokemon they chose is already summoned, then tell the user

        else:
            printTextBox('You summoned '+ str(options[new]) + '!') # Tell the user which pokemon they summmoned
            flag = False # Exit the loop once they choose a pokemon to summon

    options.remove('Go Back') # Remove 'Go Back' as an option once they leave the "Change Pokemon" Menu

    return new # Return the index of the user's new pokemon (or return 'Go Back' if they chose to go back)

def battleSequence(party1names, party1types, party1attacks, party1dmg, party1pp, party1maxpp, party1hp, party1maxhp, items, party2names, party2types, party2attacks, party2dmg, party2hp, party2maxhp, trainerbattle):
    currentpokemon = 0 # Set the index of the user's current pokemon
    enemypokemon = 0 # Set the index of the enemy's current pokemon

    printPokemonStats(party2names[enemypokemon], party2maxhp[enemypokemon], party2hp[enemypokemon]) # Display the stats of the enemy pokemon
    printPokemonStats(party1names[currentpokemon], party1maxhp[currentpokemon], party1hp[currentpokemon]) # Display the stats of the user's current pokemon

    itemsreserve = items.copy() # Store a copy of the user's inventory
    party1hpreserve = party1hp.copy() # Store a copy of the HP values for each pokemon in the user's party
    party1ppreserve = [] # Create a list that will hold a copy of the user's PP values going into the battle
    for index in range(0, len(party1pp)):
        party1ppreserve.append(party1pp[index].copy()) # Store a copy of the PP values for each pokemon in the user's party

    battleflag = True # Set the flag to true to start the battle sequence
    while battleflag == True:
        printOptionList(battledecisions) # Display the battle decisions that the user can make
        decision = getUserDecision('What will you do?', 'Choose what you want to do in battle.', battledecisions) # Get the battle decision that the user wants to make

        if battledecisions[decision] == 'Attack':
            attack = chooseAttack(party1attacks[currentpokemon], party1maxpp[currentpokemon], party1pp[currentpokemon]) # Get the user's input for the attack they want to use

            if attack != 'Go Back': # If the user didn't choose to attack, then continue with the attack sequence
                party1pp[currentpokemon][attack] = decrementValue(party1pp[currentpokemon][attack], 1) # Decrement the current attack's PP by 1
                damage = calculateBonusDamage(party1dmg[currentpokemon][attack], party1types[currentpokemon], party2types[enemypokemon]) # Calculate the amount of bonus damage that the attack will deal
                party2hp[enemypokemon] = decrementValue(party2hp[enemypokemon], damage) # Decrement the enemy's HP by the damage value of the user's attack

                printTextBox(str(party1names[currentpokemon]) + ' used ' + str(party1attacks[currentpokemon][attack]) + '! ' + str(party2names[enemypokemon]) + ' took ' + str(damage) + ' damage!') # Display the user's attack, and the damage it dealt

                if party2hp[enemypokemon] != 0:
                    attack = getBotDecision(party2attacks[enemypokemon]) # Get the enemy's input for the attack they want to use
                    damage = calculateBonusDamage(party2dmg[enemypokemon][attack], party2types[enemypokemon], party1types[currentpokemon]) # Calculate the amount of bonus damage that the attack will deal
                    party1hp[currentpokemon] = decrementValue(party1hp[currentpokemon], damage) # Decrement the current pokemon's HP by the damage value of the enemy's attack
                    printTextBox(str(party2names[enemypokemon]) + ' used ' + str(party2attacks[enemypokemon][attack]) + '! ' + str(party1names[currentpokemon]) + ' took ' + str(damage) + ' damage!') # Display the enemy's attack, and the damage it dealt

                else:
                    printTextBox(str(party2names[enemypokemon]) + ' fainted!') # If the enemy pokemon has 0 HP, then tell the user that the enemy pokemon fainted

                if party1hp[currentpokemon] == 0:
                    printTextBox(str(party1names[currentpokemon]) + ' fainted!') # If the user's pokemon has 0 HP, then tell the user that the enemy pokemon fainted)

                printPokemonStats(party2names[enemypokemon], party2maxhp[enemypokemon], party2hp[enemypokemon]) # Display the stats of the enemy pokemon
                printPokemonStats(party1names[currentpokemon], party1maxhp[currentpokemon], party1hp[currentpokemon]) # Display the stats of the user's current pokemon

        elif (battledecisions[decision] == 'Open Inventory') and (len(items) > 0):
            item = chooseItem(items, party1maxhp[currentpokemon], party1hp[currentpokemon], party1maxpp[currentpokemon], party1pp[currentpokemon], trainerbattle) # Get the user's input for the item they want to use

            if item != 'Go Back': # If the user didn't choose to attack, then use the item they chose
                item = items.pop(item) # Remove the item from the user's inventory, and store it

                if item == 'Elixir':
                    for index in range(0, len(party1pp[currentpokemon])):
                        party1pp[currentpokemon][index] = incrementValue(party1maxpp[currentpokemon][index], party1pp[currentpokemon][index], 10) # Increment the PP values of the current pokemon by 10

                    printTextBox('You used Elixir! All of ' + party1names[currentpokemon] + 's attacks gained 10 PP!') # Tell the user that their pokemon's attacks gained 10 PP

                elif item == 'Super Elixir':
                    party1pp[currentpokemon] = party1maxpp[currentpokemon].copy() # Set the current pokemon's PP values to their max values
                    printTextBox('You used Super Elixir! All of ' + party1names[currentpokemon] + 's attacks gained full PP!') # Tell the user that their pokemon's attacks gained full PP

                elif item == 'Potion':
                    party1hp[currentpokemon] = incrementValue(party1maxhp[currentpokemon], party1hp[currentpokemon], 20) # Increment the HP value of the current pokemon by 20
                    printTextBox('You used Potion! ' + party1names[currentpokemon] + ' gained 20 HP!') # Tell the user that their pokemon gained 20 HP

                elif item == 'Super Potion':
                    party1hp[currentpokemon] = party1maxhp[currentpokemon] # Set the current pokemon's HP to their max value
                    printTextBox('You used Super Potion! ' + party1names[currentpokemon] + ' gained full HP!') # Tell the user that their pokemon gained full HP

                elif item == 'Pokèball':
                    catchchance = random.random() # Generate a random number between 0 and 1, and store it

                    if catchchance > 0.5:
                        printTextBox('You caught ' + str(party2names[enemypokemon]) + '!') # Tell the user that their caught the pokemon
                        enemy = pokemonnames.index(party2names[enemypokemon]) # Find the index of the enemy's pokemon in the universal list
                        party1pp.append(pokemonpp[enemy].copy()) # Add the pokemon's PP values from the universal pokemon list into the user's party
                        party1maxpp.append(pokemonpp[enemy].copy()) # Add the pokemon's max PP values from the universal pokemon list into the user's party

                        party1names.append(party2names.pop(enemypokemon)) # Add the pokemon's name to the user's party
                        party1types.append(party2types.pop(enemypokemon)) # Add the pokemon's type to the user's party
                        party1attacks.append(party2attacks.pop(enemypokemon)) # Add the pokemon's attacks to the user's party
                        party1dmg.append(party2dmg.pop(enemypokemon)) # Add the pokemon's damage values to the user's party
                        party1hp.append(party2hp.pop(enemypokemon)) # Add the pokemon's HP values to the user's party
                        party1maxhp.append(party2maxhp.pop(enemypokemon)) # Add the pokemon's max HP values to the user's party
                    else:
                        printTextBox(str(party2names[enemypokemon]) + ' escaped the Pokèball!')

        elif (battledecisions[decision] == 'Open Inventory') and (len(items) == 0):
            print('There is nothing in your inventory!') # If the user tries to access an empty inventory, then tell the user that there is nothing in their inventory

        elif battledecisions[decision] == 'Change Pokemon':
            newpokemon = changePokemon(party1names, currentpokemon) # Get the user's input for the new pokemon they want to switch to

            if newpokemon != 'Go Back': # If the user didn't choose to go back, then change their current pokemon
                currentpokemon = newpokemon # Set the chosen pokemon as the user's current pokemon
                printPokemonStats(party2names[enemypokemon], party2maxhp[enemypokemon], party2hp[enemypokemon]) # Display the stats of the enemy pokemon
                printPokemonStats(party1names[currentpokemon], party1maxhp[currentpokemon], party1hp[currentpokemon]) # Display the stats of the user's current pokemon

        elif (battledecisions[decision] == 'Flee') and (trainerbattle == False):
            battleflag = False # Exit the loop to end the battle

        elif (battledecisions[decision] == 'Flee') and (trainerbattle == True):
            print('You can not run away from a trainer!') # If the user tries to flee a trainer battle, tell the user that they can't

        if party1hp.count(0) == len(party1hp):
            printTextBox('All of your pokemon fainted! You blacked out!') # If all of the pokemon in the user's party have 0 HP, tell the user that all their pokemon fainted
            input('Press enter to continue:') # Pause until the user presses enter
            
            printTextBox('Restarting battle from the beginning...') # Tell the user that the battle will restart
            input('Press enter to continue:') # Pause until the user presses enter

            currentpokemon = 0 # Reset the index of the user's current pokemon
            enemypokemon = 0 # Reset the index of the enemy's current pokemon

            items = itemsreserve.copy() # Reset the user's inventory to what it was at the beginning of the battle
            party1hp = party1hpreserve.copy() # Reset the user's HP values to what they were at the beginning of the battle
            for index in range(0, len(party1pp)):
                party1pp[index] = party1ppreserve[index].copy() # Reset the user's PP values to what they were at the beginning of the battle

            party2hp = party2maxhp.copy() # Reset the HP values of the enemy's party to their max values

            printPokemonStats(party2names[enemypokemon], party2maxhp[enemypokemon], party2hp[enemypokemon]) # Display the stats of the enemy pokemon
            printPokemonStats(party1names[currentpokemon], party1maxhp[currentpokemon], party1hp[currentpokemon]) # Display the stats of the user's current pokemon

        elif (party1hp[currentpokemon] == 0) and (battledecisions.count('Attack') == 1):
            battledecisions.remove('Attack') # If the user's current pokemon has 0 HP, and they have the option to attack, then remove the option to attack

        elif (party1hp[currentpokemon] > 0) and (battledecisions.count('Attack') == 0):
            battledecisions.insert(0, 'Attack') # If the user's current pokemon has more than 0 HP, and they don't have the option to attack, then add the option to attack

        if party2hp.count(0) == len(party2hp):
            printTextBox('You won the battle!') # If all of the enemy's pokemon has 0 HP, then tell the user they won the battle
            battleflag = False # Set the battle flag to False to end the battle sequence

        elif party2hp[enemypokemon] == 0:
            enemypokemon += 1 # Summon a new enemy by changing the index of the enemy pokemon
            printTextBox('The enemy summons ' + str(party2names[enemypokemon]) + '!') # Tell the user the enemy's new pokemon
            printPokemonStats(party2names[enemypokemon], party2maxhp[enemypokemon], party2hp[enemypokemon]) # Display the stats of the enemy's pokemon
            printPokemonStats(party1names[currentpokemon], party1maxhp[currentpokemon], party1hp[currentpokemon]) # Display the stats of the user's pokemon

    return [party1names, party1types, party1attacks, party1dmg, party1pp, party1maxpp, party1hp, party1maxhp, items] # Return the user's whole party, and their stats after the battle

printTextBox('Hello there! Welcome to the world of pokémon! My name is Oak! People call me the pokémon Prof!') # Print Oak's speech
input('Press Enter to continue:')    # Take input to continue

printTextBox('This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights. Myself... I study pokémon as a profession.') # Print Oak's speech
input('Press Enter to continue:')    # Take input to continue

printTextBox('You may type the letter H (not case sensitive) at any choice throughout your journey for help.') # Print Oak's speech
input('Press Enter to continue:')    # Take input to continue

flag = True # Set flag to true
while flag == True:     # Loop until the user chooses name and gender and confirms
    name = setName()    # Call the setName function to choose a name
    gender = setGender()    # Call the setGender function to choose a gender

    printTextBox('Are you sure your name is ' + name + ', and you are a ' + gender + '?')   # Print a text box to ask the user to confirm

    verify = getUserDecision('Press 1 for yes, press 2 for no.', 'Press 1 if you are OK with your decision, 2 if you are not OK with your decision', verification)  # Ask the user to confirm
    if verification[verify] == 'Yes':   # Check if user chose yes
        printTextBox('Welcome ' + name + ' to the wonderful world of pokémon! There are three rare pokémon here. The pokémon are held in these pokéballs! When I was young like you, I was a serious pokémon trainer. But now, in my old age, I have only these three pokémon left. You, ' + name + ', can choose one. Go on, choose!')     # Print oak's speech
        input('Press Enter to continue:')    # Take input to continue
        flag = False   # Exit the loop

    else:   # Check if user chose no
        print('Ok, lets try again.')    # Tell the user to try again

flag = True # Set flag to true
while flag == True:     # Loop until the user chooses a starter
    starter_choice = starterPick()  # Call the starterPick function to have the user choose a starter
    printTextBox('Are you sure you want to choose ' + starter_choice + '?')  # Ask to confirm with user starter choice

    verify = getUserDecision('Press 1 for yes, press 2 for no,', 'Press 1 if you are OK with your decision, 2 if you are not OK with your decision', verification)  # Confirm user choice
    if verification[verify] == 'Yes':   # Check if user confirmed
        printTextBox('Congratulations! You chose ' + starter_choice + '!')    # Tell user their choice
        flag = False   # End loop

    else:   # Check if user chose no
        print('Ok, lets try again.')    # Tell user we will restart choice

starter_choice = pokemonnames.index(starter_choice) # Find the index of the chosen pokemon
userpartynames.append(pokemonnames[starter_choice]) # Add the name of the starter pokemon to the user's party
userpartytypes.append(pokemontypes[starter_choice]) # Add the type of the starter pokemon to the user's party
userpartyattacks.append(pokemonattacks[starter_choice].copy()) # Add the attacks of the starter pokemon to the user's party
userpartydmg.append(pokemondmg[starter_choice].copy()) # Add the damage values of the starter pokemon's attacks to the user's party
userpartypp.append(pokemonpp[starter_choice].copy()) # Add the PP values of the starter pokemon's attacks to the user's party
userpartymaxpp.append(pokemonpp[starter_choice].copy()) # Add the max PP values of the starter pokemon's attacks to the user's party
userpartyhp.append(pokemonhp[starter_choice]) # Add the HP values of the starter pokemon to the user's party
userpartymaxhp.append(pokemonhp[starter_choice]) # Add the max HP values of the starter pokemon to the user's party

printTextBox('Now that you have chosen your first pokémon, it is time for you to head out. Be careful young one, and enjoy the world of pokémon!')  # Print oak's speech
input('Press Enter to continue:')    # Take input to continue

printTextBox('By the way, have you met Blue? He came to choose a pokémon this morning before you came around, and I believe you two will make great rivals.')   # Print oak's speech
input('Press Enter to continue:')    # Take input to continue

printTextBox('Whats up ' + name + ', I am your rival, Blue, and I want to fight you in a pokémon battle!')     # Print Blue's introduction line
input('Press Enter to continue:')    # Take input to continue

if userpartynames.count('Charmander') == 1:
    enemy = pokemonnames.index('Bulbasaur') # Find the index of 'Bulbasaur' in the universal pokemon list, and store it

elif userpartynames.count('Bulbasaur') == 1:
    enemy = pokemonnames.index('Squirtle') # Find the index of 'Squirtle' in the universal pokemon list, and store it

else:
    enemy = pokemonnames.index('Charmander') # Find the index of 'Charmander' in the universal pokemon list, and store it

enemypartynames = [pokemonnames[enemy]] # Set the name of the indexed pokemon to the enemy's party
enemypartytypes = [pokemontypes[enemy]] # Set the type of the indexed pokemon to the enemy's party
enemypartyattacks = [pokemonattacks[enemy].copy()] # Set the attacks of the indexed pokemon to the enemy's party
enemypartydmg = [pokemondmg[enemy].copy()] # Set the damage values of the indexed pokemon to the enemy's party
enemypartyhp = [pokemonhp[enemy]] # Set the HP values of the indexed pokemon to the enemy's party
enemypartymaxhp = [pokemonhp[enemy]] # Set the max hp values of the indexed pokemon to the enemy's party

battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, True)

printTextBox('Congratulations on defeating Blue! You have won ¥200!')   # Congratulate user on defeating blue
input('Press Enter to continue:')    # Take input to continue

money += 200    # Add money to the users balance
printTextBox('Wow, congrats on the win, ' + name + '! This wont be the last you see of me, however...')     # Print Blue's losing statement
input('Press Enter to continue:')    # Take input to continue

printTextBox('After defeating Blue, you decide to take a stroll onto the first route to try and make it to the next city. On the walk, you discover some tall grass. Would you like to walk through it to discover a pokémon?')     # Ask user about tall grass

tallGrassChoice = ['Go in the grass', 'Continue walking']   # Make a list for the choice to go into the tall grass or not
printOptionList(tallGrassChoice)    # Print the choices that the user can choose
tall_grass = getUserDecision('', 'Go in the grass to encounter a pokemon, or Continue walking on the current route', tallGrassChoice)    # Take user input on their choice

if tallGrassChoice[tall_grass] == 'Go in the grass':     # Check if user chose to go into the grass
    encounter_chance = random.random() # Generate a random number between 0 and 1

    if encounter_chance > 0.5:
        enemy = pokemonnames.index('Pidgey') # Find the index of 'Pidgey' in the universal pokemon list
        printTextBox('You encountered a Pidgey!') # Tell the user what pokemon they encountered

    else:
        enemy = pokemonnames.index('Rattata') # Find the index of 'Rattata' in the universal pokemon list
        printTextBox('You encountered a Rattata!') # Tell the user what pokemon they encountered

    enemypartynames = [pokemonnames[enemy]] # Set the name of the indexed pokemon to the enemy's party
    enemypartytypes = [pokemontypes[enemy]] # Set the type of the indexed pokemon to the enemy's party
    enemypartyattacks = [pokemonattacks[enemy].copy()] # Set the attacks of the indexed pokemon to the enemy's party
    enemypartydmg = [pokemondmg[enemy].copy()] # Set the damage values of the indexed pokemon to the enemy's party
    enemypartyhp = [pokemonhp[enemy]] # Set the HP values of the indexed pokemon to the enemy's party
    enemypartymaxhp = [pokemonhp[enemy]] # Set the max HP values of the indexed pokemon to the enemy's party

    battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, False)

printTextBox('You continue on your path towards the next city. On your journey, you see a pokémon trainer.')    # Print text box
input('Press Enter to continue:')    # Take input to continue

printTextBox('You have been challenged to a battle by Ace Trainer Ganti!')  # Tell user of challenge
input('Press Enter to continue:')    # Take input to continue

enemy = pokemonnames.index('Rattata') # Find the index of 'Rattata' in the universal pokemon list
enemypartynames = [pokemonnames[enemy]] # Set the name of the indexed pokemon to the enemy's party
enemypartytypes = [pokemontypes[enemy]] # Set the type of the indexed pokemon to the enemy's party
enemypartyattacks = [pokemonattacks[enemy].copy()] # Set the attacks of the indexed pokemon to the enemy's party
enemypartydmg = [pokemondmg[enemy].copy()] # Set the damage values of the indexed pokemon to the enemy's party
enemypartyhp = [pokemonhp[enemy]] # Set the HP values of the indexed pokemon to the enemy's party
enemypartymaxhp = [pokemonhp[enemy]] # Set the max HP values of the indexed pokemon to the enemy's party
printTextBox('The enemy summons a Rattata!') # Print what pokemon the enemy summoned

battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, True)

money += 200     # Add money to user's balance
printTextBox('¥200 has been added to your inventory.')  # Tell user they won money

printTextBox('After defeating Ganti, you continue on the route. Again, you see a pokémon trainer. This time a lass.')   # Print text box
input('Press Enter to continue:')    # Take input to continue

printTextBox('You have been challenged by Pokèmon Lass Ariel!')     # Tell user of challenge
input('Press Enter to continue:')    # Take input to continue

enemy = pokemonnames.index('Pidgey') # Find the index of 'Pidgey' in the universal pokemon list
enemypartynames = [pokemonnames[enemy]] # Set the name of the indexed pokemon to the enemy's party
enemypartytypes = [pokemontypes[enemy]] # Set the type of the indexed pokemon to the enemy's party
enemypartyattacks = [pokemonattacks[enemy].copy()] # Set the attacks of the indexed pokemon to the enemy's party
enemypartydmg = [pokemondmg[enemy].copy()] # Set the damage values of the indexed pokemon to the enemy's party
enemypartyhp = [pokemonhp[enemy]] # Set the HP values of the indexed pokemon to the enemy's party
enemypartymaxhp = [pokemonhp[enemy]] # Set the max HP values of the indexed pokemon to the enemy's party
printTextBox('The enemy summons a Pidgey!') # Print what pokemon the enemy summoned

battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, True)

printTextBox('After winning the pokèmon battle, you continue onwards and arrive at Viridian City.')     # Tell user of arrival
input('Press Enter to continue:')    # Take input to continue

viridian_options = ['Pokèmon Center', 'Pokèmart', 'Pokèmon Gym']    # Create list of places at Viridian
flag = True     # Make the flag true
while flag == True:     # Loop until the user defeats the pokemon gym
    print('Where would you like to go?')    # Ask user where they want to go
    print('')   # Print empty string

    printOptionList(viridian_options)   # Print options list/Where to go
    viridian_choice = getUserDecision('', 'The Pokemon Center allows you to restore your Pokemons stats, The Pokemart is a place for you to buy items, the Pokemon Gym has trainers that you can battle.', viridian_options)   # Take user's input

    if viridian_options[viridian_choice] == 'Pokèmon Center':    # Check if the user chose to go to the pokecenter
        printTextBox('You have chosen to go the the Pokèmon Center.')   # Tell the user their choice
        input('Press enter to continue: ')   # Pause until user continues

        userpartyhp = userpartymaxhp.copy() # Set the HP values of the pokemon in the user's party to their max values
        for i in range(0, len(userpartypp)):
            userpartypp[i] = userpartymaxpp[i].copy() # Set the PP values of the pokemon in the user's party to their max values

        printTextBox('HP and PP has been restored for all of your pokemon!')

    elif viridian_options[viridian_choice] == 'Pokèmart':  # Check if user chose to go to the pokemart
        printTextBox('You have chosen to go to the Pokèmart.')  # tell user their choice
        input('Press enter to continue: ')   # Pause until user continues

        shopping_results = buyItem(shop, money) # Start the shopping sequence
        money = shopping_results[0] # Extract index 0 of the shopping results, and store it as the user's new money count
        inventory.extend(shopping_results[1:]) # Extract the rest of the shopping results, and add it to the user's inventory

    elif viridian_options[viridian_choice] == 'Pokèmon Gym':  # Check if user chose to go to the Pokèmon Gym
        printTextBox('You have chosen to go to the Pokèmon Gym.')   # Tell user their choice
        input('Press enter to continue: ')   # Pause until user continues

        printTextBox('Hi, Im Brock! Im the gym leader in this city, and I specialize with Rock types!')   # Print Brock's speech
        input('Press enter to continue: ')   # Pause until user continues

        printTextBox('If you have come to battle me, then good luck!')  # Print Brock's speech
        input('Press enter to continue: ')   # Pause until user continues

        printTextBox('You have been challenged to a battle by Viridian City Gym Leader Brock!')     # Print challenge

        enemy = pokemonnames.index('Geodude') # Find the index of 'Geodude' in the universal pokemon list
        enemypartynames = [pokemonnames[enemy]] # Set the name of the indexed pokemon to the enemy's party
        enemypartytypes = [pokemontypes[enemy]] # Set the type of the indexed pokemon to the enemy's party
        enemypartyattacks = [pokemonattacks[enemy].copy()] # Set the attacks of the indexed pokemon to the enemy's party
        enemypartydmg = [pokemondmg[enemy].copy()] # Set the damage values of the indexed pokemon to the enemy's party
        enemypartyhp = [pokemonhp[enemy]] # Set the HP values of the indexed pokemon to the enemy's party
        enemypartymaxhp = [pokemonhp[enemy]] # Set the max HP values of the indexed pokemon to the enemy's party

        enemy = pokemonnames.index('Onix') # Find the index of 'Onix' in the universal pokemon list
        enemypartynames.append(pokemonnames[enemy]) # Add the name of the indexed pokemon to the enemy's party
        enemypartytypes.append(pokemontypes[enemy]) # Add the type of the indexed pokemon to the enemy's party
        enemypartyattacks.append(pokemonattacks[enemy].copy()) # Add the attacks of the indexed pokemon to the enemy's party
        enemypartydmg.append(pokemondmg[enemy].copy()) # Add the damage values of the indexed pokemon to the enemy's party
        enemypartyhp.append(pokemonhp[enemy]) # Add the HP values of the indexed pokemon to the enemy's party
        enemypartymaxhp.append(pokemonhp[enemy]) # Add the max HP values of the indexed pokemon to the enemy's party

        printTextBox('The enemy summons a Geodude!') # Print what pokemon the enemy summoned
        battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, True)

        printTextBox('Congratulations, ' + name + '! You have defeated Brock, the rock-type gym leader!')   # Print text
        input('Press Enter to continue:')    # Take input to continue

        money += 750    # Add money to users balance
        printTextBox('You have earned ¥750 from winning!')  # Tell user they gained money
        input('Press Enter to continue:')    # Take input to continue

        printTextBox('You have won the Boulder Badge! Congratulations!')     # Inform user of their new badge
        input('Press Enter to continue:')    # Take input to continue

        shop = ['Pokèball', 'Potion', 'Elixir', 'Super Potion', 'Super Elixir' ]   # List of items that the user can buy in the PokeMart by default
        printTextBox('New items have been added to the shop!')  # Tell user of shop updates
        input('Press Enter to continue:')    # Take input to continue

        viridian_options[2] = 'Route 2'     # Set the third option to the next route rather than the gym

        printTextBox('You should heal before heading onto the next route.')     # Print Brock's advice
        input('Press Enter to continue:')    # Take input to continue

    elif viridian_options[viridian_choice] == 'Route 2':    # Check if user chose to move onto the next route
        printTextBox('So you decide to head onto the next route, route 2.')     # Print user's decision
        input('Press Enter to continue:')    # Take input to continue
        flag = False   # Set the flag to false to exit the loop

    else:   # Check for errors
        print('Error: Line 255: Unhandled exception')   # Print error code

printTextBox('On route 2, you walk on the path.')  # Print users discoveries
input('Press Enter to continue:')    # Take input to continue

printTextBox('You spot a pokèmon trainer!')     # Print users discoveries
input('Press Enter to continue:')    # Take input to continue

printTextBox('Pokèmon Trainer Paul has challenged you to a battle!')    # Tell user of challenge
input('Press Enter to continue:')    # Take input to continue

enemy = pokemonnames.index('Nidoran♂') # Find the index of 'Nidoran♂' in the universal pokemon list
enemypartynames = [pokemonnames[enemy]] # Set the name of the indexed pokemon to the enemy's party
enemypartytypes = [pokemontypes[enemy]] # Set the type of the indexed pokemon to the enemy's party
enemypartyattacks = [pokemonattacks[enemy].copy()] # Set the attacks of the indexed pokemon to the enemy's party
enemypartydmg = [pokemondmg[enemy].copy()] # Set the damage values of the indexed pokemon to the enemy's party
enemypartyhp = [pokemonhp[enemy]] # Set the HP values of the indexed pokemon to the enemy's party
enemypartymaxhp = [pokemonhp[enemy]] # Set the max HP values of the indexed pokemon to the enemy's party
printTextBox('The enemy summons a Nidoran♂!')# Print what pokemon the enemy summoned

battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, True)

money += 200    # Add money to user's balance
printTextBox('¥200 has been added to your inventory.')  # Tell user they won money
input('Press Enter to continue:')    # Take input to continue

printTextBox('After defeating Paul, you continue on the route. You discover some tall grass. Would you like to walk in it and discover a Pokèmon?')     # Tell user about grass
input('Press enter to continue: ')   # Pause until user continues

printOptionList(tallGrassChoice)    # Print the choices that the user can choose
tall_grass = getUserDecision('', 'Go in the grass to encounter a pokemon, or Continue walking on the current route', tallGrassChoice)    # Take user input on their choice

if tallGrassChoice[tall_grass] == 'Go in the grass':     # Check if user chose to go into the grass
    encounter_chance = random.random() # Generate a random number between 0 and 1

    if encounter_chance > 0.5:
        enemy = pokemonnames.index('Nidoran♂') # Find the index of 'Nidoran♂' in the universal pokemon list
        printTextBox('You encountered a Nidoran♂') # Print what pokemon the user encounters

    else:
        enemy = pokemonnames.index('Nidoran♀') # Find the index of 'Nidoran♀' in the universal pokemon list
        printTextBox('You encountered a Nidoran♀!') # Print what pokemon the user encounters

    enemypartynames = [pokemonnames[enemy]] # Set the name of the indexed pokemon to the enemy's party
    enemypartytypes = [pokemontypes[enemy]] # Set the type of the indexed pokemon to the enemy's party
    enemypartyattacks = [pokemonattacks[enemy].copy()] # Set the attacks of the indexed pokemon to the enemy's party
    enemypartydmg = [pokemondmg[enemy].copy()] # Set the damage values of the indexed pokemon to the enemy's party
    enemypartyhp = [pokemonhp[enemy]] # Set the HP values of the indexed pokemon to the enemy's party
    enemypartymaxhp = [pokemonhp[enemy]] # Set the max HP values of the indexed pokemon to the enemy's party

    battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, False)

printTextBox('You continue walking. As you are walking, you spot another pokèmon trainer! You confront her and she challenges you to a pokèmon battle!')    # Print challenge
input('Press enter to continue: ')   # Pause until user continues

printTextBox('You have been challenged to a battle by Bug Catcher Amanda!')     # Print challenge
input('Press enter to continue: ')   # Pause until user continues

enemy = pokemonnames.index('Caterpie') # Find the index of 'Caterpie' in the universal pokemon list
enemypartynames = [pokemonnames[enemy]] # Set the name of the indexed pokemon to the enemy's party
enemypartytypes = [pokemontypes[enemy]] # Set the type of the indexed pokemon to the enemy's party
enemypartyattacks = [pokemonattacks[enemy].copy()] # Set the attacks of the indexed pokemon to the enemy's party
enemypartydmg = [pokemondmg[enemy].copy()] # Set the damage values of the indexed pokemon to the enemy's party
enemypartyhp = [pokemonhp[enemy]] # Set the HP values of the indexed pokemon to the enemy's party
enemypartymaxhp = [pokemonhp[enemy]] # Set the max HP values of the indexed pokemon to the enemy's party
printTextBox('The enemy summons a Caterpie!') # Print what pokemon the enemy summoned

battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, True)

printTextBox('After defeating Amanda, you continue walking down the route, and find yourself at Pewter City.')  # Print arrival
input('Press enter to continue: ')   # Pause until user continues

pewter_options = ['Pokèmon Center', 'Pokèmart', 'Pokèmon Gym']    # Create list of places at Pewter
flag = True     # Set the loop to run
while flag == True:     # Loop until user leaves Pewter
    print('Where would you like to go?')    # Ask player where he would like to go
    print('')   # Print empty string

    printOptionList(pewter_options)   # Print options list/Where to go
    pewter_choice = getUserDecision('', 'The Pokemon Center allows you to restore your Pokemons stats, The Pokemart is a place for you to buy items, the Pokemon Gym has trainers that you can battle.', viridian_options)   # Take user's input

    if pewter_options[pewter_choice] == 'Pokèmon Center':  # Check if user chose to go to pokecenter
        printTextBox('You have chosen to go the the Pokèmon Center.')   # Tell the user their choice
        input('Press enter to continue: ')   # Pause until user continues

        userpartyhp = userpartymaxhp.copy() # Set the HP values of the pokemon in the user's party to their max values
        for i in range(0, len(userpartypp)):
            userpartypp[i] = userpartymaxpp[i].copy() # Set the PP values of the pokemon in the user's party to their max values

        printTextBox('HP and PP has been restored for all of your pokemon!')

    elif pewter_options[pewter_choice] == 'Pokèmart':    # Check if user chose to go to the pokemart
        printTextBox('You have chosen to go to the Pokèmart.')  # tell user their choice
        input('Press enter to continue: ')   # Pause until user continues

        shopping_results = buyItem(shop, money) # Start the shopping sequence
        money = shopping_results[0] # Extract index 0 of the shopping results, and store it as the user's new money count
        inventory.extend(shopping_results[1:]) # Extract the rest of the shopping results, and add it to the user's inventory

    elif pewter_options[pewter_choice] == 'Pokèmon Gym':  # Check if user chose to go to the Pokèmon Gym
        printTextBox('You have chosen to go to the Pokèmon Gym.')   # Tell user their choice
        input('Press enter to continue: ')   # Pause until user continues

        printTextBox('Hey there, im Misty. I specialize with water types, and im your battle today!')   # Print Misty's speech
        input('Press enter to continue: ')   # Pause until user continues

        printTextBox('You have been challenged to a battle by Pewter City Gym Leader Misty!')   # Print challenge

        enemy = pokemonnames.index('Staryu') # Find the index of 'Staryu' in the universal pokemon list
        enemypartynames = [pokemonnames[enemy]] # Set the name of the indexed pokemon to the enemy's party
        enemypartytypes = [pokemontypes[enemy]] # Set the type of the indexed pokemon to the enemy's party
        enemypartyattacks = [pokemonattacks[enemy].copy()] # Set the attacks of the indexed pokemon to the enemy's party
        enemypartydmg = [pokemondmg[enemy].copy()] # Set the damage values of the indexed pokemon to the enemy's party
        enemypartyhp = [pokemonhp[enemy]] # Set the HP values of the indexed pokemon to the enemy's party
        enemypartymaxhp = [pokemonhp[enemy]] # Set the max HP values of the indexed pokemon to the enemy's party

        enemy = pokemonnames.index('Starmie') # Find the index of 'Starmie' in the universal pokemon list
        enemypartynames.append(pokemonnames[enemy]) # Add the name of the indexed pokemon to the enemy's party
        enemypartytypes.append(pokemontypes[enemy]) # Add the type of the indexed pokemon to the enemy's party
        enemypartyattacks.append(pokemonattacks[enemy].copy()) # Add the attacks of the indexed pokemon to the enemy's party
        enemypartydmg.append(pokemondmg[enemy].copy()) # Add the damage values of the indexed pokemon to the enemy's party
        enemypartyhp.append(pokemonhp[enemy]) # Add the HP values of the indexed pokemon to the enemy's party
        enemypartymaxhp.append(pokemonhp[enemy]) # Add the max HP values of the indexed pokemon to the enemy's party

        printTextBox('The enemy summons a Staryu!') # Print what pokemon the enemy summoned
        battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, True)

        printTextBox('Congratulations, ' + name + '! You have defeated Misty, the water-type gym leader!')   # Print text
        input('Press Enter to continue:')    # Take input to continue

        money += 900    # Add money to users balance
        printTextBox('You have earned ¥900 from winning!')  # Tell user they gained money
        input('Press Enter to continue:')    # Take input to continue

        printTextBox('You have won the Cascade Badge! Congratulations!')     # Inform user of their new badge
        input('Press Enter to continue:')    # Take input to continue

        pewter_options[2] = 'Route 3'     # Set the third option to the next route rather than the gym
        printTextBox('You should heal before heading onto the next route.')     # Print Misty's advice
        input('Press Enter to continue:')    # Take input to continue

    elif pewter_options[pewter_choice] == 'Route 3':    # Check if user chose to move onto the next route
        printTextBox('So you decide to head onto the next route, route 3.')     # Print user's decision
        input('Press Enter to continue:')    # Take input to continue
        flag = False   # Set the flag to false to exit the loop

    else:   # Check for errors
        print('Error: Line 255: Unhandled exception')   # Print error code

printTextBox('On the route, you come across your rival, Blue.')     # Print Blue's arrival
input('Press Enter to continue:')    # Take input to continue

printTextBox('Hello, ' + name + '! I heard youve beat your first two gym leaders already, and I wanted to congratulate you. Im around the same part, and wanted to challenge you to a battle.')     # Print Blue's speech and challenge
input('Press Enter to continue:')    # Take input to continue

printTextBox('You have been challenged to a battle by Pokèmon Rival Blue!')     # Print challenge
input('Press Enter to continue:')    # Take input to continue

if userpartynames.count('Bulbasaur') == 1:     # Check user's starter to determine Blue's starter
    enemy = pokemonnames.index('Squirtle') # Find the index of 'Squirtle' universal pokemon list
    printTextBox('The enemy summons a Squirtle!') # Print what pokemon the enemy summoned

elif userpartynames.count('Charmander') == 1:  # Check user's starter to determine Blue's starter
    enemy = pokemonnames.index('Bulbasaur') # Find the index of 'Bulbasaur' universal pokemon list
    printTextBox('The enemy summons a Bulbasaur!') # Print what pokemon the enemy summoned

elif userpartynames.count('Squirtle') == 1:     # Check the user's starter to determine Blue's starter
    enemy = pokemonnames.index('Charmander') # Find the index of 'Charmander' universal pokemon list
    printTextBox('The enemy summons a Charmander!') # Print what pokemon the enemy summoned

else:   # Check for errors
    print('Exception not handled - contact programmer')     # Print error

enemypartynames = [pokemonnames[enemy]] # Set the name of the indexed pokemon to the enemy's party
enemypartytypes = [pokemontypes[enemy]] # Set the type of the indexed pokemon to the enemy's party
enemypartyattacks = [pokemonattacks[enemy].copy()] # Set the attacks of the indexed pokemon to the enemy's party
enemypartydmg = [pokemondmg[enemy].copy()] # Set the damage values of the indexed pokemon to the enemy's party
enemypartyhp = [pokemonhp[enemy]] # Set the HP values of the indexed pokemon to the enemy's party
enemypartymaxhp = [pokemonhp[enemy]] # Set the max HP values of the indexed pokemon to the enemy's party

enemy = pokemonnames.index('Rhyhorn') # Find the index of 'Rhyhorn' in the universal pokemon list
enemypartynames.append(pokemonnames[enemy]) # Add the name of the indexed pokemon to the enemy's party
enemypartytypes.append(pokemontypes[enemy]) # Add the type of the indexed pokemon to the enemy's party
enemypartyattacks.append(pokemonattacks[enemy].copy()) # Add the attacks of the indexed pokemon to the enemy's party
enemypartydmg.append(pokemondmg[enemy].copy()) # Add the damage values of the indexed pokemon to the enemy's party
enemypartyhp.append(pokemonhp[enemy]) # Add the HP values of the indexed pokemon to the enemy's party
enemypartymaxhp.append(pokemonhp[enemy]) # Add the max HP values of the indexed pokemon to the enemy's party

battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, True)

printTextBox('Congratulations on defeating Pokèmon Trainer Blue!')  # Print Blue's text
input('Press Enter to continue:')    # Take input to continue

printTextBox('Well, ' + name + ', it seems you have defeated me. Congratulations, you are the greater trainer!')    # Print Blue's text
input('Press Enter to continue:')    # Take input to continue

printTextBox('That brings you to the end of your adventure! To continue, please purchase non-existant DLC with non-existant currency!')    # Print ending message
