# Python Libraries
import pygame, asyncio, time
from sys import exit

import settings
# My Files
from settings import *
from LevelFile import Level
import menu


# In this File: 1 Class, 1 Main
# 1 Game Class
# Main

class Game:
    def __init__(self):
        # Initialising Pygame and Generating Window
        pygame.init()
        pygame.display.set_caption("Flower Girl: A Damsel in Distress")

        # Private Attribute Screen
        self.screen = pygame.display.set_mode([width, height])

        # Association: Composition
        # Clock object has attributes related to frames
        self.clock = pygame.time.Clock()

        # Association: Composition
        # Level is our own class
        self.level = Level()

        self.rungame = True

        self.time = 0
        self.time_now = 0

    # Run function is used to generate each frame
    def run(self):
        pass


async def main():
    # Creates Menu Object: Menu Class is in the file "menu.py"

    # Game Object Created
    # Parameterised Constructor with choice made in Menu called

    while settings.gameover:
        settings.gameover = False
        settings.playerdeath = False
        settings.score = 0
        settings.count = 0
        settings.wave = 1
        settings.speed = 1

        # Game Object Created
        # Parameterised Constructor with choice made in Menu called
        game = Game()

        game_menu = menu.Menu()
        settings.menu_open = True
        settings.menu_page = True
        settings.highscore_page = False
        settings.level_page = False

        settings.map_created = False

        # Pause Button
        pause = menu.Button(pygame.image.load("assets/Pause.png"), (1100, 50), "",
                            pygame.font.Font("font.ttf", 200), "White", "Red")
        paused = False

        QuitButton = menu.Button(pygame.image.load("assets/QuitButton3as"), (1200, 50), "",
                                 pygame.font.Font("font.ttf", 200), "White", "Red")

        prev_time = time.time()

        q = None

        while game.rungame:

            # Menu
            if settings.menu_open:
                if settings.menu_page:
                    game_menu.mouse = pygame.mouse.get_pos()
                    game_menu.screen.blit(game_menu.background, (0, 0))

                    # Drawing all buttons
                    for button in game_menu.mainMenuButtons:
                        button.changeColor(game_menu.mouse)
                        button.update(game_menu.screen)

                    # Clicking
                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:

                            # Go to Level Page
                            if game_menu.PlayButton.checkForInput(game_menu.mouse):
                                settings.level_page = True
                                settings.menu_page = False
                                settings.highscore_page = False
                                settings.instructions_page = False
                                break

                            # Got to Highscore Page
                            if game_menu.ViewScoreButton.checkForInput(game_menu.mouse):
                                settings.level_page = False
                                settings.menu_page = False
                                settings.highscore_page = True
                                settings.instructions_page = False
                                break
                            if game_menu.InstructionsButton.checkForInput(game_menu.mouse):
                                settings.level_page = False
                                settings.menu_page = False
                                settings.highscore_page = False
                                settings.instructions_page = True
                                break

                # Highscore Page
                if settings.highscore_page:
                    game_menu.mouse = pygame.mouse.get_pos()
                    game_menu.screen.blit(game_menu.background, (0, 0))
                    game_menu.BackButton.changeColor(game_menu.mouse)
                    game_menu.BackButton.update(game_menu.screen)
                    game_menu.score.update(game_menu.screen)

                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        # Go to Menu Page
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if game_menu.BackButton.checkForInput(game_menu.mouse):
                                settings.level_page = False
                                settings.menu_page = True
                                settings.highscore_page = False
                                settings.instructions_page = False
                                break

                # Levels Page
                if settings.level_page:
                    game_menu.mouse = pygame.mouse.get_pos()
                    game_menu.screen.blit(game_menu.background, (0, 0))

                    for button in game_menu.levelButtons:
                        button.changeColor(game_menu.mouse)
                        button.update(game_menu.screen)

                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            # Go to Game (choose level == 1)
                            if game_menu.LevelOneButton.checkForInput(game_menu.mouse):
                                game_menu.chooseLevel = 1
                                break
                            # Go to Game (choose level == 1)
                            if game_menu.LevelTwoButton.checkForInput(game_menu.mouse):
                                game_menu.chooseLevel = 2
                                break
                            # Go to Menu Page
                            if game_menu.BackButton.checkForInput(game_menu.mouse):
                                settings.level_page = False
                                settings.menu_page = True
                                settings.highscore_page = False
                                settings.instructions_page = False
                                break

                # Instructions Page
                if settings.instructions_page:
                    game_menu.mouse = pygame.mouse.get_pos()
                    game_menu.screen.blit(game_menu.background, (0, 0))
                    game_menu.BackButton.changeColor(game_menu.mouse)
                    game_menu.BackButton.update(game_menu.screen)
                    game_menu.instruction.update(game_menu.screen)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                        # Go to Menu Page
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if game_menu.BackButton.checkForInput(game_menu.mouse):
                                settings.level_page = False
                                settings.menu_page = True
                                settings.highscore_page = False
                                settings.instructions_page = False
                                break

                if game_menu.chooseLevel == 1 or game_menu.chooseLevel == 2:
                    settings.menu_open = False
                    settings.level_page = False
                    settings.highscore_page = False
                    settings.menu_page = False
                    settings.instructions_page = False

                    settings.game_level = game_menu.chooseLevel

                pygame.display.update()
                await asyncio.sleep(0)

            # Game
            else:
                if not settings.map_created:
                    game.level.create_map()
                    settings.map_created = True
                settings.dt = time.time() - prev_time
                prev_time = time.time()
                mouse = pygame.mouse.get_pos()


                # Check every event happening
                for event in pygame.event.get():
                    mouse = pygame.mouse.get_pos()
                    # Quitting condition
                    if event.type == pygame.QUIT or (
                            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or settings.gameover:
                        # pygame.quit()
                        game.rungame = False

                    # Game Restart condition
                    if settings.playerdeath and q != None:
                        if q.checkForInput(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                            settings.gameover = True
                            break

                    # Quit Button Pressed
                    if QuitButton.checkForInput(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                        settings.gameover = True
                        settings.playerdeath = True
                        break

                    # Pause Condition
                    if pause.checkForInput(
                            mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                        if not paused:
                            paused = True
                        else:
                            paused = False

                if paused:
                    instruction = menu.Button(pygame.image.load("assets/TheInstructions.png"), (640, 275), "",
                                         pygame.font.Font("font.ttf", 50), "#d7fcd4", "Orange")
                    instruction.update(game.screen)
                    # pause.update(game.screen)
                    pygame.display.update()
                    # settings.clock_back = int(pygame.time.get_ticks() / 1000)
                    game.clock.tick(fps)
                    await asyncio.sleep(0)
                    continue

                # Break While Loop if Quitting before the rest of the loop runs (Using before because was pygame.quit() in quit loop
                if not game.rungame:
                    break

                # Screen.fill
                game.screen.fill("light green")
                # Will call run function of the Level object created at runtime in Game
                game.level.run()

                # Drawing "Game Over" Button if player is dead
                if settings.playerdeath:
                    # self.clock.tick(fps)
                    mouse = pygame.mouse.get_pos()
                    q = menu.Button(pygame.image.load("assets/Options Rect.png"), (640, 100), "Game Over",
                                    pygame.font.Font("font.ttf", 40), "White", "Red")
                    q.changeColor(mouse)
                    q.update(game.screen)
                    game.time = 0
                    game.time_now = 0
                    settings.clock_back = int(pygame.time.get_ticks() / 1000)
                    if settings.score > settings.highscore:
                        settings.highscore = settings.score

                # Wave every 30 seconds
                # Displaying wave number

                game.time = int(pygame.time.get_ticks() / 1000) - settings.clock_back
                if game.time % 30 == 0 and game.time > game.time_now:
                    settings.wave += 1
                    settings.speed += 1
                    game.time_now = game.time

                if game.time - game.time_now < 5 and not settings.playerdeath:
                    w = menu.Button(pygame.image.load("assets/Picture1.png"), (640, 100), "WAVE " + str(settings.wave),
                                    pygame.font.Font("font.ttf", 50), "White", "Red")
                    w.update(game.screen)

                target = menu.Button(pygame.image.load("assets/Target.png"), (mouse), "",
                                    pygame.font.Font("font.ttf", 50), "White", "Red")
                target.update(game.screen)

                # Quit Button Displayed
                QuitButton.update(game.screen)

                # Pause Button Refreshed
                pause.update(game.screen)

                # Display is refreshed
                # Operator Overriding: many objects of different classes (base and derived) have an update function
                pygame.display.update()

                # Controlling Frame Rate: set to 60 in settings
                game.clock.tick(fps)
                await asyncio.sleep(0)

        settings.wave -= 1
        settings.speed -= 1


asyncio.run(main())
