from Config import *
from Sound import monster_sound



class Monster(pg.sprite.Sprite):  # Спрайт-класс монстра, родитель для красного и чёрного монстров
    def __init__(self, sheet, columns, rows, all_sprites):
        super().__init__(all_sprites)
        self.frames = []
        self.cur_frame = 0
        self.cut_sheet(sheet, columns, rows)
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = WIDTH // 2 + self.rect.x, -10
        self.velocity = 5
        self.frames_fps = 0

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pg.Rect(0, 0, sheet.get_width() // columns,
                            sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pg.Rect(
                    frame_location, self.rect.size)))

    def change_frame(self):
        if self.frames_fps >= 5:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.frames_fps = 0


class BlackMonster(Monster):  # Монстр, двигающийся вдоль оси X
    def __init__(self, sheet, columns, rows, all_sprites):
        super(BlackMonster, self).__init__(sheet, columns, rows, all_sprites)

    def move(self):
        self.frames_fps += 1
        self.rect.x += self.velocity
        if self.rect.x >= WIDTH - 100:
            self.velocity *= -1
        elif self.rect.x <= 10:
            self.velocity *= -1
        if self.rect.y > HEIGHT:
            self.kill()
            monster_sound.stop()



class RedMonster(Monster):  # Монстр, двигающийся вдоль оси Y
    def __init__(self, sheet, columns, rows, all_sprites):
        super(RedMonster, self).__init__(sheet, columns, rows, all_sprites)

    def move(self):
        self.frames_fps += 1
        self.rect.y += self.velocity
        if self.rect.y > HEIGHT:
            self.kill()
            monster_sound.stop()
