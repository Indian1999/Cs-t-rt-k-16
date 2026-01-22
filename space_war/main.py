import pygame # pip install pygame (terminálban)
import random
import os

class Player:
    def __init__(self, pos, size, surf, dire):
        self.image = pygame.transform.scale(surf, (size[0], size[1]))
        self.image = pygame.transform.rotate(self.image, -dire*90)
        self.dire = dire
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

        
class Game:
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 500
        self.SPACESHIP_WIDTH = self.WIDTH // 11
        self.SPACESHIP_HEIGHT = self.HEIGHT // 7
        self.FPS = 60
        self.ASSETS = os.path.join(os.path.dirname(__file__), "assets")
        self.load_assets()

    def handle_movement(self, keys_pressed):
        if keys_pressed[pygame.K_w]:
            self.red.move(0, -5)
        if keys_pressed[pygame.K_s]:
            self.red.move(0, 5)
        if keys_pressed[pygame.K_d]:
            self.red.move(5, 0)
        if keys_pressed[pygame.K_a]:
            self.red.move(-5, 0)
        if keys_pressed[pygame.K_UP]:
            self.yellow.move(0, -5)
        if keys_pressed[pygame.K_DOWN]:
            self.yellow.move(0, 5)
        if keys_pressed[pygame.K_RIGHT]:
            self.yellow.move(5, 0)
        if keys_pressed[pygame.K_LEFT]:
            self.yellow.move(-5, 0)
    
    def load_assets(self):
        self.BACKGROUND = pygame.image.load(os.path.join(self.ASSETS, "space.png"))
        self.BACKGROUND = pygame.transform.scale(self.BACKGROUND, (self.WIDTH, self.HEIGHT))
        
        self.RED_SPACESHIP = pygame.image.load(os.path.join(self.ASSETS, "spaceship_red.png"))
        self.YELLOW_SPACESHIP = pygame.image.load(os.path.join(self.ASSETS, "spaceship_yellow.png"))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameOn = False
                pygame.quit()
                exit()

    def draw_frame(self):
        self.window.blit(self.BACKGROUND, (0,0))
        self.window.blit(self.red.image, (self.red.rect.x, self.red.rect.y))
        self.window.blit(self.yellow.image, (self.yellow.rect.x, self.yellow.rect.y))

        pygame.display.update()

    def run(self):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Space Wars!")

        self.red = Player(pos=(50, self.HEIGHT//2 - self.SPACESHIP_HEIGHT//2),
                          size=(self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT),
                          surf=self.RED_SPACESHIP, dire = 1)
        
        
        self.yellow = Player(pos=(self.WIDTH - 50 - self.SPACESHIP_WIDTH, self.HEIGHT//2 - self.SPACESHIP_HEIGHT//2),
                          size=(self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT),
                          surf=self.YELLOW_SPACESHIP, dire = -1)

        self.clock = pygame.time.Clock()
        self.gameOn = True

        while self.gameOn:
            self.clock.tick(self.FPS) # 1/60-ad másodpercenként fut a ciklus
            self.handle_events()
            keys_pressed = pygame.key.get_pressed()
            self.handle_movement(keys_pressed)

            self.draw_frame()

game = Game()
game.run()