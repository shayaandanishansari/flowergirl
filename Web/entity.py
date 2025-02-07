import pygame
import settings


class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, obstacle_sprites):
        super().__init__(groups)
        self.direction = pygame.math.Vector2()
        self.obstacle_sprites = obstacle_sprites

    def move(self, speed):
        speed = settings.speed*speed + 6
        # Ensures that the magnitude is always one no matter the direction
        # != 0 because a 0 mag vector cannot be normalized
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

            self.rigid_rect.x += self.direction.x * speed
            self.collision('horizontal')
            self.rigid_rect.y += self.direction.y * speed
            self.collision('vertical')

            """
            if self.rigid_rect.x < 59 or self.rigid_rect.x > 4081:
                self.rigid_rect.x += -self.direction.x * speed
            if self.rigid_rect.y < 59 or self.rigid_rect.y > 3541:
                self.rigid_rect.y += -self.direction.y * speed
            """

            self.rect = self.rigid_rect



    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rigid_rect):
                    if self.direction.x > 0:  # moving right
                        self.rigid_rect.right = sprite.rect.left
                    if self.direction.x < 0:  # moving left
                        self.rigid_rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rigid_rect):
                    if self.direction.y > 0:  # moving down
                        self.rigid_rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # moving up
                        self.rigid_rect.top = sprite.rect.bottom

    # Abstract Function
    def damage(self):
        pass

    # Abstract Function
    def death(self):
        pass


