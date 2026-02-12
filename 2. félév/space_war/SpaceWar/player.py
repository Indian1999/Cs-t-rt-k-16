import pygame
from .bullet import Bullet

class Player:
    def __init__(self, pos, size, surf, dire, color, shoot_sound, damage_sound):
        self.image = pygame.transform.scale(surf, (size[0], size[1]))
        self.image = pygame.transform.rotate(self.image, -dire*90)
        self.dire = dire
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.color = color
        self.health = 10
        self.max_bullets = 3
        self.bullets = []
        self.shoot_sound = shoot_sound
        self.damage_sound = damage_sound

    def take_damage(self):
        self.health -= 1
        self.damage_sound.play()

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def shoot(self):
        if len(self.bullets) >= self.max_bullets:
            return
        self.shoot_sound.play()
        if self.dire == 1:
            start_x = self.rect.x + self.rect.width
        else:
            start_x = self.rect.x - 10
        start_y = self.rect.y + self.rect.height // 2
        self.bullets.append(Bullet((start_x, start_y), self.dire, self.color))
    