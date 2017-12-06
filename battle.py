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
