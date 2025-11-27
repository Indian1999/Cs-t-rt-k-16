import random

class Mage:
    def __init__(self, name, maxHealth = 30, maxMana = 90, armor = 5, intellect = 10, level = 1):
        self.maxHealth = maxHealth
        self.name = name
        self.health = self.maxHealth
        self.maxMana = maxMana
        self.mana = self.maxMana
        self.armor = armor
        self.intellect = intellect
        self.level = level
        self.baseDamage = round(self.level * 0.5 + self.intellect * 0.1)

    def __str__(self):
        return f"Name: {self.name} (Mage)\n\tHealth: {self.health}/{self.maxHealth}\n\tMana: {self.mana}/{self.maxMana}\n\tArmor: {self.armor}\n\tLevel: {self.level}\n\tIntellect: {self.intellect}\n\tBase damage: {self.baseDamage}"
    
    def take_damage(self, amount):
        damage = max(amount - self.armor, 0)
        self.health = max(self.health - damage, 0)

    def fireball(self):
        if self.mana >= 10:
            self.mana -= 10
            return round(2.5 * self.baseDamage)
        else:
            return None
    
    def basicAttack(self):
        return self.baseDamage
    
    def firestorm(self):
        if self.mana >= 15:
            self.mana -= 15
            self.take_damage(round(self.baseDamage * 0.7))
            return round(5.6 * self.baseDamage)
        else:
            return None
        
    def restoreMana(self):
        self.mana = min(round(self.mana + self.maxMana * 0.05), self.maxMana)
        print(f"{self.name} restores {round(self.maxMana * 0.05)} mana points.")
    
gandalf = Mage("Gandalf", 295, 34, 1, 150, 13)
khadgar = Mage("Khadgar", 526, 51, 7, 55, 4)
print(gandalf)
print(khadgar)

def x_attack_y(x, y, player_turn = False):
    damage = None
    while damage == None:
        if not player_turn:
            randomAttack = random.randint(1, 3)
        else:
            print(f"Your mana: {x.mana}/{x.maxMana}")
            randomAttack = int(input("Adj meg egy képességet! (1: basicAttack (0), 2: fireball (10), 3: firestorm (15))"))
        if randomAttack == 1:
            damage = x.basicAttack()
        elif randomAttack == 2:
            damage = x.fireball()
        elif randomAttack == 3:
            damage = x.firestorm()
    print(f"{y.name} health: {y.health}/{y.maxHealth}")
    if randomAttack == 1:
        print(f"{x.name} is using a basic attack for {damage} damage")        
    elif randomAttack == 2:
        print(f"{x.name} is using a fireball for {damage} damage")   
    elif randomAttack == 3:
        print(f"{x.name} is using a firestorm for {damage} damage")   
    y.take_damage(damage)
    print(f"{y.name} health: {y.health}/{y.maxHealth}")

def on_end_of_turn():
    gandalf.restoreMana()
    khadgar.restoreMana()
    print(f"{gandalf.name} health: {gandalf.health}/{gandalf.maxHealth}")
    print(f"{gandalf.name} mana: {gandalf.mana}/{gandalf.maxMana}")
    print(f"{khadgar.name} health: {khadgar.health}/{khadgar.maxHealth}")
    print(f"{khadgar.name} mana: {khadgar.mana}/{khadgar.maxMana}")

while gandalf.health > 0 and khadgar.health > 0:
    x_attack_y(gandalf, khadgar)
    x_attack_y(khadgar, gandalf, True)
    on_end_of_turn()

if gandalf.health <= 0:
    print("Khadgar nyert!")
else:
    print("Gandalf nyert!")



