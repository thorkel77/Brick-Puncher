import pygame

class Image(pygame.sprite.Sprite):
    def __init__(self,image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (x,y))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

  