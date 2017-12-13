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
            print(str(index + 1) + '. ' + options[index] + ' ' + str(currentpp[index]) + ' / ' + str(maximumpp[index]) + ' PP')

        except IndexError:
            print(str(index + 1) + '. ' + options[index])

    flag = True
    while flag == True:
        attack = getUserDecision('Choose an attack', 'Choose which move you want to attack the enemy with. PP stands for Power Points, and represents how many times you can use it. Lower PP moves are usually stronger.', options)

        if options[attack] == 'Go Back':
            attack = 'Go Back'
            flag = False

        elif currentpp[attack] == 0:
            print('You do not have enough PP for that move!')

        else:
            flag = False

    options.remove('Go Back')

    return attack # Return the index of the chosen attack (or return 'Go Back' if they chose to go back)

def chooseItem(options, maximumhp, currenthp, maximumpp, currentpp, trainerbattle):
    options.append('Go Back') # Add 'Go Back' as an option in the item menu
    printOptionList(options) # Print the list of options that the user can choose in the item menu

    flag = True
    while flag == True:
        item = getUserDecision('Choose an item', 'Choose an item to use. Elixirs restore PP, Potions restore HP, and Pokèballs allow you to capture a pokemon', options)

        if options[item] == 'Go Back':
            item = 'Go Back'
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
            new = 'Go Back'
            flag = False # Exit the loop if they choose to go back

        elif new == current:
            print(str(options[new]) + ' is already summoned!') # If the pokemon they chose is already summoned, then tell the user

        else:
            printTextBox('You summoned '+ str(options[new]) + '!')
            flag = False # Exit the loop once they choose a pokemon to summon

    options.remove('Go Back') # Remove 'Go Back' as an option once they leave the "Change Pokemon" Menu

    return new # Return the index of the user's new pokemon (or return 'Go Back' if they chose to go back)

def battleSequence(party1names, party1types, party1attacks, party1dmg, party1pp, party1maxpp, party1hp, party1maxhp, items, party2names, party2types, party2attacks, party2dmg, party2hp, party2maxhp, trainerbattle):
    currentpokemon = 0
    enemypokemon = 0
    printPokemonStats(party2names[enemypokemon], party2maxhp[enemypokemon], party2hp[enemypokemon]) # Display the stats of the enemy pokemon
    printPokemonStats(party1names[currentpokemon], party1maxhp[currentpokemon], party1hp[currentpokemon]) # Display the stats of the user's current pokemon

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
            printTextBox('You have no more pokemon to summon! You lost the battle!')
            battleflag = False

        elif (party1hp[currentpokemon] == 0) and (battledecisions.count('Attack') == 1):
            battledecisions.remove('Attack') # If the user's current pokemon has 0 HP, and they have the option to attack, then remove the option to attack

        elif (party1hp[currentpokemon] > 0) and (battledecisions.count('Attack') == 0):
            battledecisions.insert(0, 'Attack') # If the user's current pokemon has more than 0 HP, and they don't have the option to attack, then add the option to attack

        if party2hp.count(0) == len(party2hp):
            printTextBox('You won the battle!') # If all of the enemy's pokemon has 0 HP, then tell the user they won the battle
            battleflag = False # Set the battle flag to False to end the battle sequence

        elif (party2hp[enemypokemon] == 0):
            enemypokemon += 1 # Summon a new enemy by changing the index of the enemy pokemon
            printTextBox('The enemy summons ' + str(party2names[enemypokemon]) + '!') # Tell the user the enemy's new pokemon
            printPokemonStats(party2names[enemypokemon], party2maxhp[enemypokemon], party2hp[enemypokemon]) # Display the stats of the enemy's pokemon
            printPokemonStats(party1names[currentpokemon], party1maxhp[currentpokemon], party1hp[currentpokemon]) # Display the stats of the user's pokemon

    return [party1names, party1types, party1attacks, party1dmg, party1pp, party1maxpp, party1hp, party1maxhp, items] # Return the user's whole party, and their stats after the battle

