# Python Libraries
# import pygame
# import menu
from math import degrees, atan2, pi, sin, cos

import HighScoreFile
# My Files
import settings
from settings import *
from debugfile import *
from entity import Entity


# In this File: 2 Classes
# 1 Player Class: public Entity
# 1 Bullet Class: public pygame.sprite.Sprite

# Inheritance
class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, enemy_sprites, img_add):
        # Calling the constructor of base class pygame.sprite.Sprite
        super().__init__(groups, obstacle_sprites)

        # Image to be blit
        self.bullet = None
        self.mouse = None

        self.image = pygame.image.load(img_add).convert_alpha()

        # Constant Image that will be the basis of rotation
        self.base_image = self.image

        # RigidBody: HitBox
        self.rigid_rect = self.image.get_rect(center=pos)

        # DrawBody: Blit Image
        self.rect = self.image.get_rect(center=pos)

        # Set the direction of the player as a Vector
        self.direction = pygame.math.Vector2()

        # The player need to know what sprites to interact with
        # self.obstacle_sprites = obstacle_sprites
        self.enemy_sprites = enemy_sprites

        # For the Bullet
        # Store what Group The Player is so that we can add bullet to that group too
        self.groups = groups
        self.shoot = False
        self.shoot_cooldown = 3
        self.gun_barrel_offset = pygame.math.Vector2(36, 0)
        self.angles = 0

        self.health = 10000

    def player_rotation(self):
        # These attributes are automatically generated as attributes of the Player Class
        self.mouse = pygame.mouse.get_pos()
        self.angles = degrees(atan2((self.mouse[1] - height/1.2), (self.mouse[0] - width/1.2)))
        self.image = pygame.transform.rotate(self.base_image, - self.angles)
        # Attribute Inheritance
        self.rect = self.image.get_rect(center=self.rigid_rect.center)

    def input(self):
        self.direction.x = 0
        self.direction.y = 0

        # Bullet Input
        if pygame.mouse.get_pressed() == (1, 0, 0):
            self.shoot = True
            self.is_shooting()
            if self.bullet != None:
                pass

            if int(self.angles) in range(10, 170):
                self.direction.y = -1
            if int(self.angles) in range(-170, -10):
                self.direction.y = 1
            if int(self.angles) in range(90+10, 180-10) or int(self.angles) in range(-180+10, -90-10):
                self.direction.x = 1
            if int(self.angles) in range(-90+10, 0-10) or int(self.angles) in range(0+10, 90-10):
                self.direction.x = -1

            if int(self.angles) in range(-10,10):
                self.direction.x = -1
            if int(self.angles) in range(-180,-170) or int(self.angles) in range(170, 180):
                self.direction.x = 1
        else:
            self.shoot = False

    def is_shooting(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 6
            spawn_bullet_pos = self.rigid_rect.center + self.gun_barrel_offset.rotate(self.angles)
            self.bullet = Bullet(spawn_bullet_pos[0], spawn_bullet_pos[1], self.groups, self.obstacle_sprites,
                                 self.angles, self.enemy_sprites)

    # Function Overloading
    def update(self):
        # Take input and then move the player
        self.input()
        self.move(5)
        self.player_rotation()
        # pygame.draw.rect(pygame.display.get_surface(), 'red', self.rect, 1)
        # pygame.draw.rect(pygame.display.get_surface(), 'yellow', self.rigid_rect, 1)
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        debug("Score: " + str(settings.score))
        debug("Health: " + str(self.health // 100), 40)

    def death(self):
        if self.health <= 0:
            settings.playerdeath = True
            self.kill()

    def damage(self, other):
        self.health -= other.attack_damage

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, groups, obstacle_sprites, angle, enemy_sprites):
        # Calling the constructor of base class pygame.sprite.Sprite
        super().__init__(groups)

        self.enemy_sprites = enemy_sprites

        if settings.game_level == 1:
            self.image = pygame.image.load("flower.png").convert_alpha()
        elif settings.game_level == 2:
            self.image = pygame.image.load("bullet.png").convert_alpha()

        self.image = pygame.transform.rotozoom(self.image, 0, 2)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.angle = angle
        self.obstacle_sprites = obstacle_sprites

        self.x_vel = cos(self.angle * (2 * pi / 360)) * 50 - (settings.speed*6)
        self.y_vel = sin(self.angle * (2 * pi / 360)) * 50 - (settings.speed*6)
        self.bullet_lifetime = 1000
        self.spawn_time = pygame.time.get_ticks()

    def bullet_movement(self, other_sprites, enemy_sprites):
        self.x += self.x_vel
        self.y += self.y_vel

        self.rect.centerx = self.x
        self.rect.centery = self.y

        if pygame.time.get_ticks() - self.spawn_time > self.bullet_lifetime:
            self.kill()

        for sprite in other_sprites:
            # Normal Collision
            if sprite.rect.colliderect(self.rect):
                self.kill()
                sprite.damage()
                sprite.death()

        for sprite in enemy_sprites:
            # Normal Collision
            if sprite.rect.colliderect(self.rect):
                self.kill()
                sprite.damage()
                sprite.death()

    def update(self):
        self.bullet_movement(self.obstacle_sprites, self.enemy_sprites)