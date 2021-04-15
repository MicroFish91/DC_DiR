# In this simple RPG game, the hero fights the goblin. He has the options to:
# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, enemy):
        pass
    def alive(self):
        if self.health > 0:
            return True
        else:
            print(f"The {self.name} is dead.")
    def print_status(self):
        pass

class Hero(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Hero"
    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")

class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Goblin"
    def attack(self, enemy):
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
    def print_status(self):
        print(f"The goblin has {self.health} health and {self.power} power.")

def main():
    hero = Hero(10, 5)
    goblin = Goblin(6,2)

    while goblin.alive() and hero.alive():
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if goblin.alive():
            # Goblin attacks hero
            if hero.alive():
                print("You are dead.")
main()