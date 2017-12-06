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

def setGender():   # Define setGender as a function
    genders = ['Boy', 'Girl'] # Create a list of available genders that the user can choose
    printTextBox('Hello there! Welcome to the world of pokémon! My name is Oak! People call me the pokémon Prof!')
    printTextBox('This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights. Myself... I study pokémon as a profession.')
    printTextBox('Are you a boy or a girl?')
    printOptionList(genders) # Print the list of gender that the user can choose
    choice = getUserDecision(genders) # Ask for the index of the user's decision, then store it
    return genders[choice]   # Return the user's gender to the main code

def setName():    # Define setName as a function
    alias = '0'    # Set the user's name blank
    printTextBox('What is your name?')
    alias = input(': ')     # Print Oak's speech
    return alias    # Return the user's name to the main code

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