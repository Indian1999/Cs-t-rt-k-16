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
        return round(2.5 * self.baseDamage)
    
    def basicAttack(self):
        return self.baseDamage
    
    def firestorm(self):
        self.take_damage(round(self.baseDamage * 0.7))
        return round(5.6 * self.baseDamage)
    
gandalf = Mage("Gandalf", 245, 1, 150, 13)
khadgar = Mage("Khadgar", 526, 7, 55, 4)
print(gandalf)
print(khadgar)

while gandalf.health > 0 and khadgar.health > 0:
    print(f"Khadgar HP: {khadgar.health}/{khadgar.maxHealth}")
    khadgar.take_damage(gandalf.baseDamage)
    print(f"Khadgar HP: {khadgar.health}/{khadgar.maxHealth}")

    
    print(f"Gandalf HP: {gandalf.health}/{gandalf.maxHealth}")
    gandalf.take_damage(khadgar.baseDamage)
    print(f"Gandalf HP: {gandalf.health}/{gandalf.maxHealth}")

