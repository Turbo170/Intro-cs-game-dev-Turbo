#class holding data for enemy and using functions as well.
class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        
    def attack_player(self, player):
        player.take_damage(self.attack)
    
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0