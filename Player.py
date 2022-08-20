from enum import Enum
import pygame

class Player:
    health = 0
    attack = 0
    intelligence = 0
    phyDef = 0
    magDef = 0
    level = 1
    exp = 0
    god = False
    maxHealth = 0
    inventory = list()
    magic = list()
    x=100
    y=30
    facing=True
    upper_left = (100, 30)
    length_height = (210, 500)
    transform = pygame.Rect(upper_left, length_height)

    def __init__(self, health, attack, phyDef, magDef):
        self.health = health
        self.maxHealth = health
        self.attack = attack
        self.phyDef = phyDef
        self.magDef = magDef

    def Attack(self,monsters):
        # put animation here

        for monster in monsters:
            if()

    def Magic(self):
        # put animation here

        pass

    def Defend(self):
        # put animation here

        pass

    def PhysicsDefend(self, damage):
        self.health -= (damage - self.phyDef)
        Player.Defend(self)

    def MagicDefend(self, damage):
        self.health -= (damage - self.magDef)
        Player.Defend(self)

    def AddInventory(self, equipment):
        self.inventory.append(equipment)

    def Equipt(self, weapon):
        self.attack += weapon.attack
        self.intelligence += weapon.inteligence
        self.magDef += weapon.magDef
        self.phyDef += weapon.phyDef

    def Levelup(self):
        if self.exp == self.level * self.level * 10:
            self.level += 1
            self.maxHealth += 10
            self.health = self.maxHealth

    def Left(self):
        self.x-=2

    def Up(self):
        self.y-=2

    def Right(self):
        self.x+=2

    def Down(self):
        pass

    def Fall(self):
        self.y-=3
