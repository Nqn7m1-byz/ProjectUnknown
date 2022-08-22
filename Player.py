import pygame


class Player:
    level = 1
    exp = 0
    god = False
    maxHealth = 0
    inventory = list()
    magic = list()
    facing = True
    length_height = (210, 500)
    transform = None

    def __init__(self, health, attack, phyDef, magDef, intelligence):
        self.health = health
        self.maxHealth = health
        self.attack = attack
        self.phyDef = phyDef
        self.magDef = magDef
        self.intelligence = intelligence
        self.image = pygame.image.load('player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (100, 130)
        self.vel_y = 0
        self.jumped = False

    def Update(self):
        x_move = 0
        y_move = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped is False:
            self.vel_y = -18
            self.jumped = True
        if not key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_a]:
            x_move -= 5
        if key[pygame.K_d]:
            x_move += 5
        self.vel_y += 1.2
        if self.vel_y > 10:
            self.vel_y = 10
        y_move += self.vel_y
        self.rect.x += x_move
        self.rect.y += y_move

    def Attack(self, monsters):
        # put animation here

        for monster in monsters:
            pass

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

    def GodMode(self):
        self.health=1000000000
        self.maxHealth=self.health
