import pygame

from random import randint

import settings
from settings import *
from entity import Entity
from pickup import Heart


class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, obstacle_sprites, visible_sprites, pickup_sprites):

        # general setup
        super().__init__(groups, obstacle_sprites)
        self.sprite_type = 'enemy'

        # Reference of visible_sprites passed
        self.visible_sprites = visible_sprites
        self.pickup_sprites = pickup_sprites

        # stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.attack_radius = monster_info['attack_radius']
        self.image_address = monster_info['image']
        self.image = pygame.image.load(self.image_address).convert_alpha()

        # movement
        self.rect = self.image.get_rect(topleft=pos)
        self.rigid_rect = self.rect.inflate(0, -10)
        # self.obstacle_sprites = obstacle_sprites

        self.distance = 0

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, player):
        self.distance = self.get_player_distance_direction(player)[0]

        # if distance <= self.attack_radius and self.can_attack:
        if self.distance <= self.attack_radius:
            self.status = 'attack'
        else:
            self.status = 'move'

    def actions(self, player):
        if self.status == 'attack':
            player.damage(self)
            player.death()
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:  # not needed because enemy never still
            self.direction = pygame.math.Vector2()

    def update(self):
        self.move(self.speed)

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)

    def death(self):
        # wif pygame.time.get_ticks() % 10 == 1:

        if self.health < 0:
            settings.score += self.exp
            if randint(1, 75) == 1:
                Heart(self.rect.center, [self.visible_sprites, self.pickup_sprites])
            self.kill()
            return True
        else:
            return False

    def damage(self):
        self.health -= 20