class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def alive(self): 
        if self.name == 'Zombie':
            return True
        elif self.health > 0:
            return True
        else: 
            return False

class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = 'Hero'
    def attack(self, enmey):
        # Hero attacks goblin
        enmey.health -= self.power
        print("You do {} damage to the {}.".format(self.power, enmey.name))
    def print_status(self):
        print("{} have {} health and {} power.".format(self.name, self.health, self.power))

class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = 'Goblin'

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
    def attack(self,enemy):
        # Goblin attacks hero
        enemy.health -= self.power
        print("You do {} damage to the {}.".format(self.power, enemy.name))

# Main function starts here
def main():
    hero = Hero(10,5)

    choice = input("Who do you want to fight? Goblin (1), Zombie (2)")

    if choice == "1":
        enemy = Goblin(6, 2)
    elif choice == "2":
        enemy = Zombie(10, 2)


    while enemy.alive() and hero.alive():
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The enemy has {} health and {} power.".format(enemy.health, enemy.power))
        print()
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')

        # User is attacking
        raw_input = input()
        if raw_input == "1":
            # Hero attacks enemy
            hero.attack(enemy) # Hero - self, enemy
            # Is the enemy alive?
            if enemy.alive() == False:
                print("The enemy is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
        else:
            print("Invalid input {}".format(raw_input))

        # Enemy Attacks
        if enemy.health > 0:
            # enemy attacks heros
            # enemy is attacking the hero
            enemy.attack(hero)
            if hero.alive() == False:
                print("You are dead.")
        # if zombie.health = 0
        #     zombie.alive()
        #     print('You can not die')

main()