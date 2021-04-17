# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random

#Character class and subclasses

class Character:
    def __init__(self,name,health,power,coins):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins


    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def prob(self, percent_chance):
        rand = random.randint(1,10)
        if rand > percent_chance:
            return True
        else:
            return False
    
    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")

    def power_up(self, power_up_by):
        power_level = self.power * power_up_by
        return power_level
        # else:
        #     self.power = self.power * 1
        #     return self.power

    def attack_shadow(self,attacked, power_level):
        if self.prob(9):
            attacked.health -= power_level
            print(f"{self.name} does {power_level} damage to {attacked.name}.")
            if attacked.alive() == False:
                print(f"{attacked.name} is dead.\n")
                self.coins += attacked.coin_bonus
                print(f"the bounty for killing {attacked.name} is\n{attacked.coin_bonus} coins. You have {self.coins} coins!")
        else:
            print(f"{attacked.name} got away.\n")

    def attack_zombie(self, attacked, power_level):
        attacked.health -= power_level 
        print(f"{self.name} does {power_level} damage to {attacked.name}.")
        print(f"but {attacked.name} is not dead.\nneed {self.name} braaaaaiiiins...\n")
    
    def attack_alchemist(self,attacked, power_level):
        attacked.health -= power_level
        print(f"{self.name} does {power_level} damage to {attacked.name}.")
        if self.prob(7) and self.coins > 5:
            self.coins -= 5
            attacked.coins += 5
            print(f"{attacked.name} stole 5 of our coins.\nYour now have {self.coins} coins")
            if attacked.alive() == False:
                print(f"{attacked.name} is dead.\n")
                self.coins += attacked.coins * 2
                print(f"the bounty for killing {attacked.name} is\n{attacked.coins * 2} coins. You have {self.coins} coins!")
        else:
            if attacked.alive() == False:
                print(f"{attacked.name} is dead.\n")
                self.coins += attacked.coins * 2
                print(f"the bounty for killing {attacked.name} is\n{attacked.coins * 2} coins. You have {self.coins} coins!")

    def attack(self, attacked, power_level ):
        if attacked.type == "shadow":
            self.attack_shadow(attacked,power_level)
        elif attacked.type == "zombie":
            self.attack_zombie(attacked,power_level)
        elif attacked.type == "alchemist":
            self.attack_alchemist(attacked, power_level)
        else:
            attacked.health -= power_level 
            print(f"{self.name} does {power_level} damage to {attacked.name}.\n")
            if attacked.alive() == False:
                print(f"{attacked.name} is dead.\n")
                self.coins += attacked.coin_bonus
                print(f"the bounty for killing {attacked.name} is\n{attacked.coin_bonus} coins. You have {self.coins} coins!")

class Hero(Character):
    def __init__(self, name, health = 10, power = 5, coins = 10):
        super().__init__(name, health, power, coins)
        self.type = "hero"
        self.armor = 0
        self.evade = 0
        self.bag = []

    def attack(self, attacked):
        power_level = 0
        if super().prob(8):
            power_level = super().power_up(2)
            
        else:
            power_level = self.power
        super().attack(attacked,power_level)

class Goblin(Character):
    def __init__(self, name, health = 6, power = 2, coins = 0):
        super().__init__(name, health, power,coins)
        self.type = "goblin"
        self.coin_bonus = 2

class Zombie(Character):
    def __init__(self, name, health = 1, power = 4, coins = 0):
        super().__init__(name, health, power,coins)
        self.type = "zombie"
        self.coin_bonus = 0
    
    def alive(self):
            return True

class Medic(Character):
    def __init__(self, name, health = 12, power = 3, coins = 0):
        super().__init__(name, health, power,coins)
        self.type = "medic"
        self.coin_bonus = 2

    def recuperate(self):
        if super().prob(8) and super().alive():
            self.health += 2
            print(f"{self.name} healed and now has {self.health} health.\n")
        
class Shadow(Character):
    def __init__(self, name, health = 1, power = 7, coins = 0):
        super().__init__(name, health, power, coins)
        self.type = "shadow"
        self.coin_bonus = 7

class Alchemist(Character):
    def __init__(self, name, health = 8, power = 3, coins = 3): 
        super().__init__(name, health, power, coins)
        self.type = "alchemist"
        self.coin_bonus = coins * 2

class Giant(Character):
    def __init__(self, name, health = 10, power = 8, coins = 0):
        super().__init__(name, health, power, coins)
        self.type = "giant"
        self.coin_bonus = 6
##########################################
#item class and subclasses
class Item:
    def __init__(self):
        pass


    def use(self,character):
        # if self.instance_var == "health":
        #     character_value == character.health
        # elif self.instance_var == ""
        # elif self.instance_var == ""
        # elif self.instance_var == ""
        # elif self.instance_var == ""
        # elif self.instance_var == ""

        characterAttr = getattr(character, self.instance_var)

        if self.oper == "add":
            characterAttr += self.power
            setattr(character, self.instance_var, characterAttr)
            verb = "added"
        elif self.oper == "sub":
            characterAttr -= self.power
            verb = "subtracted"
        elif self.oper == "mulit":
            characterAttr *= self.power
            verb = "multiplied"
        print(f"{character.name} used {self.name} and {verb} {self.power}\npoints to their health. ")
        print(f"{character.name} has {getattr(character, self.instance_var)} {self.instance_var}")



class Armor(Item):
    def __init__(self):
        pass
class Evade(Item):
    def __init__(self):
        pass
class Potion(Item):
    def __init__(self,name,num,oper,inst_var):
        self.name = name
        self.power = num
        self.oper = oper
        self.instance_var = inst_var
        
class Weapon(Item):
    def __init__(self):
        pass

##########################################
super_tonic = Potion("super_tonic",10,"add","power")

emmit = Hero("emmit")
hyacinth = Goblin("hyacinth")
richard = Zombie("richard")
elizabeth = Medic("elizabeth")
vicar = Shadow("vicar")
daisy = Alchemist("daisy")
rose = Giant("rose")
char_list = [emmit,hyacinth,richard,elizabeth,vicar,daisy,rose]
def main():
    
    while emmit.alive():
        print("- - - - - - - - - -")
        for char in char_list:
            if char.alive():
                char.print_status()
            else:
                print(f"{char.name} is dead")
        print()
        print("What do you want to do?")
        print("""1. fight zombie
2. fight goblin
3. fight medic
4. fight shadow
5. fight alchemist
6. fight giant
7. do nothing
8. flee""")
        print("> ", end=' ')

        choice = input()

        if choice == "1":
            emmit.attack(richard)  
        elif choice == "2":
            emmit.attack(hyacinth)
        elif choice == "3":
            emmit.attack(elizabeth)
            elizabeth.recuperate()
        elif choice == "4":
            emmit.attack(vicar)
        elif choice == "5":
            emmit.attack(daisy)
        elif choice == "6":
            emmit.attack(rose)
        elif choice == "7":
            #pass
            super_tonic.use(emmit)
        elif choice == "8":
            print("Run, Run, Run...")
            break
        else:
            print(f"Invalid input {choice}")

        # if richard.alive():
        #     richard.attack(emmit)
main()