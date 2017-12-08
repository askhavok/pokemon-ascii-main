def calculateBonusDamage(damagevalue, attackertype, defendanttype):
    criticalchance = random.random() # Generate a random number between 0 and 1

    if (attackertype == 'Grass') and (defendanttype == 'Fire'):
        damagevalue /= 2 # If the attacker's type is Grass, and the defendant's type is Fire, then cut the damage value of the attack in half
    elif (attackertype == 'Grass') and (defendanttype == 'Water'):
        damagevalue *= 2 # If the attacker's type is Grass, and the defendant's type is Water, then double the damage value of the attack
    elif (attackertype == 'Grass') and (defendanttype == 'Flying'):
        damagevalue /= 2 # If the attacker's type is Grass and the defendant's type is Flying, then cut the damage value of the attack in half
    elif (attackertype == 'Grass') and (defendanttype == 'Grass'):
        damagevalue /= 2 # If the attacker and defendant's type is both Grass, then cut the damage value of the attack in half
    elif (attackertype == 'Fire') and (defendanttype == 'Grass'):
        damagevalue *= 2 # If the attacker's type is Fire and the defendant's type is Grass, then double the damage value of the attack
    elif (attackertype == 'Fire') and (defendanttype == 'Water'):
        damagevalue /= 2 # If the attacker's type is Fire, and the defendant's type is Water, then cut the damage value of the attack in half
    elif (attackertype == 'Fire') and (defendanttype == 'Fire'):
        damagevalue /= 2 # If the attacker and defendant's type is both Fire, then cut the damage value of the attack in half
    elif (attackertype == 'Water') and (defendanttype == 'Grass'):
        damagevalue /= 2 # If the attacker's type is Water, and the defendant's type is Grass, then cut the damage value of the attack in half
    elif (attackertype == 'Water') and (defendanttype == 'Fire'):
        damagevalue *= 2 # If the attacker's type is Water, and the defendant's type is Fire, then double the damage value of the attack
    elif (attackertype == 'Water') and (defendanttype == 'Water'):
        damagevalue /= 2 # If the attacker and the defendant's type is both Water, then cut the damage value of the attack in half
    elif (attackertype == 'Flying') and (defendanttype == 'Grass'):
        damagevalue *= 2 # If the attacker's type is Flying and the defendant's type is Grass, then double the damage value of the attack

    if criticalchance < 0.1:
        damagevalue += 0.5 * damagevalue # Increase the damage value of the current attack by 50% if the random number is below 0.1 (10% chance)

    damagevalue = int(damagevalue) # Cast the integer value of damage value, then store it

    return damagevalue # Return the amount of damage dealt

printPokemonStats(enemypartynames[enemypokemon], enemypartymaxhp[enemypokemon], enemypartyhp[enemypokemon]) # Display the stats of the enemy pokemon
printPokemonStats(partynames[currentpokemon], partymaxhp[currentpokemon], partyhp[currentpokemon]) # Display the stats of the user's current pokemon

flag = True # Set the flag to true to start the battle sequence
while (partyhp.count(0) != len(partyhp)) and (enemypartyhp.count(0) != len(enemypartyhp)) and (flag == True):
    printOptionList(battledecisions) # Display the battle decisions that the user can make
    decision = getUserDecision('What will you do?', battledecisions) # Get the battle decision that the user wants to make

    if battledecisions[decision] == 'Attack':
        partyattacks[currentpokemon].append('Go Back') # Add 'Go Back' to the list of options that the user can choose in the attack menu
        printOptionList(partyattacks[currentpokemon]) # Display the attacks of the current pokemon that the user can use

        flag = True # Set the flag to true to run the while loop
        while flag == True:
            attack = getUserDecision('Choose an attack', partyattacks[currentpokemon]) # Get the user's input for the attack they want to use

            if partyattacks[currentpokemon][attack] == 'Go Back':
                flag = False # Exit the loop
            elif partypp[currentpokemon][attack] == 0:
                printTextBox('You do not have enough PP for that move!') # If the current pokemon doesn't have enough PP for a move, then tell the user that they don't have enough PP
            else:
                flag = False # Exit the loop

        if partyattacks[currentpokemon][attack] != 'Go Back':
            partypp[currentpokemon][attack] = decrementValue(partypp[currentpokemon][attack], 1) # Decrement the current pokemon's PP by the amount required by the move
            damage = calculateBonusDamage(partydmg[currentpokemon][attack], partytypes[currentpokemon], enemypartytypes[enemypokemon])
            enemypartyhp[enemypokemon] = decrementValue(enemypartyhp[enemypokemon], damage) # Decrement the enemy's HP by the damage value of the user's attack

            printTextBox(str(partynames[currentpokemon]) + ' used ' + str(partyattacks[currentpokemon][attack]) + '! ' + str(enemypartynames[enemypokemon]) + ' took ' + str(damage) + ' damage!') # Display the user's attack, and the damage it dealt

            if enemypartyhp[enemypokemon] != 0:
                attack = getBotDecision(enemypartyattacks[enemypokemon]) # Get the enemy's input for the attack they want to use
                damage = calculateBonusDamage(enemypartydmg[enemypokemon][attack], enemypartytypes[enemypokemon], partytypes[currentpokemon])
                partyhp[currentpokemon] = decrementValue(partyhp[currentpokemon], damage) # Decrement the current pokemon's HP by the damage value of the enemy's attack

                printTextBox(str(enemypartynames[enemypokemon]) + ' used ' + str(enemypartyattacks[enemypokemon][attack]) + '! ' + str(partynames[currentpokemon]) + ' took ' + str(damage) + ' damage!') # Display the enemy's attack, and the damage it dealt

                if partyhp[currentpokemon] == 0:
                    printTextBox(str(partynames[currentpokemon]) + ' fainted!')

            printPokemonStats(enemypartynames[enemypokemon], enemypartymaxhp[enemypokemon], enemypartyhp[enemypokemon]) # Display the stats of the enemy pokemon
            printPokemonStats(partynames[currentpokemon], partymaxhp[currentpokemon], partyhp[currentpokemon]) # Display the stats of the user's current pokemon

        partyattacks[currentpokemon].remove('Go Back') # Remove 'Go Back' from the list of options that the user can choose in the attack menu

    elif battledecisions[decision] == 'Open Inventory':
        if len(inventory) > 0:
            inventory.append('Go Back') # Add 'Go Back' to the list of options that the user can choose in the inventory menu
            printOptionList(inventory) # Display the items that the user can use
            item = getUserDecision('Choose an item', inventory) # Get the user's input for the item they want to use

            if inventory[item] != 'Go Back':
                if inventory[item] == 'Elixir':
                    partyattacks[currentpokemon].append('Go Back')
                    printOptionList(partyattacks[currentpokemon])

                    flag = True # Set the flag to true to run the while loop
                    while flag == True:
                        attack = getUserDecision('Which attack do you want to restore?', partyattacks[currentpokemon])

                        if partyattacks[currentpokemon][attack] == 'Go Back':
                            flag = False # Exit the loop
                        elif partypp[currentpokemon][attack] == partypp[currentpokemon][attack]:
                            printTextBox('That move already has max PP!')
                        else:
                            flag = False # Exit the loop

                    if partyattacks[currentpokemon][attack] != 'Go Back':
                        partypp[currentpokemon][attack] = incrementValue(partypp[currentpokemon][attack], partypp[currentpokemon][attack], 10) # Restore 10 of the player's PP
                        printTextBox('You used ' + str(item) + '! ' + str(partynames[currentpokemon]) + ' gained 10 PP!') # Display the used item, and how much PP their pokemon gained
                        del(inventory[item])

                    partyattacks[currentpokemon].remove('Go Back')

                elif inventory[item] == 'Potion':
                    partyhp[currentpokemon] = incrementValue(partymaxhp[currentpokemon], partyhp[currentpokemon], 10) # Restore 10 of the pokemon's HP
                    printTextBox('You used ' + str(item) + '! ' + str(partynames[currentpokemon]) + ' gained 10 HP!') # Display the used item, and how much HP their pokemon gained
                    del(inventory[item])

                printPokemonStats(enemypartynames[enemypokemon], enemypartymaxhp[enemypokemon], enemypartyhp[enemypokemon]) # Display the stats of the enemy's pokemon
                printPokemonStats(partynames[currentpokemon], partymaxhp[currentpokemon], partyhp[currentpokemon]) # Display the stats of the user's current pokemon

            inventory.remove('Go Back') # Remove 'Go Back' from the list of options that the user can choose in the inventory menu

        else:
            printTextBox('There is nothing in your inventory!') # If there is less than 1 item in the user's inventory, then tell the user that there is nothing in their inventory

    elif battledecisions[decision] == 'Change Pokemon':
        partynames.append('Go Back') # Add 'Go Back' to the list of options that the user can choose
        printOptionList(partynames) # Display the names of pokemon that the user can choose

        flag = True # Set the flag to run the while loop
        while flag == True:
            newpokemon = getUserDecision('Which pokemon do you want to summon?', partynames) # Get the user's input for the new pokemon they want to switch to

            if partynames[newpokemon] == 'Go Back':
                flag = False # Exit the loop
            elif newpokemon == currentpokemon:
                printTextBox(str(partynames[currentpokemon]) + ' is already summoned!') # If the pokemon they want to switch to is the same as the current pokemon, then tell the user that it's already summoned
            else:
                flag = False # Exit the loop

        if partynames[newpokemon] != 'Go Back':
            printTextBox('You summoned ' + str(partynames[newpokemon]) + '!') # Display the pokemon that the user summoned

            printPokemonStats(enemypartynames[enemypokemon], enemypartymaxhp[enemypokemon], enemypartyhp[enemypokemon]) # Display the stats of the enemy's pokemon
            printPokemonStats(partynames[newpokemon], partymaxhp[newpokemon], partyhp[newpokemon]) # Display the stats of the user's new pokemon

            currentpokemon = newpokemon # Set the new pokemon as the user's current pokemon

        partynames.remove('Go Back')

    elif battledecisions[decision] == 'Flee':
        flag = False # Exit the loop to end the battle

    if (partyhp[currentpokemon] == 0) and (battledecisions.count('Attack') == 1):
        battledecisions.remove('Attack') # If the user's current pokemon has 0 HP, and they have the option to attack, then remove the option to attack
    elif (partyhp[currentpokemon] > 0) and (battledecisions.count('Attack') == 0):
        battledecisions.insert(0, 'Attack') # If the user's current pokemon has more than 0 HP, and they don't have the option to attack, then add the option to attack

    if enemypartyhp[enemypokemon] == 0:
        printTextBox(str(enemypartynames[enemypokemon]) + ' fainted! The enemy summons ' + str(enemypartynames[enemypokemon + 1]) + '!')
        enemypokemon += 1
        printPokemonStats(enemypartynames[enemypokemon], enemypartymaxhp[enemypokemon], enemypartyhp[enemypokemon]) # Display the stats of the enemy's pokemon
        printPokemonStats(partynames[newpokemon], partymaxhp[newpokemon], partyhp[newpokemon]) # Display the stats of the user's new pokemon
1