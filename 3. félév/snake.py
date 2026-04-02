import pygame # pip install pygame (terminálba)
import random

class Food:
    def __init__(self, xlim, ylim, pixel_size):
        self.xlim = xlim
        self.ylim = ylim
        self.pixel_size = pixel_size
        self.random_pos()

    def random_pos(self):
        self.x = random.randint(0, self.xlim-self.pixel_size) // self.pixel_size * self.pixel_size
        self.y = random.randint(0, self.ylim-self.pixel_size) // self.pixel_size * self.pixel_size

    def draw(self, window, color):
        pygame.draw.rect(window, color, pygame.Rect(self.x, self.y, self.pixel_size, self.pixel_size))

class Snake:
    def __init__(self, x, y, speed, xlim, ylim):
        self.x = x
        self.y = y
        self.speed = speed
        self.xlim = xlim
        self.ylim = ylim
        self.length = 1
        self.x_vel = 0
        self.y_vel = 0
        self.body = [(self.x, self.y)] # (5, 6)
        self.is_dead = False

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop(0)
        self.is_dead = (self.x, self.y) in self.body[:-1]
        if self.x >= self.xlim or self.y >= self.ylim:
            self.is_dead = True

    def set_direction(self, dire):
        if dire == "right" and self.x_vel != -self.speed:
            self.x_vel = self.speed
            self.y_vel = 0
        elif dire == "left" and self.x_vel != self.speed:
            self.x_vel = -self.speed
            self.y_vel = 0
        elif dire == "up" and self.y_vel != self.speed:
            self.x_vel = 0
            self.y_vel = -self.speed
        elif dire == "down" and self.y_vel != -self.speed:
            self.x_vel = 0
            self.y_vel = self.speed

    def draw(self, window, color):
        for pixel in self.body:
            pygame.draw.rect(window, color, pygame.Rect(pixel[0], pixel[1], self.speed, self.speed))

    def is_touching(self, food):
        if food.x == self.x and food.y == self.y:
            self.length += 1
            food.random_pos()


class SnakeGame:
    BACKGROUND_COLOR = (123, 87, 200)
    SNAKE_COLOR = (10, 10, 10)
    FOOD_COLOR = (14, 231, 27)

    def __init__(self, rows = 12, cols = 15, pixel_size = 30, fps = 10):
        self.rows = rows
        self.cols = cols
        self.pixel_size = pixel_size
        self.fps = fps
        self.WIDTH = cols * pixel_size
        self.HEIGHT = rows * pixel_size
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

    def draw_frame(self):
        self.window.fill(SnakeGame.BACKGROUND_COLOR)

        self.snake.draw(self.window, SnakeGame.SNAKE_COLOR)
        self.food.draw(self.window, SnakeGame.FOOD_COLOR)

        pygame.display.update()

    def run(self):
        game_over = False
        app_close = False

        self.snake = Snake(
            x = round(self.WIDTH // 2 / self.pixel_size) * self.pixel_size,
            y = round(self.HEIGHT // 2 / self.pixel_size) * self.pixel_size,
            speed = self.pixel_size,
            xlim = self.WIDTH,
            ylim = self.HEIGHT
        )

        self.food = Food(self.WIDTH, self.HEIGHT, self.pixel_size)

        while not app_close:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    app_close = True
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.set_direction("left")
                    if event.key == pygame.K_RIGHT:
                        self.snake.set_direction("right")
                    if event.key == pygame.K_UP:
                        self.snake.set_direction("up")
                    if event.key == pygame.K_DOWN:
                        self.snake.set_direction("down")
            
            self.snake.move()

            if self.snake.is_dead:
                game_over = True
                continue

            self.snake.is_touching(self.food)

            self.draw_frame()

game = SnakeGame()
game.run()