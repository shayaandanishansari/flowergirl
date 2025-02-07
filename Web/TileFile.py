import pygame
from settings import *


class Things(pygame.sprite.Sprite):
    def __init__(self, groups, pos, image_address):
        # pygame.sprite.Sprite().__init__(groups)
        super().__init__(groups)
        self.image = pygame.image.load(image_address).convert_alpha()
        self.rect = self.image.get_rect(center=pos)

    def death(self):
        pass

    def damage(self):
        pass


class Rock(Things):
    def __init__(self, pos, groups, image_address):
        # Things().__init__(groups, pos, image_address)
        super().__init__(groups, pos, image_address)
        self.rect = self.rect.inflate(-10, -10)


class Bush(Things):
    def __init__(self, pos, groups, image_address):
        super().__init__(groups, pos, image_address)
        self.rect = self.rect.inflate(-10, -10)
        self.health = 100

    # Function Overriding
    def death(self):
        if self.health == 0:
            # Destroys sprite object
            self.kill()

    # Function Overriding
    def damage(self):
        self.health -= 10


