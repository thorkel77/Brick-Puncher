import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/50-Breakout-Tiles.png").convert_alpha()
        #self.image = pygame.image.load("Images/PNG/50-Breakout-Tiles.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (x,y))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move_left(self):
        self.rect.x -= 25

    def move_right(self):
        self.rect.x += 25

    def leaves_screen_sides(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 700:
            self.rect.x = 700

    def reinitialiser_position(self):
        self.rect.x = 350
        self.rect.y = 560
