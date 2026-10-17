import msvcrt
import Game_data_1

#this is the buying system
def buy_item(shop_index): 
    if Game_data_1.players[0][3] <= 0:
        print("You have no gold to spend!".center(70))
        print("=" * 70)
        return
    elif Game_data_1.players[0][3] > 0:
        Game_data_1.shop[shop_index][1] -= 1
        Game_data_1.player_inv[shop_index][1] += 1
        Game_data_1.players[0][3] -= Game_data_1.shop[shop_index][2]
        Game_data_1.players[0][5] = Game_data_1.player_inv[5][1]
        print(f"Do you wish to purchase other items? Y/N: ".center(70))
        other_purchase = msvcrt.getwch().lower()
        while True:
            if other_purchase in ["y", "n"]:
                break
            else:
                print("=" * 70)
                print("Please choose a valid option (Y/N)".center(70))
                other_purchase = msvcrt.getwch().lower()
                print("=" * 70)
        if other_purchase == "y":
            the_shop()
        else:
            print("=" * 70)
            print("Thank you for your purchase!".center(70))
            print("=" * 70)

#this is the shop system

# i know i could made the start shorter but this works just find but its a tiny bit longer
def the_shop():
    if Game_data_1.players[0][3] <= 0:
        print("You have no gold to spend!".center(70))
        print("=" * 70)
        return
    elif Game_data_1.players[0][3] > 0:
        print("=" * 70)
        print("Welcome to the shop! what do you wish to buy?".center(70))
        print(f"You currently have {Game_data_1.players[0][3]} gold.".center(70))
        print("=" * 70)

        print(f"= {'1':>2}. {Game_data_1.shop[0][0]:<12} there is {Game_data_1.shop[0][1]:>2} in stock. Price: {Game_data_1.shop[0][2]:>3}  =".center(70))
        print(f"= {'2':>2}. {Game_data_1.shop[1][0]:<12} there is {Game_data_1.shop[1][1]:>2} in stock. Price: {Game_data_1.shop[1][2]:>3}  =".center(70))
        print(f"= {'3':>2}. {Game_data_1.shop[2][0]:<12} there is {Game_data_1.shop[2][1]:>2} in stock. Price: {Game_data_1.shop[2][2]:>3}  =".center(70))
        print(f"= {'4':>2}. {Game_data_1.shop[3][0]:<12} there is {Game_data_1.shop[3][1]:>2} in stock. Price: {Game_data_1.shop[3][2]:>3}  =".center(70))
        print(f"= {'5':>2}. {Game_data_1.shop[4][0]:<12} there is {Game_data_1.shop[4][1]:>2} in stock. Price: {Game_data_1.shop[4][2]:>3}  =".center(70))
        print(f"= {'6':>2}. {Game_data_1.shop[5][0]:<12} there is {Game_data_1.shop[5][1]:>2} in stock. Price: {Game_data_1.shop[5][2]:>3}  =".center(70))
        print("=" * 70)
        shop_purchase = msvcrt.getwch().lower()
        while True:
            if shop_purchase in ["1", "2", "3", "4", "5", "6"]:
                break
            else:
                print("=" * 70)
                print("Please choose a valid option (1-6)".center(70))
                shop_purchase = msvcrt.getwch().lower()
                print("=" * 70)

        shop_index = int(shop_purchase) - 1
        if Game_data_1.players[0][3] < Game_data_1.shop[shop_index][2]:
            print("You do not have enough gold to purchase this item.".center(70))
            print(f"You have {Game_data_1.players[0][3]} gold and this item costs {Game_data_1.shop[shop_index][2]} gold.".center(70))
            print("=" * 70)
            the_shop()
            return
        else:
            print("=" * 70)
            print(f"You have chosen to purchase {Game_data_1.shop[shop_index][0]}".center(70))
            print("=" * 70)
            if Game_data_1.shop[shop_index][1] <= 0:
                print("Sorry, this item is out of stock.".center(70))
                the_shop()
                return  

        if shop_purchase == "1":
            buy_item(shop_index)
        elif shop_purchase == "2":
            buy_item(shop_index)
        elif shop_purchase == "3":
            buy_item(shop_index)
        elif shop_purchase == "4":
            buy_item(shop_index)
        elif shop_purchase == "5":
            buy_item(shop_index)
        elif shop_purchase == "6":
            buy_item(shop_index)    