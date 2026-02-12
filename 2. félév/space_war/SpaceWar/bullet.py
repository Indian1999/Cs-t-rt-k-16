import pygame

class Bullet:
    def __init__(self, pos, dire, color):
        self.rect = pygame.Rect(pos[0], pos[1]-2, 10, 4)
        self.dire = dire
        self.color = color

    def move(self, velocity):
        self.rect.x += velocity * self.dire
