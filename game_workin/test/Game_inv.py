import Game_data_1

#this is the inv prompt (it was a lot longer thats why its in its own file), i may add droping items? if that is needed
def view_inventory():
        print("You opened your inventory and it contains:".center(70))
        print("=" * 70)
        print(f"= {'Weapon'} =            = {'Quantity'} =".center(70))
        print("=" * 70)
        count = 0
        for p in Game_data_1.player_inv:
            count += 1
            print(f"= {count}.  {p[0]:<12} You have {p[1]:<3} left =".center(70))
        print("=" * 70)
   
