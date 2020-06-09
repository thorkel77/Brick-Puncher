import pygame

class Square(pygame.sprite.Sprite):

    RESISTANCE = {
        1: pygame.image.load("Images/PNG/23-Breakout-Tiles.png"),
        2: pygame.image.load("Images/PNG/21-Breakout-Tiles.png"),
        3: pygame.image.load("Images/PNG/24-Breakout-Tiles.png")
    }

    def __init__(self, coup, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.coup = coup
        self.width = width
        self.height = height
        self.image = Square.RESISTANCE[self.coup].convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.width, self.height)

    def touche(self):
        self.coup -= 1

        if self.coup == 0:
            self.kill()
            return True
        else:
            self.image = Square.RESISTANCE[self.coup].convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            return False
