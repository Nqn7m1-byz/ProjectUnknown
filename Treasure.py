import os
import pygame

class Treasure(pygame.sprite.Sprite):
    def __init__(self, x, y, list):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        good_treasure_rect = [(6, 9, 20, 19), (6, 36, 20, 24)]
        luxurious_treasure_rect = [(70, 137, 20, 19), (70, 164, 20, 24)]
        list = ["A", "B", "C"]
        if a:
            self.frame_rects = good_treasure_rect
        else:
            self.frame_rects = luxurious_treasure_rect

        self.frames = []
        for frame_rect in self.frame_rects:
            self.frames.append(get_image(load_graphics('Graphic')['treasure chests']), frame_rect)

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

def load_graphics(path):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        img = pygame.image.load(os.path.join(path, pic))
        if img.get_alpha():
            img = img.convert_alpha()
        else:
            img = img.convert()
        graphics[name] = img
    return graphics

def get_image(sheet, x, y, width, height):
    image = pygame.Surface((width, height))
    image.blit(sheet, (0,0), (x, y, width, height))
    image = pygame.transform.scale(image, (width, height))
    return image


