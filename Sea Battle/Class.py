import pygame
import random
pygame.init()
size_cells = 35

class Settings:
    def __init__(self, width, height, x, y, orientation):
        self.WIDTH = width
        self.HEIGHT = height
        self.IMAGE = None
        self.X = x
        self.Y = y
        self.ORIENTATION = orientation
        
    def rotate_ship(self):
        if self.ORIENTATION == "horizontal":
            self.ORIENTATION = "vertical"
        else:
            self.ORIENTATION = "horizontal"

    def load_image(self):
        self.IMAGE = pygame.image.load("images/Ship.png")
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))

    def blit_sprite(self, screen_game):
        screen_game.blit(self.IMAGE, (self.X, self.Y))

    def rotate(self, rotation):
        if rotation == 90:
            self.rotate_ship(self)
            self.IMAGE = pygame.transform.rotate(self.IMAGE, 90)
            self.WIDTH, self.HEIGHT = self.HEIGHT, self.WIDTH

    def blit_sprite(self, screen_game):
        screen_game.blit(self.IMAGE, (self.X, self.Y))

class Ship4(Settings):
    def __init__(self, x1, y1, width1=140, height1=35):
        orientation1 = random.choice(["horizontal", "vertical"])
        Settings.__init__(self, width=width1, height=height1, x=x1, y=y1, orientation=orientation1)
        self.load_image(self)

class Ship3(Settings):
    def __init__(self, x1, y1, width1=105, height1=35):
        orientation1 = random.choice(["horizontal", "vertical"])
        Settings.__init__(self, width=width1, height=height1, x=x1, y=y1, orientation=orientation1)
        self.load_image(self)

class Ship2(Settings):
    def __init__(self, x1, y1, width1=70, height1=35):
        orientation1 = random.choice(["horizontal", "vertical"])
        Settings.__init__(self, width=width1, height=height1, x=x1, y=y1, orientation=orientation1)
        self.load_image(self)

class Ship1(Settings):
    def __init__(self, x1, y1, width1=35, height1=35):
        orientation1 = random.choice(["horizontal", "vertical"])
        Settings.__init__(self, width=width1, height=height1, x=x1, y=y1, orientation=orientation1)
        self.load_image(self)
