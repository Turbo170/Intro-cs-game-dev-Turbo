import random
import time #using this to make the code take a pause in between turns

#this is the health of both player and enemy
PlayerHealth = 100
EnemyHealth = 100

#Attacks variable that is the list of attacks
move = ["Throw a punch", "throw a right hook", "feint into a kick"]

print("Welcome challenger...")
time.sleep(2)
print("This is where the fight begins")
time.sleep(2)

#This is the players turn and where the loop starts
while PlayerHealth > 0 and EnemyHealth > 0:
    input("\nPress Enter to attack")

    #the attack damage would be random from 1-32 and then subtracted from the enemys health.
    AttackDamage = random.randint(1, 32)
    EnemyHealth -= AttackDamage

    #made it so it randomly chooses one of the attacks in the list but its not really doing it randomly idk why
    Attack = random.choice(move) 
    print(f"\nYou {Attack} and has done {AttackDamage} damage to the opponent.")
    time.sleep(2)
    
    print(f"\nYour Health: {PlayerHealth} | Opponent's Health: {EnemyHealth}")

    #if statement to win
    if EnemyHealth <= 0:
        print("You have defeated your opponent.\nYOU WIN!")
        break
    time.sleep(2)
    
    #This is the enemy's turn
    print("\nThe opponent is preparing to attack...")
    time.sleep(4)

    #the attack damage would be random from 1-32 and then subtracted from the enemys health.
    EnemyAttackDamage = random.randint(1, 32)
    PlayerHealth -= EnemyAttackDamage
    print(f"\nThe opponent {Attack} and has done {EnemyAttackDamage} damage to you.")
    time.sleep(2)

    print(f"\nYour Health: {PlayerHealth} | Opponent's Health: {EnemyHealth}")

    if PlayerHealth <= 0:
        print("You have been defeated by your opponent.\nYOU LOSE!")
        break
#this is just the end of the loop, uses the same code twice, one for the player and one for the enemy
#the Damage is actually random even though i would like for it have a set damage for each attack but have a critical hit chance