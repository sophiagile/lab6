# BATTLE SCENE 

class Character: 
    def __init__(self, name: str, health: int, damage: int):
        self.name = name 
        self.health = health 
        self.health_max = health 
        self.damage = damage

    def attack(self, target)-> None: 
        target.hp -= self.damage 
        target.hp = max(target.hp, 0)

class Hero(Character):
    def __init__(self, name, health):
        super().__init__(name, health, damage=0)
        self.weapon = empty_handed

class Enemy(Character):
    def __init__(self, name, health):
        super().__init__(name, health, damage=0)
        self.weapon = healing_staff

class Weapon:
    def __init__(self,
                 name: str,
                 weapon_type: str,
                 damage: int,
                 value: int)-> None:
        self.name = name
        self.weapon_type = weapon_type 
        self.damage = damage
        self.value = value


empty_handed = Weapon(name="Empty handed",
                      weapon_type="dummy",
                      damage=0,
                      value=0)

healing_staff = Weapon(name="Healing Staff",
               weapon_type="magic",
               damage=-3,
               value=0)


protagonist = Hero(name="Hero", health=100)
protagonist.health = 10

ally = Enemy(name="Friendly Enemy", health=100)


