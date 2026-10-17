""""
 you can now just use hotkey instead of typing
 other minor issues have been fixed

 there is now a way to view your inventory and shop
 you can select what weapon you wish to use in combat (each has its own dmg stats and msg)
 you can block attacks with a shield (if you have one in your inventory)
 the fire ball now has a burn effect that does damage over time
(needs a small fix it does the 5dmg for 3 turns but it does it all at once instead of over 3 turns)

also need to add a USE for score 
"""
import sys
import msvcrt
import Game_combat_potions
from Game_data_1 import players, player_inv, enemies, enemy_inv, shop, reset_game
import Game_inv
import Game_shop_1

#this is to restart
def restart():
    print ("Do you wish to play again? Y/N: ".center(70))
    game1 = msvcrt.getwch().lower()
    if game1 == "y":
        #this just makes it so the game resets when you play again
        reset_game()
        the_game()
    else:
        sys.exit()

#this is the game it's self
def the_game():

    #select name
    player_name = input("=" * 70 + "\n" + " " * 25 + "What is your name? ")
    print("=" * 70)


    players[0][0] = player_name


    #this is to print the score board
    def scoreboard():
        print(f"{'Name':<12}{'Health':<10}{'Damage':<10}{'Gold':<10}{'Score':<10}{'Potions':<10}")

        for e in enemies:
            print(f"{e[0]:<12}{e[1]:<10}{e[2]:<10}{e[3]:<10}{e[4]:<10}{e[5]:<10}")
        for p in players:
            print(f"{p[0]:<12}{p[1]:<10}{p[2]:<10}{p[3]:<10}{p[4]:<10}{p[5]:<10}")

    scoreboard()

    #death flags for the enemies
    death0 = 0
    death1 = 0
    death2 = 0

    #counter for the battles
    Battle_counter = 0
    
    #this is the message prompting the player to pick an enemy
    Game_combat_potions.enemy_msg()


    #this is the loop that allows you to battle till you die or win
    while players[0][1] > 0 and (death0 == 0 or death1 == 0 or death2 == 0):
        
        #counter for the battles and a header for each battle
        Battle_counter += 1
        print(f"Battle {Battle_counter}".center(70))
        print("=" * 70)

        # This lets you pick the enemy you want to battle
        enemy_attack = Game_combat_potions.choose_enemy_to_attack(
            death0, death1, death2, enemies
        )


        print("=" * 70)

        # This is the combat system
        weapon_choice = Game_combat_potions.weapon_to_use()
        death0, death1, death2 = Game_combat_potions.the_combat_system(
            enemy_attack, death0, death1, death2, weapon_choice
        )


        # This is the death system
        if players[0][1] <= 0:
            print("You have DIED".center(70))
            print("=" * 70)
            players[0][1] = 0
            scoreboard()
            print("=" * 70)

            #this is to play again or not
            restart()

        # This fixes drinking a potion after all enemies are dead
        if death0 == 1 and death1 == 1 and death2 == 1:
            break

        # This is the potions system
        if players[0][1] < 25:
            if player_inv[5][1] <= 0:
                print("You have no potions left!".center(70))
                print("=" * 70)
            else:
                Game_combat_potions.consume_health_potion()

        #this allows you to view your inventory or the shop after each battle (i found it annoying for it to ask for both everytime)
        print("=" * 70)
        print("do you wish to view your inventory or the shop? I/S/N:".center(70))
        inv_shop_choice = msvcrt.getwch().lower()
        print("=" * 70)
        while True:
            if inv_shop_choice == "i":
                Game_inv.view_inventory()
                break
            elif inv_shop_choice == "s":
                Game_shop_1.the_shop()
                break
            elif inv_shop_choice == "n":
                break
            else:
                print("=" * 70)
                print("Please choose a valid option (I/S/N)".center(70))
                print("Do you wish to view your inventory or the shop? I/S/N:".center(70))
                inv_shop_choice = msvcrt.getwch().lower()
                print("=" * 70)

    #this is to wipe the gold, score, and potions of the enemies
    for enemy in enemies:
        enemy[3:6] = [0, 0, 0]

    #win
    print("=" * 70)
    print("Game Over".center(70))
    print("Victory".center(70))
    print("=" * 70)
    print("=" * 70)
    scoreboard()
    print("=" * 70)

#this is to start the game
the_game()

#this is to play again or not
restart()