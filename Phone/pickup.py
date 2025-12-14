import pygame
from settings import *


class Heart(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/heart.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)

    def touching(self, other):
        if self.rect.colliderect(other.rect):
            if other.health > 9000:
                other.health = 10000
            else:
                other.health += 1000
            self.kill()

