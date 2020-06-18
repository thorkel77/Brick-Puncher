import pygame
from random import randint

class Ball(pygame.sprite.Sprite):


    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.direction_x = 1
        self.direction_y = 1
        self.vitesse = 8
        #self.image = pygame.image.load("Images/PNG/58-Breakout-Tiles.png").convert_alpha()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (x,y))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #self.velocity = [randint(4, 8), randint(-8, 8)]
        #self.velocity = [randint(4, 8), randint(-8, 8)]

    def flip_direction_x(self):
        self.direction_x *= -1

    def flip_direction_y(self):
        self.direction_y *= -1

    def flip_random(self):
        rand = randint(0, 1)
        if rand == 1:
            self.flip_direction_x()
        else:
            self.flip_direction_y()

    def leaves_screen(self):
        if self.rect.x < 0 or self.rect.x > 790:
            self.flip_direction_x()
            
        if self.rect.y < 60:
            self.flip_direction_y()
           

        #return self.rect.y > 600

    def lose(self):
        if self.rect.y > 580:
            return True

    # def update(self):
    #     self.rect.x += self.velocity[0]
    #     self.rect.y += self.velocity[1]
    #
    # def bounce(self):
    #     self.velocity[0] = -self.velocity[0]
    #     self.velocity[1] = randint(-8, 8)

    def move(self):
        self.rect.x += self.vitesse * self.direction_x
        self.rect.y += self.vitesse * self.direction_y

    def reinitialiser_position(self):
        self.rect.x = 350
        self.rect.y = 200