import time #used for time sleep in between prints

#print explaining its your inventory
print("------------------------------\nYour Inventory:\n")
Inventory = {
    "Blue Sea Weed:": 10,
    "Star Coral:": 4,
    "Onyx Jem:": 1
}
#printing keys and values "showing" the inventory above^
for keys, values in Inventory.items():
    print(keys,values)

#User presses enter to continue the code then it waits a bit using time sleep
input("\nPress enter to make a potion!")
time.sleep(1)

print("You start brewing a special concoction.\n\nCrafting...\n")
time.sleep(3)

"""The inventory begins to update and removes 5 blue sea weed and 2
star coral while adding a WaterBreathing potion"""
Inventory.update({"Blue Sea Weed:" : 5})
Inventory.update({"Star Coral:" : 2})
Inventory.update({"Powerful WaterBreathing Potion:" : 1})

print("------------------------------\nYour Inventory:\n")

#printing keys and values "showing" the NEW inventory
for keys, values in Inventory.items():
    print(keys,values)
time.sleep(2)

print("\nYou created a WaterBreathing Potion!\n Used:")
time.sleep(3)
print("\n 5 blue Sea Weed\n 2 Star coral.")