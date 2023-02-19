from Platforms import *
from Sound import *


class Doodler(pg.sprite.Sprite):

    def __init__(self, x, y, all_sprites):
        super().__init__(all_sprites)
        self.image = pg.image.load('images/Doodler.png')
        self.rect = self.image.get_rect()
        self.falling = 0
        self.rect.x = x
        self.rect.y = y
        self.jump_power = -15

    def update(self, platforms, monsters_group):
        self.rect.y += self.jump_power
        self.jump_power += GRAVITY
        for monster in monsters_group:
            if self.rect.colliderect(monster):
                if self.jump_power >= 0 and monster.rect.y - self.rect.y >= 54:
                    self.rect.bottom = monster.rect.top
                    self.jump_power = -15
                    monsters_group.remove(monster)
                else:
                    self.falling = True
                    self.jump_power = 15
                    monsters_group.remove(monster)
        if not self.falling:
          for platform in platforms:
              if self.rect.colliderect(platform) and self.jump_power > 0 and platform.rect.y - self.rect.y >= 69:
                  jump_sound.play()
                  self.rect.bottom = platform.rect.top
                  self.jump_power = -15
                  if platform.__class__ == BreakingPlatform:
                      breaking_platform_sound.play()
                      platform.crash = True
                  elif platform.__class__ == TeleportingPlatform:
                      platform.teleport()

    def move(self, keys):
        if keys[pg.K_RIGHT]:
            self.rect.x = (self.rect.x + 10 + WIDTH) % WIDTH
        if keys[pg.K_LEFT]:
            self.rect.x = (self.rect.x - 10 + WIDTH) % WIDTH

    def render(self, surface):
        surface.blit(self.image, self.rect)

    def get_position(self):
        return self.rect.x, self.rect.y

    def restart(self):
        self.rect.x = WIDTH // 2 - 50
        self.rect.y = HEIGHT - 50
        self.jump_power = -15
