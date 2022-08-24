import pygame


class Monster:
    maxHealth = 0

    def __init__(self, health, attack, phyDef, magDef):
        self.health = health
        self.maxHealth = health
        self.attack = attack
        self.phyDef = phyDef
        self.magDef = magDef
        self.vel_y = 0

    def Update(self):
        x_move = 0
        y_move = 0

    def Attack(self, monsters):
        pass

    def Magic(self):
        pass

    def Defend(self):
        pass

    def PhysicsDefend(self, damage):
        self.health -= (damage - self.phyDef)
        Monster.Defend(self)

    def MagicDefend(self, damage):
        self.health -= (damage - self.magDef)
        Monster.Defend(self)

class Witch(Monster):
    pass
