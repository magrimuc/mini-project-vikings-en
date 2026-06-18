import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        # your code here
    
    def attack(self):
        return self.strength
        

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        pass
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        self.name = name
        self.health = health
        self.strength = strength

    def battleCry(self):
        # your code here
        return("Odin Owns You All!")

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if(self.health > 0):
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if(self.health > 0):
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


        
# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)        
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        n = random.randint(0,len(self.vikingArmy)-1)
        m = random.randint(0,len(self.saxonArmy)-1)
        o = self.saxonArmy[m].receiveDamage(self.vikingArmy[n].strength)
        if(self.saxonArmy[m].health < 1):
            del self.saxonArmy[m]
        return o
    
    def saxonAttack(self):
        n = random.randint(0,len(self.saxonArmy)-1)
        m = random.randint(0,len(self.vikingArmy)-1)
        o = self.vikingArmy[m].receiveDamage(self.saxonArmy[n].strength)
        if(self.vikingArmy[m].health < 1):
            del self.vikingArmy[m]
        return o

    def showStatus(self):
        if(len(self.saxonArmy) == 0):
            return "Vikings have won the war of the century!"
        if(len(self.vikingArmy) == 0 ):
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."