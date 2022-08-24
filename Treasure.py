import pygame
import tools

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
            self.frames.append(tools.get_image(tools.load_graphics('Graphic')['treasure chests']), frame_rect)

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.state = 'rest'

    def update(self):
        self.current_time = pygame.time.get_ticks()
        self.handle_states()

    def handle_states(self):
        if self.state == 'rest':
            self.rest()
        elif self.state == 'open':
            self.open()

    def rest(self):
        pass

    def open(self):
        self.frame_index = 1
        self.image = self.frames[self.frame_index]


