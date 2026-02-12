import pygame
import random

class Meteor:
    def __init__(self, window, surf, size):
        self.window = window
        self.image = surf
        self.rect = pygame.Rect(0, 0, size, size)
        self.x = 0
        self.y = 0
        self.setup()

    def setup(self):
        self.velocity = random.randint(2, 6)
        area = random.randint(1, 4)
        if area == 1:
            self.x = random.randint(-200, self.window.get_width() + 200)
            self.y = random.randint(-150, -50)
        elif area == 2:
            self.x = random.randint(-200, self.window.get_width() + 200)
            self.y = self.window.get_height() + random.randint(50, 150)
        elif area == 3:
            self.x = random.randint(-200, -50)
            self.y = random.randint(0, self.window.get_height())
        else:
            self.x = self.window.get_width() + random.randint(50, 200)
            self.y = random.randint(0, self.window.get_height())
        self.rect.x = self.x
        self.rect.y = self.y
        goal_x = random.randint(50, self.window.get_width() - 50)
        goal_y = random.randint(50, self.window.get_height() - 50)
        distance = ((self.x - goal_x) ** 2 + (self.y - goal_y)**2) ** 0.5
        self.dire = ((goal_x - self.x)/distance, (goal_y - self.y)/distance)

    def move(self):
        self.x += self.velocity * self.dire[0]
        self.y += self.velocity * self.dire[1]
        self.rect.x = self.x
        self.rect.y = self.y
        if self.x > self.window.get_width() + 200 or self.x < -200 or self.y < -200 or self.y > self.window.get_height()+200:
            self.setup()
