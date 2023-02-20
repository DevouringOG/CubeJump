import random
from Config import *


class Platform(pg.sprite.Sprite):

    def __init__(self, x, y, all_sprites):
        super().__init__(all_sprites)
        self.image = pg.image.load("images/base_platform.png")
        self.rect = self.image.get_rect()  # 85, 15
        self.start = y
        self.rect.x = x
        self.rect.y = y

    def render(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        #   если платформа ниже окна то она восстанавливается
        if self.rect.y >= HEIGHT - 10:
            self.rect.y = self.rect.y - HEIGHT
            self.rect.x = random.randrange(0, WIDTH - 85)

    def restart(self):
        self.rect.x = random.randrange(0, WIDTH - 85)
        self.rect.y = self.start


class HorizontalPlatform(Platform):

    def __init__(self, x, y, all_sprites):
        super().__init__(x, y, all_sprites)
        self.image = pg.image.load("images/horizontal_platform.png")
        self.speed = 5

    def update(self):
        if self.rect.y >= HEIGHT - 10:
            self.rect.y = self.rect.y - HEIGHT
            self.rect.x = random.randrange(0, WIDTH - 85)
        self.rect.x += self.speed
        if self.rect.right > WIDTH:
            self.speed = -5
        elif self.rect.x < 0:
            self.speed = 5


class BreakingPlatform(Platform):

    def __init__(self, x, y, all_sprites):
        super().__init__(x, y, all_sprites)
        self.image = pg.image.load("images/breaking_platform.png")
        self.crash = False
        self.start_y = y

    def update(self):
        if self.rect.y >= HEIGHT - 10:
            self.crash = False
            self.rect.y = self.rect.y - HEIGHT
            self.rect.x = random.randrange(0, WIDTH - 85)
        if self.crash:
            self.crash = False
            self.rect.y = self.rect.y - HEIGHT
            self.rect.x = random.randrange(0, WIDTH - 85)
