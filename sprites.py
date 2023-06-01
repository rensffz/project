import pygame

class Sprite:
    def __init__(self, sprite):
        self.sprite = pygame.image.load(sprite)
        self.w = self.sprite.get_width()
        self.h = self.sprite.get_height()
