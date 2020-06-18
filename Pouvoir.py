import pygame
from random import randint

class Pouvoir(pygame.sprite.Sprite):

    TYPE_POUVOIR = {
       
        1: pygame.image.load("Images/PNG/itemfast.png"),
        2: pygame.image.load("Images/PNG/itemslow.png"),
        3: pygame.image.load("Images/PNG/itemlaser.png"),
        4: pygame.image.load("Images/PNG/item_100.png")
    }

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        rand = randint(1, 10)
        self.rand_pouvoir = randint(1, 4)
        self.width = 60
        self.height = 30
        self.image = Pouvoir.TYPE_POUVOIR[self.rand_pouvoir].convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.width, self.height)

   
    def accelerer(self, ball):
        ball.vitesse = 12

    def ralenti(self, ball):
        ball.vitesse = 4

    def laser(self, paddle):
        paddle.image = pygame.image.load("Images/paddle2.png").convert_alpha()
        paddle.image = pygame.transform.scale(paddle.image, (100, 20))

