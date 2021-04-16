# Debugging student's code

import random
class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.coins = coins
    def alive(self):
        if self.name == 'Zombie':
            return True
        elif self.health > 0:
            return True
        else:
            return False
class Hero(Character):
    def __init__(self, health, power, coins):
        self.health = health
        self.power = power
        self.name = 'Hero'
        self.coins = 10
    def attack(self, enemy):
        if enemy.name == "zombie":
            print("Zombie can not die!")
        elif enemy.name == "medic" and random.randint(0,100) < 20:
            enemy.health -= (self.power * 2)
            print("{} does double damage({}) to {}.".format(self.name, (self.power * 2), enemy.name))
        else:
            enemy.health -= self.power
            print("{} does {} damage to {}.".format(self.name, self.power, enemy.name))
        self.bounty(enemy)#this is calling the bounty after the attack
    def bounty(self,enemy):
        if enemy.health <= 0:
            self.coins += enemy.bounty
            print(f'gained {enemy.bounty} coins \n you now have {self.coins} coins.')
    def print_status(self):
        print("{} have {} health and {} power.".format(self.name, self.health, self.power))
class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = 'Goblin'
        self.bounty = 5
    def attack(self,enemy):
        # Goblin attacks hero
        enemy.health -= self.power
        print("You do {} damage to the {}.".format(self.power, enemy.name))
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))
class Zombie(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = 'Zombie'
        self.bounty = 8
    def attack(self,enemy):
        # zombie attacks hero
        enemy.health -= self.power
        print("You do {} damage to the {}.".format(self.power, enemy.name))
class Medic(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = 'Medic'
        self.coins = 8
        self.bounty = 10
    def attack(self, enemy):
        if random.randint(0,100) < 20:
            enemy.health -= (self.power * 2)
            print("{} does double damage({}) to {}.".format(self.name, (self.power * 2), enemy.name))
        else:
            enemy.health -= self.power
            print("{} does {} damage to {}.".format(self.name, self.power, enemy.name))
class Shadow(Character):
    def __init__(self, power, newhealth):
        self.health = newhealth
        self.power = power
        self.name = 'Shadow'
        self.coins = 4
        self.bounty = 6
    def attack(self, enemy):
        if  enemy.name == "shadow" and random.randint(0,10) < 1:
            enemy.health -= (self.power)
            print("{} does damage {} to {}.".format(self.name, self.power , enemy.name))
    def damage(self, enemy):
        shadow_damage = random.random() > 0.2
        if shadow_damage == True:
            self.health -= points
            print("{} received {} damage.")(self.name, points)
        else:
            print("received no damage.") (self.name)
        if self.health <= 0:
            print("is dead.") (self.name)
        # # Hero attacks goblin
        # enmey.health -= self.power
        # print("You do {} damage to the {}.".format(self.power, enmey.name))
class Evade():
    def __init__(self):
        self.cost = 4
        self.name = 'Evade'
    
class SuperTonic():
    pass
class Armour():
    pass
class Shop():
    def __init__(self, items):
        self.items = items

    def do_shopping(self, hero):
        while True:
            print(f"Self items: {self.items[0].cost}")
            print('=====================')
            print('Welcome to the store!')
            print('=====================')
            print(f'You have {hero.coins} coins. ')
            user_u = input('What do you want to buy? ')
            print(user_u)
            for s in len((shop.items)):
                item = shop.items[s]
                print('buy') (s+ 1, item.name, item.cost)
# Main function starts here
def main():
    evade = Evade()
    # superTonic = SuperTonic()
    # armour = Armour()
    # items = [superTonic, armour, evade]
    items = [evade]
    shop = Shop(items)
    hero = Hero( 10, 5, 5)
    choice = input("Who do you want to fight? Goblin (1), Zombie (2), Medic (3), Shadow (4)")
    if choice == "1":
        enemy = Goblin( 6, 2)
    elif choice == "2":
        enemy = Zombie(10, 2)
    elif choice == "3":
        enemy = Medic( 10, 2)
    elif choice == "4":
        enemy = Shadow(1, 6)
    while enemy.alive() and hero.alive():
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The enemy has {} health and {} power.".format(enemy.health, enemy.power))
        print()
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("4. Go Shop")
        print("> ", end=' ')
        # User is attacking
        raw_input = input()
        if raw_input == "1":#  Hero attacks enemy
            hero.attack(enemy)
            # Is the enemy alive?
            if enemy.alive() == False:
                print("The enemy is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            pass
        elif raw_input == "4":
            shop.do_shopping(hero)
        else:
            print("Invalid input {}".format(raw_input))
main()
       # Enemy Attacks
        # if enemy.health > 0:
        #     enemy.attack(hero)
        # if hero.alive() == False:
        #         print("You are dead.")