import os
import pygame


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
    image = pygame.transform.scale(image, width, height)
    return image
