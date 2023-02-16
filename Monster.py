from Config import *
import random


class Monster(pg.sprite.Sprite):
    def __init__(self, all_sprites):
        super().__init__(all_sprites)
        self.image = pg.transform.scale(pg.image.load("images/enemy.png"), (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = WIDTH // 2, 0
        self.velocity = 10

    def move(self):
        self.rect.x += self.velocity
        if self.rect.x >= WIDTH - 10:
            self.velocity *= -1
        elif self.rect.x <= 10:
            self.velocity *= -1
