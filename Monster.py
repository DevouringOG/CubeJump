from Config import *
import random


class Monster(pg.sprite.Sprite):
    def __init__(self, sheet, columns, rows, all_sprites):
        super().__init__(all_sprites)
        self.frames = []
        self.cur_frame = 0
        self.cut_sheet(sheet, columns, rows)
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = WIDTH // 2, 0
        self.velocity = 10
        self.frames_fps = 0

    def move(self):
        self.frames_fps += 1
        self.rect.x += self.velocity
        if self.rect.x >= WIDTH - 100:
            self.velocity *= -1
        elif self.rect.x <= 10:
            self.velocity *= -1

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
