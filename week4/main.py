#importing data from other files to use here
from enemy import Enemy
from player import Player
import time

player = Player("The Warrior", 80, 10)

MiniBoss = Enemy("The Miniboss", 50, 10)
MainBoss = Enemy("The MainBoss", 150, 25)

Bosses = [MiniBoss, MainBoss]

print ("The Hunt has begun...")
time.sleep(1)
print ("...")
time.sleep(1)
print ("...")
time.sleep(1)

#for loop to keep the fight going until one wins/loses
for enemy in Bosses:
    print(f"You have found {enemy.name} and they approach you.")

    time.sleep(1)
    
    #while loop to check if player or enemy is alive
    while enemy.is_alive() and player.is_alive():
        player.attack_enemy(enemy)
        print(f"{player.name} has attacked {enemy.name} for {enemy.hp} HP!")

        time.sleep(2)

        print(f"\nYour Health: {player.hp} | Opponent's Health: {enemy.hp}")

        time.sleep(2)

        if enemy.is_alive():
            enemy.attack_player(player)
            print(f"\n{enemy.name} has attacked {player.name} for {player.hp} HP!")

            time.sleep(2)

            print(f"\nYour Health: {player.hp} | Opponent's Health: {enemy.hp}")

        print()

    #if statement to check if anyone died to give win condition.
    if not player.is_alive():
        print(f"{player.name} has lost the battle, you lose.")
        break
    else:
        print(f"{enemy.name} has been slain by {player.name}")

if player.is_alive():
    print(f"{player.name} has defeated all Bosses, congratulations, you actually won.")