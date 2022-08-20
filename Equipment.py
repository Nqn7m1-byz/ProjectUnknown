class Armor:
    phyDef = 0
    magDef = 0
    speed = 0.0
    attack = 0
    intelligence = 0
    name = ""

    def __init__(self, phyDef, magDef, speed,attack,intelligence,name):
        self.phyDef = phyDef
        self.magDef = magDef
        self.speed = speed
        self.attack = attack
        self.intelligence = intelligence
        self.name = name