# Authors: Kevin Quijalvo and Erik Kozy
# Date: November 29 2017
# File Name: pokemon.py
# Description: Very small pokemon RPG

import random # Import the random library

money = 500   # Set the players money
shop = ['Pokeball', 'Potion', 'Elixir']   # Set the pokemart items
inventory = ['Pokeball', 'Pokeball', 'Pokeball', 'Pokeball', 'Pokeball']  # Set user's inventory

name = ['Pokemon1', 'Pokemon2'] # Create a list of pokemon that the user has
attacks = [['fire1', 'fire2', 'fire3', 'fire4'], ['water1', 'water2', 'water3', 'water4']] # Create a list of attacks for each pokemon that the user has
movedmg = [[2, 4, 6, 8], [2, 4, 6, 8]] # Create a list of the damage values for each move of every pokemon that the user has
movepp = [[0, 4, 10, 15], [0, 5, 10, 15]] # Create a list of PP values for each move of every pokemon that the user has
maxpp = [[0, 5, 10, 15], [0, 5, 10, 15]] # Create a list of the max PP values for each move of every pokemon that the user has
hp = [50, 100] # Create a list of the current hp values for each pokemon that the user has
maxhp = [50, 100] # Create a list of the max hp values for each pokemon that the user has

battledecisions = ['Attack', 'Open Inventory', 'Change Pokemon', 'Flee'] # Create a list of decisions that the user can make during battle

currentpokemon = 0 # Index of the user's current pokemon

enemyname = 'bob'
enemyattacks = ['test1', 'test2', 'test3', 'test4']
enemymovedmg = [4, 3, 2, 5]
enemyhp = 100
enemymaxhp = 100

def professorGender():   # Define professorGender as a function
    genders = ['Boy', 'Girl'] # Create a list of available genders that the user can choose
    printTextBox('Hello there! Welcome to the world of pokémon! My name is Oak! People call me the pokémon Prof!')
    printTextBox('This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights. Myself... I study pokémon as a profession.')
    printTextBox('Are you a boy or a girl?')
    printOptionList(genders) # Print the list of gender that the user can choose
    choice = getUserDecision(genders) # Ask for the index of the user's decision, then store it
    return genders[choice]   # Return the user's gender to the main code

def professorName():    # Define professorName as a function
    alias = '0'    # Set the user's name blank
    printTextBox('What is your name?')
    alias = input(': ')     # Print Oak's speech
    return alias    # Return the user's name to the main code

def areYouSure(sex, alias):     # Define areYouSure as a function
    if sex == '1':   # Check if user chose boy
        sure = input('So youre a boy and your name is ' + alias + '? Press 1 for yes, press 2 for no')   # Confirm user's choices
    elif sex == '2':     # Check if user chose girl
        sure = input('So youre a girl and your name is ' + alias + '? Press 1 for yes, press 2 for no')  # Confirm user's choices
    else:   # Check for error statements
        print('Error?')     # Print error statement
        sure = '2'  # Set the loop to restart
    if sure == '1':     # Check if the user chose to continue
        printTextBox('Congratulations ' + alias + ', and welcome again to the world of pokémon! Enjoy the world!')
    elif sure == '2':   # Check if user chose to restart
        printTextBox('Please choose again')
    else:   # Check for errors
        print('An error occured, set up will restart')  # Print error code
        sure = '2'  # Set the setup to restart
    return sure     # Return the value of whether to restart or continue to the main code
    # MAKE SURE TO WRITE WHILE LOOP FOR THIS

def starterPick():  # Define starterPick as a function
    printTextBox('Choose your starter')
    starters = ['Bulbasaur', 'Charmander', 'Squirtle']
    printOptionList(starters) # Print the list of starter pokemon that the user can choose
    choice = getUserDecision(starters) # Ask for the index of the user's choice, then store it
    if starters[choice] == 'Bulbasaur':   # Check if user chose bulbasaur
        printTextBox('Congratulations! You chose Bulbasaur, the grass type pokémon!')
    elif starters[choice] == 'Charmander':  # Check if user chose charmander
        printTextBox('Congratulations! You chose Charmander, the fire type pokemon!')
    elif starters[choice] == 'Squirtle':  # Check if the user chose squirtle
        printTextBox('Congratulations! You chose Squirtle, the water type pokemon!')
    return starters[choice] # Return the starter pokemon that the user chose

def pokeMartGive(current_pokedollars, shopping_stuff):   # Define pokeMartGive as a function
    shopping_stuff.append('Quit the shop')  # Add quit the shop to the list to show
    pokeMartList(shopping_stuff)    # Call the pokeMartList function
    buy = getUserDecision(shopping_stuff)   # Take user's input on what to buy
    if shopping_stuff[buy] != 'Quit the shop':
        if shopping_stuff[buy] == 'Pokeball - ¥200':  # Check if user bought a pokeball
            current_pokedollars = decrementValue(current_pokedollars, 200)    # Subtract the cost from the user's balance
            print('You bought a Pokeball!')     # Tell user what they bought
        elif shopping_stuff[buy] == 'Potion - ¥150':  # Check if user bought a potion
            current_pokedollars = decrementValue(current_pokedollars, 150)    # Subtract the cost from the user's balance
            print('You bought a potion!')   # Tell user what they bought
        elif shopping_stuff[buy] == 'Elixir - ¥300':  # Check if the user bought an elixir
            current_pokedollars = decrementValue(current_pokedollars, 300)      # Subtract the cost from user's balance
            print('You bought an elixir!')  # Print to user what they bought
    shopping_stuff.remove('Quit the shop')
    return current_pokedollars  # Return the user's money to the main code

def pokeMartList(shopping_things):
    printTextBox('Welcome to the item shop!')
    printOptionList(shopping_things)

def printPokemonStats(pokemonname, maximumhp, currenthp):
    healthbar = 20 # Create a health bar with a length of 20 characters

    print('| ' + str(pokemonname)) # Print the name of the enemy's pokemon
    print('| HP: ' + str(currenthp) + ' / ' + str(maximumhp)) # Print the enemy's current health

    print('| ', end='') # Print the beginning of the health bar
    bars = int(healthbar * (currenthp / maximumhp)) # Calculate how much of the health bar is filled, cast the integer value of it, then store it
    emptyspaces = healthbar - bars # Calculate the number of how much of the health bar is empty
    print('█' * bars, end='') # Print the calculated number of bars
    print(' ' * emptyspaces, end='') # Print the calculated number of emptyspaces
    print('|') # Print the end of the health bar

    print('|______________________') # Print the bottom of the stats box
    print('') # Print an empty line

def printTextBox(message):
    textboxlength = 50 # Set all text boxes to be 50 characters long
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

def getUserDecision(optionlist):
    while True:
        try:
            index = input('Choose an option (Enter a number): ') # Ask for the user's decision as a number, then store it
            print('') # Print an empty line
            index = int(index) - 1 # Cast the integer value of the user's input, then store it
            optionlist[index] # Check to see if an option exists at the specified index
            break # Break the loop
        except ValueError:
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

printPokemonStats(enemyname, enemymaxhp, enemyhp) # Display the stats of the enemy pokemon
printPokemonStats(name[currentpokemon], maxhp[currentpokemon], hp[currentpokemon]) # Display the stats of the user's current pokemon

while (hp.count(0) != len(hp)) and (enemyhp > 0):
    printOptionList(battledecisions) # Display the battle decisions that the user can make
    decision = getUserDecision(battledecisions) # Get the battle decision that the user wants to make

    if battledecisions[decision] == 'Attack':
        attacks[currentpokemon].append('Go Back') # Add 'Go Back' to the list of options that the user can choose in the attack menu
        printOptionList(attacks[currentpokemon]) # Display the attacks of the current pokemon that the user can use

        while True:
            attack = getUserDecision(attacks[currentpokemon]) # Get the user's input for the attack they want to use

            if attacks[currentpokemon][attack] == 'Go Back':
                break # Exit the loop
            elif movepp[currentpokemon][attack] == 0:
                printTextBox('You do not have enough PP for that move!') # If the current pokemon doesn't have enough PP for a move, then tell the user that they don't have enough PP
            else:
                break # Exit the loop

        if attacks[currentpokemon][attack] != 'Go Back':
            movepp[currentpokemon][attack] = decrementValue(movepp[currentpokemon][attack], 1) # Decrement the current pokemon's PP by the amount required by the move
            enemyhp = decrementValue(enemyhp, movedmg[currentpokemon][attack]) # Decrement the enemy's HP by the damage value of the user's attack

            printTextBox(str(name[currentpokemon]) + ' used ' + str(attacks[currentpokemon][attack]) + '! ' + str(enemyname) + ' took ' + str(movedmg[currentpokemon][attack]) + ' damage!') # Display the user's attack, and the damage it dealt

            attack = getBotDecision(enemyattacks) # Get the enemy's input for the attack they want to use
            hp[currentpokemon] = decrementValue(hp[currentpokemon], enemymovedmg[attack]) # Decrement the current pokemon's HP by the damage value of the enemy's attack

            printTextBox(str(enemyname) + ' used ' + str(enemyattacks[attack]) + '! ' + str(name[currentpokemon]) + ' took ' + str(enemymovedmg[attack]) + ' damage!') # Display the enemy's attack, and the damage it dealt

            printPokemonStats(enemyname, enemymaxhp, enemyhp) # Display the stats of the enemy pokemon
            printPokemonStats(name[currentpokemon], maxhp[currentpokemon], hp[currentpokemon]) # Display the stats of the user's current pokemon

        attacks[currentpokemon].remove('Go Back') # Remove 'Go Back' from the list of options that the user can choose in the attack menu

    elif battledecisions[decision] == 'Open Inventory':
        if len(inventory) > 0:
            inventory.append('Go Back') # Add 'Go Back' to the list of options that the user can choose in the inventory menu
            printOptionList(inventory) # Display the items that the user can use
            item = getUserDecision(inventory) # Get the user's input for the item they want to use

            if inventory[item] != 'Go Back':
                if inventory[item] == 'Elixir':
                    attacks[currentpokemon].append('Go Back')
                    printOptionList(attacks[currentpokemon])

                    while True:
                        attack = getUserDecision(attacks[currentpokemon])

                        if attacks[currentpokemon][attack] == 'Go Back':
                            break
                        elif movepp[currentpokemon][attack] == maxpp[currentpokemon][attack]:
                            printTextBox('That move already has max PP!')
                        else:
                            break

                    if attacks[currentpokemon][attack] != 'Go Back':
                        movepp[currentpokemon][attack] = incrementValue(maxpp[currentpokemon][attack], movepp[currentpokemon][attack], 10) # Restore 10 of the player's PP
                        printTextBox('You used ' + str(item) + '! ' + str(name[currentpokemon]) + ' gained 10 PP!') # Display the used item, and how much PP their pokemon gained
                        del(inventory[item])

                    attacks[currentpokemon].remove('Go Back')

                elif inventory[item] == 'Potion':
                    hp[currentpokemon] = incrementValue(maxhp[currentpokemon], hp[currentpokemon], 10) # Restore 10 of the pokemon's HP
                    printTextBox('You used ' + str(item) + '! ' + str(name[currentpokemon]) + ' gained 10 HP!') # Display the used item, and how much HP their pokemon gained
                    del(inventory[item])

                printPokemonStats(enemyname, enemymaxhp, enemyhp) # Display the stats of the enemy's pokemon
                printPokemonStats(name[currentpokemon], maxhp[currentpokemon], hp[currentpokemon]) # Display the stats of the user's current pokemon

            inventory.remove('Go Back') # Remove 'Go Back' from the list of options that the user can choose in the inventory menu

        else:
            printTextBox('There is nothing in your inventory!') # If there is less than 1 item in the user's inventory, then tell the user that there is nothing in their inventory

    elif battledecisions[decision] == 'Change Pokemon':
        name.append('Go Back') # Add 'Go Back' to the list of options that the user can choose
        printOptionList(name) # Display the names of pokemon that the user can choose

        while True:
            newpokemon = getUserDecision(name) # Get the user's input for the new pokemon they want to switch to

            if name[newpokemon] == 'Go Back':
                break # Exit the loop
            elif newpokemon == currentpokemon:
                printTextBox(str(name[currentpokemon]) + ' is already summoned!') # If the pokemon they want to switch to is the same as the current pokemon, then tell the user that it's already summoned
            else:
                break # Exit the loop

        if name[newpokemon] != 'Go Back':
            printTextBox('You summoned ' + str(name[newpokemon]) + '!') # Display the pokemon that the user summoned

            printPokemonStats(enemyname, enemymaxhp, enemyhp) # Display the stats of the enemy's pokemon
            printPokemonStats(name[newpokemon], maxhp[newpokemon], hp[newpokemon]) # Display the stats of the user's new pokemon

            currentpokemon = newpokemon # Set the new pokemon as the user's current pokemon

        name.remove('Go Back')

    elif battledecisions[decision] == 'Flee':
        break # Exit the loop to end the battle

    else:
        print('Error: User entered an invaild decision.') # If the user somehow enters an option that is not in the list, then tell them that an error occurred

    if (hp[currentpokemon] == 0) and (battledecisions.count('Attack') == 1):
        battledecisions.remove('Attack') # If the user's current pokemon has 0 HP, and they have the option to attack, then remove the option to attack
    elif (hp[currentpokemon] > 0) and (battledecisions.count('Attack') == 0):
        battledecisions.insert(0, 'Attack') # If the user's current pokemon has more than 0 HP, and they don't have the option to attack, then add the option to attack
