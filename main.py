import pygame
from Player import Player

player = Player(10, 5, 5, 6)


def main():
    pygame.init()
    pygame.display.set_mode((1000, 500))
    pygame.display.set_caption("Untitled")
    running = True
    while running:
        running = CheckEvents()
        player.update()


def CheckEvents():
    quit = True
    # input detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
    return quit


if __name__ == '__main__':
    main()
