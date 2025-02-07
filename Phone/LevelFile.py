# Python Libraries
import pygame

# My Files
from PlayerFile import *
from TileFile import *
from random import randint
from enemy import Enemy


# In this File: 2 Classes
# 1 Level Class
# 1 Camera Class: public pygame.sprite.Group

class Level:
    def __init__(self):
        # Association: Composition
        # Using getter function to load in current display which is "screen" a private attribute of Game
        self.display_surface = pygame.display.get_surface()

        # Polymorphism: "Camera" is derived class of "pygame.sprite.Group"
        # Upcasting: when objects are stored in visible_sprites

        # Composition: object that stores array of objects
        # ObjectArrays
        self.visible_sprites = Camera()
        self.obstacle_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.pickup_sprites = pygame.sprite.Group()

    # Method for generating objects created only once
    # Background, Boundary, Rocks, Bushes, Player
    def create_map(self):
        # All objects created except player are not directly accessible to the Player Class
        # They are stored in different "pygame.sprite.Group()"s: array of objects

        # Background
        if settings.game_level == 1:
            for x in range(0, ground_width * scale + 1, ground_width):
                for y in range(0, ground_height * scale + 1, ground_height):
                    Things(self.visible_sprites, (x, y), 'ground_cropped.png')

            # Rocks around the boundary
            Rock((627, 615), [self.visible_sprites, self.obstacle_sprites], 'rock.png')
            Rock((600, 1200), [self.visible_sprites, self.obstacle_sprites], 'rock.png')
            Rock((700, 2000), [self.visible_sprites, self.obstacle_sprites], 'rock.png')
            Rock((700, 2900), [self.visible_sprites, self.obstacle_sprites], 'rock.png')

            Rock((3569 - 120, 615), [self.visible_sprites, self.obstacle_sprites], 'rock.png')
            Rock((3569 - 200, 1200), [self.visible_sprites, self.obstacle_sprites], 'rock.png')
            Rock((3569 - 80, 2000), [self.visible_sprites, self.obstacle_sprites], 'rock.png')
            Rock((3569 - 180, 2900), [self.visible_sprites, self.obstacle_sprites], 'rock.png')

            Rock((1500, 3100), [self.visible_sprites, self.obstacle_sprites], 'rock.png')
            Rock((1915, 3000), [self.visible_sprites, self.obstacle_sprites], 'rock.png')
            Rock((3569, 3029), [self.visible_sprites, self.obstacle_sprites], 'rock.png')

            Rock((1543, 656), [self.visible_sprites, self.obstacle_sprites], 'rock.png')
            Rock((2817, 571), [self.visible_sprites, self.obstacle_sprites], 'rock.png')

        elif settings.game_level == 2:
            for x in range(0, ground_width * scale + 1, ground_width):
                for y in range(0, ground_height * scale + 1, ground_height):
                    Things(self.visible_sprites, (x, y), 'ground_desert6.png')
            # Rocks around the boundary
            Rock((627, 615), [self.visible_sprites, self.obstacle_sprites], 'bush.png')
            Rock((600, 1200), [self.visible_sprites, self.obstacle_sprites], 'bush.png')
            Rock((700, 2000), [self.visible_sprites, self.obstacle_sprites], 'bush.png')
            Rock((700, 2900), [self.visible_sprites, self.obstacle_sprites], 'bush.png')

            Rock((3569 - 120, 615), [self.visible_sprites, self.obstacle_sprites], 'bush.png')
            Rock((3569 - 200, 1200), [self.visible_sprites, self.obstacle_sprites], 'bush.png')
            Rock((3569 - 80, 2000), [self.visible_sprites, self.obstacle_sprites], 'bush.png')
            Rock((3569 - 180, 2900), [self.visible_sprites, self.obstacle_sprites], 'bush.png')

            Rock((1500, 3100), [self.visible_sprites, self.obstacle_sprites], 'bush.png')
            Rock((1915, 3000), [self.visible_sprites, self.obstacle_sprites], 'bush.png')
            Rock((3569, 3029), [self.visible_sprites, self.obstacle_sprites], 'bush.png')

            Rock((1543, 656), [self.visible_sprites, self.obstacle_sprites], 'bush.png')
            Rock((2817, 571), [self.visible_sprites, self.obstacle_sprites], 'bush.png')

        # Player
        if settings.game_level == 1:
            self.player = Player((ground_width * scale / 2, ground_height * scale / 2), [self.visible_sprites],
                                 self.obstacle_sprites, self.enemy_sprites, "player.png")

        elif settings.game_level == 2:
            self.player = Player((ground_width * scale / 2, ground_height * scale / 2), [self.visible_sprites],
                                 self.obstacle_sprites, self.enemy_sprites, "tank.png")

        # Rocks and Bushes
        for i in range(settings.object_rate):
            if settings.game_level == 1:
                x = randint(571 + 128, 3569 - 128)
                y = randint(571 + 128, 3029 - 128)

                rand = randint(1, 2)

                # 1 third objects are unbreakable: 33%
                if rand == 1:
                    if not x in range(self.player.rect.centerx - 256,
                                      self.player.rect.centerx + 256) and not y in range(self.player.rect.centerx - 256,
                                                                                         self.player.rect.centerx + 256):
                        Rock((x, y), [self.visible_sprites, self.obstacle_sprites], 'rock.png')

                # 2 third of objects breakable: 66%
                if rand == 2:
                    if not x in range(self.player.rect.centerx - 256,
                                      self.player.rect.centerx + 256) and not y in range(self.player.rect.centerx - 256,
                                                                                         self.player.rect.centerx + 256):
                        Bush((x, y), [self.visible_sprites, self.obstacle_sprites], 'bush.png')


            elif settings.game_level == 2:
                x = randint(571 + 128, 3569 - 128)
                y = randint(571 + 128, 3029 - 128)

                rand = randint(1, 2)

                # 1 third objects are unbreakable: 33%
                if rand == 1:
                    if not x in range(self.player.rect.centerx - 256,
                                      self.player.rect.centerx + 256) and not y in range(self.player.rect.centerx - 256,
                                                                                         self.player.rect.centerx + 256):
                        Rock((x, y), [self.visible_sprites, self.obstacle_sprites], 'rocks.png')

                # 2 third of objects breakable: 66%
                if rand == 2:
                    if not x in range(self.player.rect.centerx - 256,
                                      self.player.rect.centerx + 256) and not y in range(self.player.rect.centerx - 256,
                                                                                         self.player.rect.centerx + 256):
                        Bush((x, y), [self.visible_sprites, self.obstacle_sprites], 'cactus.png')

        # Boundary
        if settings.game_level == 1:
            for i in range(64 * 8, ground_width * scale - 64 * 8, 64):
                Rock((i, 64 * 8), [self.visible_sprites, self.obstacle_sprites], 'rock.png')
                Rock((i, ground_height * scale - 64 * 8), [self.visible_sprites, self.obstacle_sprites], 'rock.png')

            for j in range(64 * 8, ground_height * scale - 64 * 8, 64):
                Rock((64 * 8, j), [self.visible_sprites, self.obstacle_sprites], 'rock.png')
                Rock((ground_width * scale - 64 * 8, j), [self.visible_sprites, self.obstacle_sprites], 'rock.png')

        elif settings.game_level == 2:
            for i in range(64 * 8, ground_width * scale - 64 * 8, 64):
                Rock((i, 64 * 8), [self.visible_sprites, self.obstacle_sprites], 'rocks.png')
                Rock((i, ground_height * scale - 64 * 8), [self.visible_sprites, self.obstacle_sprites], 'rocks.png')

            for j in range(64 * 8, ground_height * scale - 64 * 8, 64):
                Rock((64 * 8, j), [self.visible_sprites, self.obstacle_sprites], 'rocks.png')
                Rock((ground_width * scale - 64 * 8, j), [self.visible_sprites, self.obstacle_sprites], 'rocks.png')

    # Method for generating enemies while game is running
    def spawn(self):
        # All objects created except player are not directly accessible to the Player Class

        # Calculating spawning location: which will be away from the player
        if randint(0, 1):
            x = randint(self.player.rect.centerx - 1280, self.player.rect.centerx - 700)
            if (x < 571 + 128):
                x = 2070
        else:
            x = randint(self.player.rect.centerx + 700, self.player.rect.centerx + 1200)
            if (x > 3569 - 128):
                x = 2070

        if randint(0, 1):
            y = randint(self.player.rect.centery - 1000, self.player.rect.centery - 500)
            if (y < 571 + 128):
                y = 1800
        else:
            y = randint(self.player.rect.centery + 500, self.player.rect.centery + 1000)
            if (y > 3029 - 128):
                y = 1800

        rand = randint(1, 20)

        if settings.game_level == 1:
            if (rand >= 1 and rand <= 8):
                Enemy('squid', (x, y), [self.visible_sprites, self.enemy_sprites], self.obstacle_sprites,
                      self.visible_sprites, self.pickup_sprites)

            # 35% chance for tier 2 enemy
            if (rand >= 9 and rand <= 15):
                Enemy('spirit', (x, y), [self.visible_sprites, self.enemy_sprites], self.obstacle_sprites,
                      self.visible_sprites, self.pickup_sprites)

            # 20% chance for tier 3 enemy
            if (rand >= 16 and rand <= 19):
                Enemy('bamboo', (x, y), [self.visible_sprites, self.enemy_sprites], self.obstacle_sprites,
                      self.visible_sprites, self.pickup_sprites)

            # 5% chance for boss
            if (rand == 20):
                Enemy('raccoon', (x, y), [self.visible_sprites, self.enemy_sprites], self.obstacle_sprites,
                      self.visible_sprites, self.pickup_sprites)

        elif settings.game_level == 2:
            if (rand >= 1 and rand <= 8):
                Enemy('fire_spirit', (x, y), [self.visible_sprites, self.enemy_sprites], self.obstacle_sprites,
                      self.visible_sprites, self.pickup_sprites)

            # 35% chance for tier 2 enemy
            if (rand >= 9 and rand <= 15):
                Enemy('spider', (x, y), [self.visible_sprites, self.enemy_sprites], self.obstacle_sprites,
                      self.visible_sprites, self.pickup_sprites)

            # 20% chance for tier 3 enemy
            if (rand >= 16 and rand <= 19):
                Enemy('zombie', (x, y), [self.visible_sprites, self.enemy_sprites], self.obstacle_sprites,
                      self.visible_sprites, self.pickup_sprites)

            # 5% chance for boss
            if (rand == 20):
                Enemy('troll', (x, y), [self.visible_sprites, self.enemy_sprites], self.obstacle_sprites,
                      self.visible_sprites, self.pickup_sprites)

    # Method for drawing and moving created objects
    # Polymorphism: Overriding
    def run(self):
        # Function Overriding: "draw()" is a function of derived class "Camera" and base class "pygame.sprite.Group"
        # Draws all objects in "visible_sprites"
        self.visible_sprites.draw(self.player)

        # Function Overriding: "update()" is a function of derived class "Camera" and base class "pygame.sprite.Group"
        # Uses update method in each object of visible sprites
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)

        settings.count = len(self.enemy_sprites)
        # Spawn ends if player is dead
        if not settings.playerdeath and settings.count < 50:
            if randint(1, spawn_rate) == 1:
                for i in range(wave):
                    self.spawn()
        settings.count = 0

        # If the player is getting a pickup
        for pickup in self.pickup_sprites:
            pickup.touching(self.player)


# Inheritance
class Camera(pygame.sprite.Group):
    def __init__(self):
        # Setting values to be worked on
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = width / 2
        self.half_height = height / 2
        self.offset = pygame.math.Vector2()

    # Function Overriding: "draw" is a function of base class pygame.sprite.Group as well
    def draw(self, player):
        # Getting the position of the player with respect to the center of the screen
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Displaying all objects in a sprite_groups(arrays of objects) with offset:
        # All sprites that are in the same group: VisibleSprites
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    # New Method of only Camera Class
    # ???
    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if
                         hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
