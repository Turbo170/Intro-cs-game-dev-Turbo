#Player enters name, which becomes the new variable for "name"
print ("Enter Name")
name = input()

#prints sentence with name variable using f string
print(f"Welcome {name}, to the one punch man game.")

#new variable called option equals to an intger which is also an input for the player to respond
option = int(input("You are walking and encounter a monster,\ndo you:\n1 Stand your ground and fight\n2 Walk past the enemy\n"))

#if used here so the player can choose "between" the new options. if anything else other then 1 is chosen, you get 2.
if (option) == 1.:
    print(f"You throw a punch, instantly killing it.\nYou Win!")
elif option == 2.:
    print(f"You leave the monster confused and they continue with their rampage.\n You Lose.")