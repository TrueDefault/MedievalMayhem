import random

# These are the stats for each chaarcter. They are formatted as [health, attack, defense, speed]
KNIGHT_STATS = [200, 1, 1.5, 1]
ASSASSIN_STATS = [100, 2.2, 0.8, 1.5]
WITCH_STATS = [100, 1, 0.75, 2]
GOLEM_STATS = [75, 1.13, 2, 0.82]
WIZARD_STATS = [83, 2, 0.82, 1]
VAMPIRE_STATS = [180, 1.2, 0.9, 0.85]
PRIEST_STATS = [100, 1, 1, 1]

# The description of the game and the chracters are printed here
print("Welcome to our  game! In this game, you and another player will pick a character and fight.")
print(" ")
print("Each character has a basic and strong attack.")
print("They can also recover each turn. You can use the basic attack 10 times, the strong attack 7 times, and recover 4 times.")
print("The basic attack is just an attack. The strong attack is stronger but has a chance to miss.") 
print("Both attacks have a chance to be critical hits, but the strong attack has a small chance to be a strong critical hit and an even smaller one to be an insane critical hit.")
print("Each character also has four stats, Those are health points, attack, defense, and speed.")
print("Healthpoints determine how much health you have left.") 
print("Your attack and your enemy's defense will determine how much damage your attacks will do, and vice versa.")
print("Speed determines who goes first. If the speed is the same, one character will randomly be chosen to go first every turn.")
print(" ")
print("The first character is the knight. The knight has high health and defense, and average speed and attack.")
print(" ")
print("The second character is the assassin. The assassin has high attack and speed, but average health and low defense.")
print(" ")
print("The third character is the witch. The witch has very high speed, average attack and health, and low defense. Her attacks can poison the enemy, which will deal damage every turn the enemy attacks.")
print(" ")
print("The fourth character is the golem. The golem has very high defense, above-average attack, and low health and speed. Its attacks set down rocks every turn, which will deal damage every turn the enemy attacks.")
print(" ")
print("The fifth character is the wizard. The wizard has very high attack, average speed, and low health and defense.") 
print("His basic attack can cause a burn, which will deal damage every turn the enemy attacks. His strong attack can shock the enemy, preventing them from moving the turn afterward.") 
print("If an enemy is shocked while burned, the burn will go away.")
print(" ")
print("The sixth character is the vampire. The vampire has very high health, above-average attack, and low defense and speed. Her attacks will always heal her.")
print(" ")
print("The seventh character is the priest. The priest has average stats. Every time the priest attacks, the priests attack, defense, or speed will increase.")
print(" ")

# We will ask the players which characters the want to use, and then set their stats up
player1class = int(input("Player 1, do you want to be a knight(1), an assassin(2), a witch(3), a golem(4), a wizard(5), a vampire(6), or a priest(7)?"))
if player1class == 1:
    player1basestats = KNIGHT_STATS
elif player1class == 2:
    player1basestats = ASSASSIN_STATS
elif player1class == 3:
    player1basestats = WITCH_STATS
elif player1class == 4:
    player1basestats = GOLEM_STATS
elif player1class == 5:
    player1basestats = WIZARD_STATS
elif player1class == 6:
    player1basestats = VAMPIRE_STATS
elif player1class == 7:
    player1basestats = PRIEST_STATS
player1moves = [10, 7, 4]
p1_small_rocks = 0
p1_big_rocks = 0
player1status = ""

p1stats = [player1class, player1status, player1moves, p1_small_rocks, p1_big_rocks, player1basestats[0], player1basestats[1], player1basestats[2], player1basestats[3], player1basestats[0], 1]

player2class = int(input("Player 2, do you want to be a knight(1), an assassin(2), a witch(3), a golem(4), a wizard(5), a vampire(6), or a preist(7)?"))
if player2class == 1:
    player2basestats = KNIGHT_STATS
elif player2class == 2:
    player2basestats = ASSASSIN_STATS
elif player2class == 3:
    player2basestats = WITCH_STATS
elif player2class == 4:
    player2basestats = GOLEM_STATS
elif player2class == 5:
    player2basestats = WIZARD_STATS
elif player2class == 6:
    player2basestats = VAMPIRE_STATS
elif player2class == 7:
    player2basestats = PRIEST_STATS
player2moves = [10, 7, 4]
p2_small_rocks = 0
p2_big_rocks = 0
player2status = ""

p2stats = [player2class, player2status, player2moves, p2_small_rocks, p2_big_rocks, player2basestats[0], player2basestats[1], player2basestats[2], player2basestats[3], player2basestats[0], 2]

# This function is used for both attack, the basic and strong attack
def attack(enemy_health, attack, enemy_defense, playerclass, enemystatus, small_rocks, big_rocks, playerhealth, move):
    if move == 1:
        # This is what happens when the player uses the basic attack
        #T The crit increases the amount of damage done.
        crit = random.randint(1,5)
        x = (random.randint(20, 30) * attack)/enemy_defense
        if crit == 1:
            x = x * 1.5
            x = int(x)
            print("You got a critical hit! Your attack did " + str(x) + " damage!")
        else:
            x = int(x)
            print("Your attack did " + str(x) + " damage!")

        # If the player is a witch, there is a chance the enemy will get poisoned, and if the player is a wizard, there is a chance the enemy will be burned
        if enemystatus == "":
            if playerclass == 3:
                enemystatus = "mild poison"
                print("The enemy was poisoned.")
            if playerclass == 5:
                burn = random.randint(1,2)
                if burn == 1:
                    enemystatus = "burn"
                    print("The enemy was burned.")
        
        # If the player is a golem, a rock will be placed on the field.
        if playerclass == 4:
            small_rocks += 1
            print("A small rock was placed on the field.")
        
        # If the player is a vampire, they will gain some health
        if playerclass == 6:
            health_gained = int(x/2)
            playerhealth = playerhealth + health_gained
            if playerhealth > 200:
                playerhealth = 200
                print("You got to full health!")
            else:
                print("You gained " + str(health_gained) + " health!")
        
        enemy_health = enemy_health - x
        return [enemy_health, enemystatus, small_rocks, playerhealth]
    else:
        # This is what happens when the player uses a strong attack
        # The kind of crit the attack will be is determined here
        for i in range(3):
            crit_chance = random.randint(1, 5)
            if crit_chance == 1:
                if i == 0:
                    crit = 5
                elif i == 1:
                    crit = 6
                elif i == 2:
                    crit = 7
            else:
                crit = 0
                break
        
        # miss chance is determined here
        miss = random.randint(1, 5)
        # damage is calculated here
        x = (random.randint(40, 50) * attack)/enemy_defense
        if miss == 1:
            x = 0
            print("Your attack missed.")
        else:
            if crit == 5:
                x = x * 1.5
                x = int(x)
                print("You got a critical hit! Your attack did " + str(x) + " damage!")
            elif crit == 6:
                x = x * 2
                x = int(x)
                print("You got a strong critical hit! Your attack did " + str(x) + " damage!")
            elif crit == 7:
                x = x * 2
                x = int(x)
                print("You got an insane critical hit! Your attack did " + str(x) + " damage!")
            else:
                x = int(x)
                print("Your attack did " + str(x) + " damage!")

        # If the player is a witch, the enemy doesn't have a status, and the attack hit, they enewm ymay get poisoned
        if enemystatus == "" and miss == 1:
            if playerclass == 3:
                enemystatus = "strong poison"
                print("The enemy was badly poisoned.")
        
        # If the player is a wizard and the attack hit, there's a chance they enemy may be shocked
        if playerclass == 5 and miss != 1:
            shock = random.randint(1, 20)
            if shock != 20:
                enemystatus = "shock"
                print("The enemy is shocked.")

        # If the player is a golem and the attack hit, a rock is placed on the field
        if playerclass == 4 and miss != 1:
            big_rocks += 1
            print("A big rock was placed on the field.")

        # If the  player is a vampire and the attack hit, the player gains some health
        if playerclass == 6 and miss != 1:
            health_gained = int(x/2)
            playerhealth = playerhealth + health_gained
            if playerhealth > 200:
                playerhealth = 200
                print("You got to full health!")
            else:
                print("You gained " + str(health_gained) + " health!")

        enemy_health = enemy_health - x
        return [enemy_health, enemystatus, big_rocks, playerhealth]

# This move just recovered some health for the player
def recover(playerhealth, max_health):
    x = random.randint(40, 60)
    playerhealth = playerhealth + x
    if playerhealth >= max_health:
        playerhealth = max_health
        print("You got to full health!")
    else:
        print("You recovered " + str(x) + " health!")
    return playerhealth

keep_going = True
turns = 0
speedtie = 0
# This is where the main gameplay part is
while keep_going:
    # Here based off of speed and the turn that it is, the plyaer and enemy stats are set based off of the stats for player 1 and 2
    if turns%2 == 0:
        if p1stats[8] > p2stats[8]:
            playerstats = p1stats
            enemystats = p2stats
            print("Player 1, you have " + str(p1stats[5]) + " health left.")
        elif p2stats[8]> p1stats[8]:
            playerstats = p2stats
            enemystats = p1stats
            print("Player 2, you have " + str(p2stats[5]) + " health left.")
        else:
            # If no one is faster, then it is picked randomly who goes first
            speedtie = random.randint(1, 2)
            if speedtie == 1:
                playerstats = p1stats
                enemystats = p2stats
                print("Player 1, you have " + str(p1stats[5]) + " health left.")
            else:
                playerstats = p2stats
                enemystats = p1stats
                print("Player 2, you have " + str(p2stats[5]) + " health left.")
    else:
        if p1stats[8] > p2stats[8]:
            playerstats = p2stats
            enemystats = p1stats
            print("Player 2, you have " + str(p2stats[5]) + " health left.")
        elif p2stats[8]> p1stats[8]:
            playerstats = p1stats
            enemystats = p2stats
            print("Player 1, you have " + str(p1stats[5]) + " health left.")
        else: 
            if speedtie == 1:
                playerstats = p2stats
                enemystats = p1stats
                print("Player 2, you have " + str(p2stats[5]) + " health left.")
            else:
                playerstats = p1stats
                enemystats = p2stats
                print("Player 1, you have " + str(p1stats[5]) + " health left.")

    # Shock prevents the player from moving
    if playerstats[1] == "shock":
        print("You are shocked. Skip turn.")
        status = ""
    else:
        # The move the plhyaer will use is determined here. If they select an invalid number, then they'll br propted to give a move again
        invalid_choice = True
        while invalid_choice:
            move = int(input("Do you want to use your basic attack(1), your strong attack(2), or recover(3)?"))
            if move == 1 or move == 2 or move == 3:
                invalid_choice = False
            else:
                invalid_choice = True
                print("That isn't a move.")

        if move == 1:
            # Basic attack 
            if playerstats[2][0] > 0:
                results = attack(enemystats[5], playerstats[6], enemystats[7], playerstats[0], enemystats[1], playerstats[3], playerstats[4], playerstats[5], move)
                enemystats[1] = results[1]
                playerstats[3] = results[2]
                playerstats[5] = results[3]
                enemystats[5] = results[0]
                playerstats[2][0] -= 1
                print("You can use this move " + str(playerstats[2][0]) + " more times.")
            else:
                # Moves can only be used a certain amount of. Turns are skipped if the player can't use that move anymore
                print("You can't use that move anymore. Skip.")
                continue

        elif move == 2:
            # Strong attack
            if playerstats[2][1] > 0:
                results = attack(enemystats[5], playerstats[6], enemystats[7], playerstats[0], enemystats[1], playerstats[3], playerstats[4], playerstats[5], move)
                enemystats[1] = results[1]
                playerstats[3] = results[2]
                playerstats[5] = results[3]
                enemystats[5] = results[0]
                playerstats[2][1] -= 1
                print("You can use this move " + str(playerstats[2][1]) + " more times.")
            else:
                print("You can't use that move anymore. Skip.")
                continue

        elif move == 3:
            # Recover
            if playerstats[2][2] > 0:
                playerstats[5] = recover(playerstats[5], playerstats[9])
                playerstats[2][2] -= 1
                print("You can use this move " + str(playerstats[2][2]) + " more times.")
            else:
                print("You can't use that move anymore. Skip.")
                continue
    
    # If the enemy doesn't have any health left, game is over
    if enemystats[5] > 0:
        keep_going = True
    else:
        if playerstats[10] == 1:
            print("Player 2 has no more health left. Player 1 wins!")
            break
        else:
            print("Player 1 has no more health left. Player 2 wins!")
            break

    # Poison does damage based off the player max health. Strong poison does more than mild poison
    if enemystats[1] == "mild poison":
        x = ((enemystats[9]/100) * 15)
        x = int(x)
        if x == 0:
            x = 1
        print("Poison did " + str(x) + " damage!")
        enemystats[5] = enemystats[5] - x
        enemystats[5] = int(enemystats[5])
    elif enemystats[1] == "strong poison":
        x = ((enemystats[9]/100) * 25)
        x = int(x)
        if x == 0:
            x = 1
        print("Poison did " + str(x) + " damage!")
        enemystats[5] = enemystats[5] - x
        enemystats[5] = int(enemystats[5])
    # Burn does damage based off the enemy's current health
    elif enemystats[1] == "burn":
        x = ((enemystats[5]/100) * 35)
        x = int(x)
        if x == 0:
            x = 1
        print("Burn did " + str(x) + " damage!")
        enemystats[5] = enemystats[5] - x
        enemystats[5] = int(enemystats[5])

    # Rocks set up by golems will damage the opponent each time the player makes a move.
    if playerstats[0] == 4:
        if playerstats[3] + playerstats[4] > 0:
            x = (((enemystats[9]/100) * 5) * playerstats[3]) + (((enemystats[9]/100) * 10) * playerstats[4])
            x = int(x)
            if x == 0:
                x = 1
            print("The rocks on the field did " + str(x) + " damage!")
            enemystats[5] = enemystats[5] - x
            enemystats[5] = int(enemystats[5])
    
    # Again, we check the enemy's health after damage is done from status conditions
    if enemystats[5] > 0:
        keep_going = True
    else:
        if playerstats[10] == 1:
            print("Player 2 has no more health left. Player 1 wins!")
            break
        else:
            print("Player 1 has no more health left. Player 2 wins!")
            break
    
    # If the player is a preist, their attack, defense, or speed will be boosted
    if playerstats[0] == 7:
        boost = random.randint(1,3)
        if boost == 1:
            playerstats[6] = playerstats[6] + 0.25
            print("Your attack increased!")
        if boost == 2:
            playerstats[7] = playerstats[7] + 0.25
            print("Your defense increased!")
        if boost == 3:
            playerstats[8] = playerstats[8] + 0.25
            print("Your speed increased!")

    # At the end of the turn, player 1 and player 2 have their stats updated
    if playerstats[10] == 1:
        p1stats = playerstats
        p2stats = enemystats
    else:
        p2stats = playerstats
        p1stats = enemystats

    # The amount of turns is increased
    turns += 1