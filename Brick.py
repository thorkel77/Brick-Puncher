import pygame
from random import randint
from Image import Image

BLACK = (0, 0, 0)

class Brick(pygame.sprite.Sprite):

    RESISTANCE = {
        1: pygame.image.load("Images/PNG/02-Breakout-Tiles.png"),
        2: pygame.image.load("Images/PNG/01-Breakout-Tiles.png"),
        3: pygame.image.load("Images/PNG/05-Breakout-Tiles.png")
    }



    BONUS = {
        1: pygame.image.load("Images/PNG/item_100.png"),
    }

    def __init__(self, coup, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.coup = coup
        self.width = width
        self.height = height
        self.image = Brick.RESISTANCE[self.coup].convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.width, self.height)
        self.rand_pouvoir = randint(1, 7)




    def touche(self):
        self.coup -= 1

        if self.coup == 0:
            self.kill()
            return True
        else:
            self.image = Brick.RESISTANCE[self.coup].convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            return False



