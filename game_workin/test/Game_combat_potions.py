"""
this file will hold the combat system and potion consumption logic for the game.
"""
import random
import msvcrt
import Game_data_1

#ranged system for the bow and maybe add a arrow thing 
def ranged_system():
    if Game_data_1.weapon_dmg[1][0] == "bow":
        print("You take three steps back and and reach your hand back for an arrow.".center(70))
        print("=" * 70)
        if Game_data_1.player_inv[3][1] <= 0:
            print("Oh no! You have no arrows left!".center(70))
            print("=" * 70)
            return False
        else:
            print("You pull back the string and let the arrow fly!".center(70))
            print("=" * 70)
            Game_data_1.player_inv[3][1] -= 1
            return True


#this is the burn damage system for the fireball weapon
def fireball_burn(enemy_index):
        burn_damage = Game_data_1.weapon_dmg[2][4]
        burn_turns = Game_data_1.weapon_dmg[2][5]
        print(f"The {Game_data_1.enemies[enemy_index][0]} is burning for {burn_damage} damage for {burn_turns} turns.".center(70))
        print("=" * 70)
        for turn in range(burn_turns):
            Game_data_1.enemies[enemy_index][1] -= burn_damage
            if Game_data_1.enemies[enemy_index][1] <= 0:
                Game_data_1.enemies[enemy_index][1] = 0
                break


#this is just a message to prompt the player to pick an enemy
def enemy_msg():
        print("=" * 70)
        print("Pick an enemy you wish to attack!".center(70))
        print("=" * 70)

#to print the currant stats of the enemies
def enemy_to_attack():
    for line in range(6):
        for i, e in enumerate(Game_data_1.enemies, 1):
            info = [
                f"{i}. {e[0]}",
                f"   Has   {e[1]} Health",
                f"   Drops {e[3]} gold",
                f"   Does  {e[2]} damage",
                f"   Gives {e[4]} score",
                f"   Drops {e[5]} potions"
            ]
            print(f"{info[line]:<23}", end="")
        print()
    print("=" * 70)

#this is the weapon picking system
def weapon_to_use():
    if Game_data_1.player_inv[2][1] > 0 or Game_data_1.player_inv[4][1] > 0:
        available_weapons = []

        #this fuckery makes it so only weapons that the player actually has in their inventory are available for use
        for weapon_index, weapon in enumerate(Game_data_1.weapon_dmg):
            for item in Game_data_1.player_inv:
                if (item[0].lower() == weapon[0].lower() and item[1] > 0
                        and (weapon[0].lower() != "bow" or Game_data_1.player_inv[3][1] > 0)):
                    available_weapons.append((weapon_index, weapon))
                    break
        print("=" * 70)
        print("Pick a weapon you wish to use!".center(70))
        print("=" * 70)
        for i, w in enumerate(available_weapons, 1):
            print(f"{i}. {w[1][0]:<10} - Damage: {w[1][2]}. Crit: {w[1][3]}".center(70))
        print("=" * 70)
        while True:
            print(" Enter 1, 2, or 3: ".center(70))
            print("=" * 70)
            weapon_choice = msvcrt.getwch()
            if weapon_choice in [str(i) for i in range(1, len(available_weapons) + 1)]:
                print(f"You chose: {available_weapons[int(weapon_choice) - 1][1][0]}".center(70))
                break
            else:
                print(f"Please choose a number between 1 and {len(available_weapons)}: ".center(70))
        return available_weapons[int(weapon_choice) - 1][0]
    else:
        weapon_choice = 0
        return weapon_choice

#this allows you to pick what enemy you would wish to fight
def choose_enemy_to_attack(death0, death1, death2, enemies):
    while True:
        enemy_to_attack()
        print(" Enter 1, 2, or 3: ".center(70))
        enemy_attack = msvcrt.getwch()

        if enemy_attack == "1":
            if death0 == 0:
                print(f"you chose: {enemies[0][0]}".center(70))
                print("=" * 70)
                break
            else:
                print("This enemy is already dead!".center(70))
                print("=" * 70)

        elif enemy_attack == "2":
            if death1 == 0:
                print(f"you chose: {enemies[1][0]}".center(70))
                print("=" * 70)
                break
            else:
                print("This enemy is already dead!".center(70))
                print("=" * 70)
        elif enemy_attack == "3":
            if death2 == 0:
                print(f"you chose: {enemies[2][0]}".center(70))
                break
            else:
                print("This enemy is already dead!".center(70))
                print("=" * 70)
        else:
            print("=" * 70)
            print()
            print("Please choose 1, 2, or 3: ".center(70))
            print()
            enemy_msg()
    return enemy_attack

#this is the combat system, handling player attacks, enemy attacks, and loot distribution
def the_combat_system(enemy_attack, death0, death1, death2, weapon_choice):
    enemy_attack = int(enemy_attack)
    enemy_index = enemy_attack - 1
    players = Game_data_1.players
    enemies = Game_data_1.enemies

    # 50% chance to hit the enemy
    if random.randint(1, 2) == 1:
        if random.randint(1, 5) == 1:
            if Game_data_1.weapon_dmg[weapon_choice][0] == "bow":
                if not ranged_system():
                    return death0, death1, death2
                
            if Game_data_1.weapon_dmg[weapon_choice][0] == "fireball":
                print("=" * 70)
                print("fire starts building up in the palm of your hand!".center(70))
                print("you throw the fireball at the enemy!".center(70))
                print("=" * 70)
            elif Game_data_1.weapon_dmg[weapon_choice][0] == "sword":
                print("=" * 70)
                print("You draw your sword and prepare to strike!".center(70))
                print("You swing your sword with all your might!".center(70))
                print("=" * 70)
                
            print("Critical hit!".center(70))
            print(f"You hit the enemy! for {Game_data_1.weapon_dmg[weapon_choice][3]} Damage.".center(70))
            print("=" * 70)
            
            # Player damage
            enemies[enemy_index][1] -= Game_data_1.weapon_dmg[weapon_choice][3]

            #if fieball then burn damage is applied
            if Game_data_1.weapon_dmg[weapon_choice][0] == "fireball":
                fireball_burn(enemy_index)
        else:
            if Game_data_1.weapon_dmg[weapon_choice][0] == "bow":
                if not ranged_system():
                    return death0, death1, death2
                
            if Game_data_1.weapon_dmg[weapon_choice][0] == "fireball":
                print("=" * 70)
                print("fire starts building up in the palm of your hand!".center(70))
                print("you throw the fireball at the enemy!".center(70))
                print("=" * 70)
            elif Game_data_1.weapon_dmg[weapon_choice][0] == "sword":
                print("=" * 70)
                print("You draw your sword and prepare to strike!".center(70))
                print("You swing your sword with all your might!".center(70))
                print("=" * 70)

            print(f"You hit the enemy! for {Game_data_1.weapon_dmg[weapon_choice][2]} Damage.".center(70))
            print("=" * 70)

            # Player damage
            enemies[enemy_index][1] -= Game_data_1.weapon_dmg[weapon_choice][2]

            #if fieball then burn damage is applied
            if Game_data_1.weapon_dmg[weapon_choice][0] == "fireball":
                fireball_burn(enemy_index)

        # Check if the enemy has died
        if enemies[enemy_index][1] <= 0:
            enemies[enemy_index][1] = 0

            print(f"{enemies\
                     
                     [enemy_index][0]} has died!!!".center(70))
            print("=" * 70)

            # sweet loot
            players[0][3] += enemies[enemy_index][3]
            players[0][4] += enemies[enemy_index][4]
            Game_data_1.player_inv[5][1] += enemies[enemy_index][5]

            # death flags
            if enemy_attack == 1:
                death0 = 1
            elif enemy_attack == 2:
                death1 = 1
            elif enemy_attack == 3:
                death2 = 1

    else:
        #also adds a 50% chance of blocking thr emenies attack
        # Enemy damage
        if Game_data_1.weapon_dmg[weapon_choice][0] == "bow":
            print("=" * 70)
            print("You take three steps back and and reach your hand back for an arrow.".center(70))
            print("You pull back the string and let the arrow fly!".center(70))
            print("=" * 70)
        elif Game_data_1.weapon_dmg[weapon_choice][0] == "fireball":
            print("=" * 70)
            print("fire starts building up in the palm of your hand!".center(70))
            print("you throw the fireball at the enemy!".center(70))
            print("=" * 70)
        elif Game_data_1.weapon_dmg[weapon_choice][0] == "sword":
            print("=" * 70)
            print("You draw your sword and prepare to strike!".center(70))
            print("You swing your sword with all your might!".center(70))
            print("=" * 70)

        if random.randint(1, 5) == 1 and Game_data_1.player_inv[1][1] > 0:
            print("You missed! No damage dealt.".center(70))
            print("You have blocked the enemies attack! using your shield.".center(70))
            print("=" * 70)
            print(f"{'Name':<12}{'Health':<10}{'Damage':<10}{'Gold':<10}{'Score':<10}{'Potions':<10}")
        else:
            players[0][1] -= enemies[enemy_index][2]
            print("You missed! No damage dealt.".center(70))
            print(f"The {enemies[enemy_index][0]} has hit you for {enemies[enemy_index][2]} damage.".center(70))
            print("=" * 70)
            print(f"{'Name':<12}{'Health':<10}{'Damage':<10}{'Gold':<10}{'Score':<10}{'Potions':<10}")

        for player in players:
            print(f"{player[0]:<12}{player[1]:<10}{player[2]:<10}{player[3]:<10}{player[4]:<10}{player[5]:<10}")
        print("=" * 70)

    return death0, death1, death2

# this is how much potions will heal
health_potions = 5

#potions consumption during combat
def consume_health_potion():
    print(f"do you wish to consume a health potion, "
          f"healing {health_potions} HP. Y/N: ".center(70))
    potions = msvcrt.getwch().lower()
    while True:
        if potions in ("y", "n"):
            break
        print("=" * 70)
        print("Please choose Y/N".center(70))
        print(f"do you wish to consume a health potion, "
              f"healing {health_potions} HP. Y/N: ".center(70))
        potions = msvcrt.getwch().lower()
        print("=" * 70)
    if potions == "y":
        Game_data_1.players[0][1] = min(25, Game_data_1.players[0][1] + health_potions)
        Game_data_1.player_inv[5][1] -= 1
        print(f"{'Name':<12}{'Health':<10}{'Damage':<10}{'Gold':<10}{'Score':<10}{'Potions':<10}")
        for player in Game_data_1.players:
            print(f"{player[0]:<12}{player[1]:<10}{player[2]:<10}{player[3]:<10}{player[4]:<10}{player[5]:<10}")
        print("=" * 70)