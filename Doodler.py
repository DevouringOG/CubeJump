from Platforms import *
from Sound import *


class Doodler(pg.sprite.Sprite):

    def __init__(self, x, y, all_sprites):
        super().__init__(all_sprites)
        self.image = pg.image.load('images/Doodler.png')
        self.left_image = self.image
        self.right_image = self.image = pg.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.falling = False
        self.rect.x = x
        self.rect.y = y
        self.jump_power = -15

    def update(self, platforms, monsters_group):
        self.rect.y += self.jump_power
        self.jump_power += GRAVITY
        #   Проверка на соприкосновение с монстрами и платформами
        for monster in monsters_group:
            if self.rect.colliderect(monster):
                if self.jump_power >= 0:
                    monster_sound.stop()
                    monster_jump_sound.play()
                    self.rect.bottom = monster.rect.top
                    self.jump_power = -15
                    monsters_group.remove(monster)
                else:
                    monster_sound.stop()
                    monster_crash_sound.play()
                    self.falling = True
                    self.jump_power = 15
                    monsters_group.remove(monster)
        if not self.falling:
            for platform in platforms:
                if self.rect.colliderect(platform) and self.jump_power > 0 and platform.rect.y - self.rect.y >= 39:
                    jump_sound.play()
                    self.rect.bottom = platform.rect.top
                    self.jump_power = -15
                    if platform.__class__ == BreakingPlatform:
                        breaking_platform_sound.play()
                        platform.crash = True
                        print(1)

    def move(self, keys):
        if keys[pg.K_RIGHT]:
            self.rect.x = (self.rect.x + 10 + WIDTH) % WIDTH
            self.image = self.right_image
        if keys[pg.K_LEFT]:
            self.rect.x = (self.rect.x - 10 + WIDTH) % WIDTH
            self.image = self.left_image

    def render(self, surface):
        surface.blit(self.image, self.rect)

    def restart(self):
        self.rect.x = (WIDTH - self.rect.width) // 2
        self.rect.y = HEIGHT - self.rect.height - 15
        self.jump_power = -15
