# Authors: Kevin Quijalvo and Erik Kozy
# Date: November 29 2017
# File Name: pokemon.py
# Description: Very small pokemon RPG

import random # Import the random library

# User stats
name = ''
money = 500   # Set the players money (They will start with 500)
inventory = ['Pokèball', 'Pokèball']  # Set user's inventory
currentpokemon = 0 # Index of the user's current pokemon

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
enemypokemon = 0 # Index of the enemy's current pokemon

# Stats of all pokemon
pokemonnames = ['Bulbasaur', 'Charmander', 'Squirtle', 'Rattata', 'Pidgey', 'Geodude', 'Onix', 'Staryu', 'Starmie', 'Rhyhorn', 'Nidoran♂', 'Nidoran♀', 'Caterpie'] # List of the names of every pokemon
pokemontypes = ['Grass', 'Fire', 'Water', 'Normal', 'Flying', 'Rock', 'Rock', 'Water', 'Water', 'Rock', 'Poison', 'Poison', 'Bug'] # List of every pokemon's type
pokemonattacks = [['Vine Whip', 'Razor Leaf'], ['Ember', 'Flame Burst'], ['Bubble', 'Water Gun'], ['Tackle'], ['Gust'], ['Rock Smash', 'Rock Slide'], ['Rock Slide', 'Earthquake'], ['Bubble', 'Water Gun'], ['Bubble', 'Surf'], ['Rock Smash', 'Earthquake'], ['Poison Sting', 'Poison Jab'], ['Poison Sting', 'Poison Jab'], ['Tackle']] # List of the attacks of every pokemon
pokemondmg = [[3, 5], [3, 5], [3, 5], [3], [3], [1, 3], [3, 4], [2, 4], [2, 5], [2, 5], [1, 4], [1, 4], [3]] # List of the default damage values for the attacks of every pokemon
pokemonpp = [[30, 10], [30, 10], [30, 10], [30], [40], [20, 10], [20, 10], [20, 20], [20, 10], [30, 10], [40, 15], [40, 15], [40]] # List of the default PP values for the attacks of every pokemon
pokemonhp = [65, 65, 65, 20, 20, 35, 55, 40, 60, 60, 20, 20, 15] # List of the default HP values of every pokemon

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

    flag = True
    while flag == True:
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
            flag = False

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

printTextBox('Hello there! Welcome to the world of pokémon! My name is Oak! People call me the pokémon Prof!')
input('Press Enter to continue:')    # Take input to continue

printTextBox('This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights. Myself... I study pokémon as a profession.')
input('Press Enter to continue:')    # Take input to continue

printTextBox('You may type the letter H (not case sensitive) at any choice throughout your journey for help.')
input('Press Enter to continue:')

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
    enemy = pokemonnames.index('Bulbasaur')

elif userpartynames.count('Bulbasaur') == 1:
    enemy = pokemonnames.index('Squirtle')

else:
    enemy = pokemonnames.index('Charmander')

enemypartynames.append(pokemonnames[enemy])
enemypartytypes.append(pokemontypes[enemy])
enemypartyattacks.append(pokemonattacks[enemy].copy())
enemypartydmg.append(pokemondmg[enemy].copy())
enemypartyhp.append(pokemonhp[enemy])
enemypartymaxhp.append(pokemonhp[enemy])

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
    encounter_chance = random.random()

    if encounter_chance > 0.5:
        enemy = pokemonnames.index('Pidgey')
        printTextBox('You encountered a Pidgey!')

    else:
        enemy = pokemonnames.index('Rattata')
        printTextBox('You encountered a Rattata!')

    enemypartynames = [pokemonnames[enemy]]
    enemypartytypes = [pokemontypes[enemy]]
    enemypartyattacks = [pokemonattacks[enemy].copy()]
    enemypartydmg = [pokemondmg[enemy].copy()]
    enemypartyhp = [pokemonhp[enemy]]
    enemypartymaxhp = [pokemonhp[enemy]]

    battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, False)

printTextBox('You continue on your path towards the next city. On your journey, you see a pokémon trainer.')    # Print text box
input('Press Enter to continue:')    # Take input to continue

printTextBox('You have been challenged to a battle by Ace Trainer Ganti!')  # Tell user of challenge
input('Press Enter to continue:')    # Take input to continue

enemy = pokemonnames.index('Rattata')
enemypartynames = [pokemonnames[enemy]]
enemypartytypes = [pokemontypes[enemy]]
enemypartyattacks = [pokemonattacks[enemy].copy()]
enemypartydmg = [pokemondmg[enemy].copy()]
enemypartyhp = [pokemonhp[enemy]]
enemypartymaxhp = [pokemonhp[enemy]]
printTextBox('The enemy summons a Rattata!')

battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, True)

money += 200     # Add money to user's balance
printTextBox('¥200 has been added to your inventory.')  # Tell user they won money

printTextBox('After defeating Ganti, you continue on the route. Again, you see a pokémon trainer. This time a lass.')   # Print text box
input('Press Enter to continue:')    # Take input to continue

printTextBox('You have been challenged by Pokèmon Lass Ariel!')     # Tell user of challenge
input('Press Enter to continue:')    # Take input to continue

enemy = pokemonnames.index('Pidgey')
enemypartynames = [pokemonnames[enemy]]
enemypartytypes = [pokemontypes[enemy]]
enemypartyattacks = [pokemonattacks[enemy].copy()]
enemypartydmg = [pokemondmg[enemy].copy()]
enemypartyhp = [pokemonhp[enemy]]
enemypartymaxhp = [pokemonhp[enemy]]
printTextBox('The enemy summons a Pidgey!')

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

        userpartyhp = userpartymaxhp.copy()
        for index in range(0, len(userpartypp)):
            userpartypp[index] = userpartymaxpp[index].copy()
            
        printTextBox('HP and PP has been restored for all of your pokemon!')

    elif viridian_options[viridian_choice] == 'Pokèmart':  # Check if user chose to go to the pokemart
        printTextBox('You have chosen to go to the Pokèmart.')  # tell user their choice
        input('Press enter to continue: ')   # Pause until user continues

        shopping_results = buyItem(shop, money)
        money = shopping_results[0]
        inventory.extend(shopping_results[1:])

    elif viridian_options[viridian_choice] == 'Pokèmon Gym':  # Check if user chose to go to the Pokèmon Gym
        printTextBox('You have chosen to go to the Pokèmon Gym.')   # Tell user their choice
        input('Press enter to continue: ')   # Pause until user continues

        printTextBox('Hi, Im Brock! Im the gym leader in this city, and I specialize with Rock types!')   # Print Brock's speech
        input('Press enter to continue: ')   # Pause until user continues

        printTextBox('If you have come to battle me, then good luck!')  # Print Brock's speech
        input('Press enter to continue: ')   # Pause until user continues

        printTextBox('You have been challenged to a battle by Viridian City Gym Leader Brock!')     # Print challenge

        enemy = pokemonnames.index('Geodude')
        enemypartynames = [pokemonnames[enemy]]
        enemypartytypes = [pokemontypes[enemy]]
        enemypartyattacks = [pokemonattacks[enemy].copy()]
        enemypartydmg = [pokemondmg[enemy].copy()]
        enemypartyhp = [pokemonhp[enemy]]
        enemypartymaxhp = [pokemonhp[enemy]]

        enemy = pokemonnames.index('Onix')
        enemypartynames.append(pokemonnames[enemy])
        enemypartytypes.append(pokemontypes[enemy])
        enemypartyattacks.append(pokemonattacks[enemy].copy())
        enemypartydmg.append(pokemondmg[enemy].copy())
        enemypartyhp.append(pokemonhp[enemy])
        enemypartymaxhp.append(pokemonhp[enemy])

        printTextBox('The enemy summons a Geodude!')
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

enemy = pokemonnames.index('Nidoran♂')
enemypartynames = [pokemonnames[enemy]]
enemypartytypes = [pokemontypes[enemy]]
enemypartyattacks = [pokemonattacks[enemy].copy()]
enemypartydmg = [pokemondmg[enemy].copy()]
enemypartyhp = [pokemonhp[enemy]]
enemypartymaxhp = [pokemonhp[enemy]]
printTextBox('The enemy summons a Nidoran♂!')

battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, True)

money += 200    # Add money to user's balance
printTextBox('¥200 has been added to your inventory.')  # Tell user they won money
input('Press Enter to continue:')    # Take input to continue

printTextBox('After defeating Paul, you continue on the route. You discover some tall grass. Would you like to walk in it and discover a Pokèmon?')     # Tell user about grass
input('Press enter to continue: ')   # Pause until user continues

printOptionList(tallGrassChoice)    # Print the choices that the user can choose
tall_grass = getUserDecision('', 'Go in the grass to encounter a pokemon, or Continue walking on the current route', tallGrassChoice)    # Take user input on their choice

if tallGrassChoice[tall_grass] == 'Go in the grass':     # Check if user chose to go into the grass 
    encounter_chance = random.random()

    if encounter_chance > 0.5:
        enemy = pokemonnames.index('Nidoran♂')
        printTextBox('You encountered a Nidoran♂')

    else:
        enemy = pokemonnames.index('Nidoran♀')
        printTextBox('You encountered a Nidoran♀!')

    enemypartynames = [pokemonnames[enemy]]
    enemypartytypes = [pokemontypes[enemy]]
    enemypartyattacks = [pokemonattacks[enemy].copy()]
    enemypartydmg = [pokemondmg[enemy].copy()]
    enemypartyhp = [pokemonhp[enemy]]
    enemypartymaxhp = [pokemonhp[enemy]]

    battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, False)

printTextBox('You continue walking. As you are walking, you spot another pokèmon trainer! You confront her and she challenges you to a pokèmon battle!')    # Print challenge
input('Press enter to continue: ')   # Pause until user continues

printTextBox('You have been challenged to a battle by Bug Catcher Amanda!')     # Print challenge
input('Press enter to continue: ')   # Pause until user continues

enemy = pokemonnames.index('Caterpie')
enemypartynames = [pokemonnames[enemy]]
enemypartytypes = [pokemontypes[enemy]]
enemypartyattacks = [pokemonattacks[enemy].copy()]
enemypartydmg = [pokemondmg[enemy].copy()]
enemypartyhp = [pokemonhp[enemy]]
enemypartymaxhp = [pokemonhp[enemy]]
printTextBox('The enemy summons a Caterpie!')

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

        userpartyhp = userpartymaxhp.copy()
        for index in range(0, len(userpartypp)):
            userpartypp[index] = userpartymaxpp[index].copy()
        printTextBox('HP and PP has been restored for all of your pokemon!')

    elif pewter_options[pewter_choice] == 'Pokèmart':    # Check if user chose to go to the pokemart
        printTextBox('You have chosen to go to the Pokèmart.')  # tell user their choice
        input('Press enter to continue: ')   # Pause until user continues

        shopping_results = buyItem(shop, money)
        money = shopping_results[0]
        inventory.extend(shopping_results[1:])

    elif pewter_options[pewter_choice] == 'Pokèmon Gym':  # Check if user chose to go to the Pokèmon Gym
        printTextBox('You have chosen to go to the Pokèmon Gym.')   # Tell user their choice
        input('Press enter to continue: ')   # Pause until user continues

        printTextBox('Hey there, im Misty. I specialize with water types, and im your battle today!')   # Print Misty's speech
        input('Press enter to continue: ')   # Pause until user continues

        printTextBox('You have been challenged to a battle by Pewter City Gym Leader Misty!')   # Print challenge

        enemy = pokemonnames.index('Staryu')
        enemypartynames = [pokemonnames[enemy]]
        enemypartytypes = [pokemontypes[enemy]]
        enemypartyattacks = [pokemonattacks[enemy].copy()]
        enemypartydmg = [pokemondmg[enemy].copy()]
        enemypartyhp = [pokemonhp[enemy]]
        enemypartymaxhp = [pokemonhp[enemy]]

        enemy = pokemonnames.index('Starmie')
        enemypartynames.append(pokemonnames[enemy])
        enemypartytypes.append(pokemontypes[enemy])
        enemypartyattacks.append(pokemonattacks[enemy].copy())
        enemypartydmg.append(pokemondmg[enemy].copy())
        enemypartyhp.append(pokemonhp[enemy])
        enemypartymaxhp.append(pokemonhp[enemy])

        printTextBox('The enemy summons a Staryu!')
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
    enemy = pokemonnames.index('Squirtle')
    printTextBox('The enemy summons a Squirtle!')

elif userpartynames.count('Charmander') == 1:  # Check user's starter to determine Blue's starter
    enemy = pokemonnames.index('Bulbasaur')
    printTextBox('The enemy summons a Bulbasaur!')

elif userpartynames.count('Squirtle') == 1:     # Check the user's starter to determine Blue's starter
    enemy = pokemonnames.index('Charmander')
    printTextBox('The enemy summons a Charmander!')

else:   # Check for errors
    print('Exception not handled - contact programmer')     # Print error

enemypartynames = [pokemonnames[enemy]]
enemypartytypes = [pokemontypes[enemy]]
enemypartyattacks = [pokemonattacks[enemy].copy()]
enemypartydmg = [pokemondmg[enemy].c]
enemypartyhp = [pokemonhp[enemy]]
enemypartymaxhp = [pokemonhp[enemy]]

enemy = pokemonnames.index('Rhyhorn')
enemypartynames.append(pokemonnames[enemy])
enemypartytypes.append(pokemontypes[enemy])
enemypartyattacks.append(pokemonattacks[enemy].copy())
enemypartydmg.append(pokemondmg[enemy].copy())
enemypartyhp.append(pokemonhp[enemy])
enemypartymaxhp.append(pokemonhp[enemy])

battleresults = battleSequence(userpartynames, userpartytypes, userpartyattacks, userpartydmg, userpartypp, userpartymaxpp, userpartyhp, userpartymaxhp, inventory, enemypartynames, enemypartytypes, enemypartyattacks, enemypartydmg, enemypartyhp, enemypartymaxhp, True)

printTextBox('Congratulations on defeating Pokèmon Trainer Blue!')  # Print Blue's text
input('Press Enter to continue:')    # Take input to continue

printTextBox('Well, ' + name + ', it seems you have defeated me. Congratulations, you are the greater trainer!')    # Print Blue's text
input('Press Enter to continue:')    # Take input to continue

printTextBox('That brings you to the end of your adventure! To continue, please purchase non-existant DLC with non-existant currency!')    # Print ending message
