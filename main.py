import pygame
from Player import Player

player = Player(10, 5, 5, 6, 1)


def main():
    pygame.init()
    screen=pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Untitled")
    background=pygame.image.load("bg.png").convert()
    running = True
    while running:
        screen.blit(background,(0,0))
        running = CheckEvents()
        player.Update()
        screen.blit(player.image,player.rect)
        pygame.display.update()


def CheckEvents():
    quit = True
    # input detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
    return quit


if __name__ == '__main__':
    main()
