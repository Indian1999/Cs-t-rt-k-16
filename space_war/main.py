import pygame # pip install pygame (terminálban)
import random
import os
pygame.font.init()

class Bullet:
    def __init__(self, pos, dire, color):
        self.rect = pygame.Rect(pos[0], pos[1]-2, 10, 4)
        self.dire = dire
        self.color = color

    def move(self, velocity):
        self.rect.x += velocity * self.dire

class Player:
    def __init__(self, pos, size, surf, dire, color):
        self.image = pygame.transform.scale(surf, (size[0], size[1]))
        self.image = pygame.transform.rotate(self.image, -dire*90)
        self.dire = dire
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.color = color
        self.health = 1
        self.max_bullets = 3
        self.bullets = []

    def take_damage(self):
        self.health -= 1

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def shoot(self):
        if len(self.bullets) >= self.max_bullets:
            return
        if self.dire == 1:
            start_x = self.rect.x + self.rect.width
        else:
            start_x = self.rect.x - 10
        start_y = self.rect.y + self.rect.height // 2
        self.bullets.append(Bullet((start_x, start_y), self.dire, self.color))

        
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
        if keys_pressed[pygame.K_w] and self.red.rect.y > 0:
            self.red.move(0, -5)
        if keys_pressed[pygame.K_s] and self.red.rect.y < self.HEIGHT - self.SPACESHIP_HEIGHT:
            self.red.move(0, 5)
        if keys_pressed[pygame.K_d] and self.red.rect.x < self.WIDTH // 2 - self.SPACESHIP_WIDTH:
            self.red.move(5, 0)
        if keys_pressed[pygame.K_a] and self.red.rect.x > 0:
            self.red.move(-5, 0)
        if keys_pressed[pygame.K_UP] and self.yellow.rect.y > 0:
            self.yellow.move(0, -5)
        if keys_pressed[pygame.K_DOWN] and self.yellow.rect.y < self.HEIGHT - self.SPACESHIP_HEIGHT:
            self.yellow.move(0, 5)
        if keys_pressed[pygame.K_RIGHT] and self.yellow.rect.x < self.WIDTH - self.SPACESHIP_WIDTH:
            self.yellow.move(5, 0)
        if keys_pressed[pygame.K_LEFT] and self.yellow.rect.x > self.WIDTH // 2:
            self.yellow.move(-5, 0)

        for bullet in self.red.bullets:
            bullet.move(8)
            if bullet and (bullet.rect.x < - 10 or bullet.rect.x > self.WIDTH + 10):
                self.red.bullets.remove(bullet)
            if bullet.rect.colliderect(self.yellow.rect):
                self.yellow.take_damage()
                self.red.bullets.remove(bullet)

        for bullet in self.yellow.bullets:
            bullet.move(8)
            if bullet and (bullet.rect.x < - 10 or bullet.rect.x > self.WIDTH + 10):
                self.yellow.bullets.remove(bullet)
            if bullet.rect.colliderect(self.red.rect):
                self.red.take_damage()
                self.yellow.bullets.remove(bullet)
    
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    self.red.shoot()
                if event.key == pygame.K_RCTRL:
                    self.yellow.shoot()

    def draw_frame(self):
        # Háttérkép
        self.window.blit(self.BACKGROUND, (0,0))

        # Határvonal
        border = pygame.Rect(self.WIDTH//2 - 5, 0, 10, self.HEIGHT)
        pygame.draw.rect(self.window, (0, 0, 0), border)

        # Játékosok
        self.window.blit(self.red.image, (self.red.rect.x, self.red.rect.y))
        self.window.blit(self.yellow.image, (self.yellow.rect.x, self.yellow.rect.y))

        # Lövedékek
        for bullet in self.red.bullets + self.yellow.bullets:
            pygame.draw.rect(self.window, bullet.color, bullet.rect)

        # UI elemek:
        health_font = pygame.font.SysFont("Arial", self.WIDTH // 25)
        red_health_text = health_font.render(f"Health: {self.red.health}", True, (255,255,255))
        yellow_health_text = health_font.render(f"Health: {self.yellow.health}", True, (255,255,255))
        self.window.blit(red_health_text, (10, 10))
        self.window.blit(yellow_health_text, (self.WIDTH - yellow_health_text.get_width() - 10, 10))

        pygame.display.update()

    def draw_winner(self, text):
        winner_font = pygame.font.SysFont("Arial", self.WIDTH // 10)
        winner_surface = winner_font.render(text, True, (255,255,255))
        self.window.blit(winner_surface, 
                         (self.WIDTH//2 - winner_surface.get_width() // 2, 
                          self.HEIGHT//2 - winner_surface.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(5000)
    
    def run(self):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Space Wars!")

        self.red = Player(pos=(50, self.HEIGHT//2 - self.SPACESHIP_HEIGHT//2),
                          size=(self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT),
                          surf=self.RED_SPACESHIP, dire = 1, color = (255, 0, 0))
        
        
        self.yellow = Player(pos=(self.WIDTH - 50 - self.SPACESHIP_WIDTH, self.HEIGHT//2 - self.SPACESHIP_HEIGHT//2),
                          size=(self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT),
                          surf=self.YELLOW_SPACESHIP, dire = -1, color = (255, 255, 0))

        self.clock = pygame.time.Clock()
        self.gameOn = True

        while self.gameOn:
            self.clock.tick(self.FPS) # 1/60-ad másodpercenként fut a ciklus
            self.handle_events()
            keys_pressed = pygame.key.get_pressed()
            self.handle_movement(keys_pressed)

            self.draw_frame()
            if self.red.health <= 0:
                self.draw_winner("Yellow Wins!")
                self.gameOn = False
            if self.yellow.health <= 0:
                self.draw_winner("Red Wins!")
                self.gameOn = False

game = Game()
game.run()