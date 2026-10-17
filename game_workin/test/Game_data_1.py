import copy

#this is the players and their stats
#0 is the player name, 1 is the health, 2 is the dmg
#3 is the gold, 4 is the score, and 5 is the potions
players = [
     ["", 25, 25, 100, 0, 3]
# if you wish to update the amount of potions,
# update it IN player_inv, this is just a place holder
 ]

#this is the player's inventory health potions currently copy to players this is me being lazy
#(change the amounts)
#0 is the name, 1 is the quantity, 2 is the heal amount ( just for health potions)
player_inv = [ 
     ["sword", 1],
     ["shield", 0], 
     ["bow", 0],
     ["arrow", 4], 
     ["fireball", 0],
     ["health pot", 3,], 
 ]

#this is the list of weapons and their damage stats
#0 is the name, 
#1 is the quantity (truthfuly i have no idea why i added this, its not used),
#2 is the dmg, 3 is crit dmg, 4 is the burn dmg, 5 is the burn turns
weapon_dmg = [
    ["sword", 1, 25, 35],
    ["bow", 0, 25, 35],
    ["fireball", 0, 15, 20, 5, 3]
]

#enemies stats
#0 is the enemies names, 1 is the health, 2 is the dmg
#3 is the gold, 4 is the score, and 5 is the potions
enemies = [
     ["Orc", 100, 10, 100, 100, 2],
      ["Goblin", 50, 5, 50, 50, 1],
      ["Wolf", 25, 7, 10, 25, 0]
 ]

#this is the enemies inventory, currantly unused not super sure how to implement it but i may add it later
# (change amounts)
#0 is the name, 1 is the quantity
enemy_inv = [ 
         ["sword", 10],
         ["shield", 10],
         ["bow", 10],
         ["arrow", 10],
         ["fireball", 10],
     ]

#these are the items in the shop (change the amounts and prices)
#0 is the name, 1 is the quantity, 2 is the price
shop = [
    ["sword", 10, 100],
    ["shield", 10, 70],
    ["bow", 10, 80],
    ["arrow", 20, 20],
    ["fireball", 10, 100],
    ["Health Pot", 10, 50]
]

#this is to reset the game when you play again, it copies the original data and resets it
_starting_players = copy.deepcopy(players)
_starting_inventory = copy.deepcopy(player_inv)
_starting_enemies = copy.deepcopy(enemies)
_starting_shop = copy.deepcopy(shop)

def reset_game():
    players[:] = copy.deepcopy(_starting_players)
    player_inv[:] = copy.deepcopy(_starting_inventory)
    enemies[:] = copy.deepcopy(_starting_enemies)
    shop[:] = copy.deepcopy(_starting_shop)