import pygame
from Player import Player

running = True
player = Player(10, 5, 5, 6)

def main():
    pygame.init()
    pygame.display.set_mode(1980,1080)
    pygame.display.set_caption("Untitled")
    while running:
        CheckEvents()


def CheckEvents():
    # input detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.Left()
            if event.key == pygame.K_s:
                player.Down()
            if event.key == pygame.K_d:
                player.Right()
            if event.key == pygame.K_w:
                player.Up()
            if event.key == pygame.K_SPACE:
                pass
