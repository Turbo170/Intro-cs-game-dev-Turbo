import time
import random

#taking the player and enemy stats from my dictionary in characters file
from characters import Player, Enemy

#funciton so the damage is shown and given a random amount of damage
def deal_damage(attacker, defender):
    damage = random.randint(20,40)
    defender["Health"] -= damage
    print(f"{attacker["Name"]} has done {damage} damage to {defender["Name"]}.")
    time.sleep(2)
    print(f"{defender ["Name"]}'s health is now at {defender["Health"]}.\n")
    time.sleep(1)
#included time.sleep to be dramatic/ make it look like the code is "thinking"

"""this function is used to check if the enemy or player health have hit zero, checking if the
win or loss condition has been met, to then printing a statement clarifying who has won or loss."""
def win_or_lose_condition():
    if Enemy["Health"] <= 0:
        print(f"You have killed {Enemy["Name"]} and Won the battle!")
        return True
    if Player["Health"] <= 0:
        print(f"{Enemy["Name"]} has stuck {Player["Name"]} down, you lost the battle.")
        return True
    return False

print("Goku vs Frieza....\n")
time.sleep(1)
print("Ready?\n")
time.sleep(1)
print("Fight!\n")

#a while loop that ends after checking the win or lose condition and deals the damage of both fighters
while Player["Health"] >= 0 and Enemy["Health"] >= 0:

    input("Press Eneter to throw a punch")
    deal_damage(Player,Enemy)
    if win_or_lose_condition():
            break

    print(f"{Enemy["Name"]}, throws a punch as well!\n")
    time.sleep(2)
    deal_damage(Enemy,Player)
    if win_or_lose_condition():
            break