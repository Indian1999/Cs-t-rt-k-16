import pygame # terminálba: pip install pygame
import random
import os
import time
pygame.font.init()

class Game:
    WIDTH = 400
    HEIGHT = 500
    FPS = 60
    FRICTION = 0.15 # Ennyi százalékkal csökentjük a gyorsulást
    COIN_CHANCE = 0.3  # esély coin spawnolásra platform létrehozásakor
    ASSETS = os.path.join(os.path.dirname(__file__), "assets")
    BG_IMAGE = pygame.image.load(os.path.join(ASSETS, "background.png"))
    BG_IMAGE = pygame.transform.scale(BG_IMAGE, (WIDTH+40, HEIGHT+40))
    COIN_IMAGE = pygame.image.load(os.path.join(ASSETS, "coin.png"))
    PLATFORM_IMAGE = pygame.image.load(os.path.join(ASSETS, "platform.png"))
    PLAYER_IMAGE = pygame.image.load(os.path.join(ASSETS, "player.png"))


    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pygame.display.set_caption("Platformer Game")
        self.score = 0

    def draw_frame(self):
        #self.window.fill((200,200,200))
        self.window.blit(Game.BG_IMAGE, (-20,0))

        for sprite in self.all_sprites:
            self.window.blit(sprite.surf, sprite.rect)

        font = pygame.font.SysFont("Arial", 18)
        surf = font.render(f"Score: {self.score}", True, (0,0,0))
        self.window.blit(surf, (10, 10))

        pygame.display.update()

    def generate_platforms(self):
        while len(self.platforms) < 7:
            p = Platform(False, self.platforms)
            self.platforms.add(p)
            self.all_sprites.add(p)
            if random.random() < Game.COIN_CHANCE:
                x = p.rect.x + p.surf.get_width() // 2
                y = p.rect.y - 15
                coin = Coin(x, y)
                self.all_sprites.add(coin)
                self.coins.add(coin)

    def move_platforms(self):
        if self.player.rect.top <= Game.HEIGHT // 3:
            move_value = abs(self.player.vel.y)
            self.player.pos.y += move_value
            for platform in self.platforms:
                platform.rect.y += move_value
                if platform.rect.top >= Game.HEIGHT:
                    platform.kill()
                    self.score += 1
            for coin in self.coins:
                coin.rect.y += move_value
                if coin.rect.top >= Game.HEIGHT:
                    coin.kill()

    def check_death(self):
        if self.player.rect.top > Game.HEIGHT:
            pygame.quit()
            quit()

    def check_coin(self):
        hits = pygame.sprite.spritecollide(self.player, self.coins, dokill=True)
        self.score += 7 * len(hits)

    def run(self):
        self.player = Player()

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.main_platform = Platform()
        self.all_sprites.add(self.main_platform)
        self.platforms.add(self.main_platform)

        self.generate_platforms()

        while True:
            self.clock.tick(Game.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.move_platforms()
            self.generate_platforms()

            self.player.move(self.platforms)
            self.player.jump(self.platforms)

            self.check_coin()
            self.check_death()

            self.draw_frame()

class Player(pygame.sprite.Sprite):
    ACC = 0.5
    def __init__(self):
        super().__init__() # Sprite osztály konstruktora
        #self.surf = pygame.Surface((50, 50))
        #self.surf.fill((32,211,98))
        self.surf = pygame.transform.scale(Game.PLAYER_IMAGE, (50,50))
        self.rect = self.surf.get_rect(center=(Game.WIDTH//2, Game.HEIGHT-30))
        self.jumping = False

        self.pos = self.rect.bottomleft
        self.pos = pygame.Vector2(self.pos[0], self.pos[1])
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)

    def move(self, platforms):
        self.acc = pygame.Vector2(0, 0.98)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.acc.x = -Player.ACC
        if keys_pressed[pygame.K_RIGHT]:
            self.acc.x = Player.ACC

        self.acc.x -= self.vel.x * Game.FRICTION
        self.vel += self.acc
        self.pos += self.vel
        if self.pos.x + self.surf.get_width() < 0:
            self.pos.x = Game.WIDTH
        if self.pos.x > Game.WIDTH:
            self.pos.x =  -self.surf.get_width()

        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.pos.y = hits[0].rect.top
            self.vel.y = 0
            self.jumping = False

        self.rect.bottomleft = self.pos

    def jump(self, platforms):
        self.rect.bottom += 1
        hits = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.bottom -= 1
        keys_pressed = pygame.key.get_pressed()
        if hits and not self.jumping and keys_pressed[pygame.K_UP]:
            self.jumping = True
            self.vel.y = -22

class Platform(pygame.sprite.Sprite):
    def __init__(self, base_platform = True, platforms = pygame.sprite.Group()):
        super().__init__()
        if base_platform:
            self.surf = pygame.transform.scale(Game.PLATFORM_IMAGE, (Game.WIDTH, 20))
            self.rect = self.surf.get_rect(center=(Game.WIDTH//2, Game.HEIGHT-10))
        else:
            self.surf = pygame.transform.scale(Game.PLATFORM_IMAGE, (random.randint(50, 120), 20))
            pos = (random.randint(0, Game.WIDTH-20), random.randint(0, Game.HEIGHT-20))
            self.rect = self.surf.get_rect(center=pos)
            while pygame.sprite.spritecollide(self, platforms, False):
                pos = (random.randint(0, Game.WIDTH-20), random.randint(0, Game.HEIGHT-20))
                self.rect = self.surf.get_rect(center=pos)
            


class Coin(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.surf = pygame.transform.scale(Game.COIN_IMAGE, (30, 30))
        self.rect = self.surf.get_rect(center=(xpos, ypos))

game = Game()
game.run()