import pygame
import HighScoreFile


class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input

        # Converts text to our font
        self.text = self.font.render(self.text_input, True, self.base_color)

        # For when there is no image given
        if self.image is None:
            self.image = self.text

        # Making a rect of the image so that it is clickable
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    # Checks if mouse is at
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    # Changes color of text when hovered over
    def changeColor(self, position):
        if self.checkForInput(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    # Drawing buttons
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)


class Menu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flower Girl: A Damsel in Distress")
        self.screen = pygame.display.set_mode((1280, 720))
        self.background = pygame.image.load("assets/Background.png").convert_alpha()

        self.screen.blit(self.background, (0, 0))

        self.mouse = None

        # Associations: Composition
        self.PlayButton = Button(pygame.image.load("assets/Play Rect.png"), (640, 240), "Play",
                                 pygame.font.Font("font.ttf", 50), "#d7fcd4", "Orange")
        self.ViewScoreButton = Button(pygame.image.load("assets/Options Rect.png"), (640, 400), "HighScore",
                                      pygame.font.Font("font.ttf", 50), "#d7fcd4", "Orange")
        self.LevelOneButton = Button(pygame.image.load("assets/Play Rect.png"), (640, 240), "Level 1",
                                     pygame.font.Font("font.ttf", 50), "#d7fcd4", "Orange")
        self.LevelTwoButton = Button(pygame.image.load("assets/Play Rect.png"), (640, 400), "Level 2",
                                     pygame.font.Font("font.ttf", 50), "#d7fcd4", "Orange")
        self.BackButton = Button(pygame.image.load("assets/Play Rect.png"), (640, 600), "Back",
                                 pygame.font.Font("font.ttf", 50), "#d7fcd4", "Green")

        self.score = Button(pygame.image.load("assets/Play Rect.png"), (640, 300), str(HighScoreFile.readhighscore()),
                            pygame.font.Font("font.ttf", 50), "White", "Green")

        self.InstructionsButton = Button(pygame.image.load("assets/Options Rect2.png"), (640, 560), "Instructions",
                                         pygame.font.Font("font.ttf", 50), "#d7fcd4", "Orange")

        self.instruction = Button(pygame.image.load("assets/TheInstructions.png"), (640, 275), "",
                                                 pygame.font.Font("font.ttf", 50), "#d7fcd4", "Orange")

        # Arrays of Objects
        self.mainMenuButtons = [self.PlayButton, self.ViewScoreButton, self.InstructionsButton]
        self.levelButtons = [self.LevelOneButton, self.LevelTwoButton, self.BackButton]
        self.scoreButtons = [self.score, self.BackButton]

        # Level 1 or 2
        self.chooseLevel = 0
