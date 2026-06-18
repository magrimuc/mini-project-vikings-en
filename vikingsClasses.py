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
        # your code here
        pass
    
    def saxonAttack(self):
        # your code here
        pass

    def showStatus(self):
        # your code here
        pass
    

####
# vikingAttack() method
#A Saxon (chosen at random) has their receiveDamage() method called with the damage equal to the strength of a Viking (also chosen at random). This should only perform a single attack and the Saxon doesn't get to attack back.

#    should be a function
#    should receive 0 arguments
#    should make a Saxon receiveDamage() equal to the strength of a Viking
#    should remove dead saxons from the army
#    should return result of calling receiveDamage() of a Saxon with the strength of a Viking

#saxonAttack() method

#The Saxon version of vikingAttack(). A Viking receives the damage equal to the strength of a Saxon.

#    should be a function
#    should receive 0 arguments
#    should make a Viking receiveDamage() equal to the strength of a Saxon
#    should remove dead vikings from the army
#    should return result of calling receiveDamage() of a Viking with the strength of a Saxon

#showStatus() method

#Returns the current status of the War based on the size of the armies.

 #   should be a function
  #  should receive 0 arguments
   # if the Saxon array is empty, should return "Vikings have won the war of the century!"
#    if the Viking array is empty, should return "Saxons have fought for their lives and survive another day..."
#    if there are at least 1 Viking and 1 Saxon, should return "Vikings and Saxons are still in the thick of battle."
#############


