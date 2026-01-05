import time

print("------------------------------\nYour Inventory:\n")
Inventory = {
    "Blue Sea Weed:": 10,
    "Star Coral:": 4,
    "Onyx Jem:": 1
}
for keys, values in Inventory.items():
    print(keys,values)

input("\nPress enter to make a potion!")
time.sleep(1)

print("You start brewing a special concoction.\n\nCrafting...\n")
time.sleep(3)

Inventory.update({"Blue Sea Weed:" : 5})
Inventory.update({"Star Coral:" : 2})
Inventory.update({"Powerful WaterBreathing Potion:" : 1})

print("------------------------------\nYour Inventory:\n")

for keys, values in Inventory.items():
    print(keys,values)
time.sleep(2)

print("\nYou created a WaterBreathing Potion!\n Used:")
time.sleep(3)
print("\n 5 blue Sea Weed\n 2 Star coral.")