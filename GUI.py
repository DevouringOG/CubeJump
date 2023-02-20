from Config import *


class Button(pg.sprite.Sprite):
    FONT = pg.font.Font('fonts/minecraft-1-1.otf', 30)

    def __init__(self, position: tuple, text: str, event, gui_sprites,
                 base_image_filename='base_button.png', hover_image_filename='hover_button.png', lock=False):
        super().__init__(gui_sprites)

        self.event = event

        self.text = self.FONT.render(text, True, 'black')

        self.base_image = pg.image.load(f"images/buttons/{base_image_filename}")
        self.base_image.blit(self.text, ((self.base_image.get_width() - self.text.get_width()) // 2,
                                         (self.base_image.get_height() - self.text.get_height()) // 2))
        self.hover_image = pg.image.load(f"images/buttons/{hover_image_filename}")
        self.hover_image.blit(self.text, ((self.hover_image.get_width() - self.text.get_width()) // 2,
                                          (self.hover_image.get_height() - self.text.get_height()) // 2))

        if lock:
            lock_img = pg.image.load("images/buttons/lock.png")
            self.hover_image.blit(lock_img, (0, 0))
            self.base_image.blit(lock_img, (0, 0))

        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self, mouse_pos: tuple, mouse_click: bool):
        if self.rect.collidepoint(*mouse_pos):
            if mouse_click:
                pg.event.post(self.event)
            self.image = self.hover_image
        else:
            self.image = self.base_image


class SpinBox(pg.sprite.Sprite):

    def __init__(self, surface, position: tuple, default_value: int, min_value: int, max_value: int,
                 UP_EVENT, DOWN_EVENT, gui_sprites):
        super().__init__(gui_sprites)

        self.surface = surface

        self.up_event = UP_EVENT
        self.down_event = DOWN_EVENT

        self.pos = position

        self.max_value = max_value
        self.min_value = min_value

        self.spin_box_image = pg.image.load("Images/buttons/spin_box.png")
        self.up_image = pg.image.load("Images/buttons/spin_box_updown.png")
        self.hover_up_image = pg.image.load("Images/buttons/hover_spin_box_updown.png")
        self.down_image = pg.transform.flip(self.up_image, False, True)
        self.hover_down_image = pg.transform.flip(self.hover_up_image, False, True)

        self.rect = self.down_image.get_rect()
        self.rect2 = self.up_image.get_rect()

        self.rect.x = position[0]
        self.rect.y = position[1] + self.rect.height // 2

        self.up_pos = (position[0] + self.spin_box_image.get_width() + self.rect.width + self.rect.width // 2,
                       position[1] + self.rect.width // 2)
        surface.blit(self.up_image, self.up_pos)
        self.rect2.x = self.up_pos[0]
        self.rect2.y = self.up_pos[1]

        surface.blit(self.spin_box_image, (position[0] + self.rect.width + self.rect.width // 4, position[1]))
        self.value = default_value
        self.value_text = game_over_font.render(str(default_value), True, "black")
        surface.blit(self.value_text, (self.pos[0] + self.rect.width * 1.8, self.pos[1] + self.rect.height * 0.4))

    def update(self, mouse_pos: tuple, mouse_click: bool):
        if self.rect.collidepoint(*mouse_pos):
            if mouse_click and self.value > self.min_value:
                pg.event.post(self.down_event)
                self.value -= 1
            self.image = self.hover_up_image
        else:
            self.image = self.up_image

        if self.rect2.collidepoint(*mouse_pos):
            if mouse_click and self.value < self.max_value:
                pg.event.post(self.up_event)
                self.value += 1
            self.surface.blit(self.hover_up_image, self.up_pos)
        else:
            self.surface.blit(self.up_image, self.up_pos)
        self.value_text = game_over_font.render(str(self.value), True, "black")
        self.surface.blit(self.spin_box_image, (self.pos[0] + self.rect.width + self.rect.width // 4, self.pos[1]))
        self.surface.blit(self.value_text, (self.pos[0] + self.rect.width * 1.8, self.pos[1] + self.rect.height * 0.4))


class Switcher(pg.sprite.Sprite):

    def __init__(self, surface, position: tuple, ON_EVENT, OFF_EVENT, gui_sprites):
        super().__init__(gui_sprites)

        self.surface = surface
        self.position = position
        self.on_event = ON_EVENT
        self.off_event = OFF_EVENT
        self.switcher_position = (position[0] + 5, position[1] + 5)
        self.off = True

        self.image = pg.image.load("Images/buttons/switcher2.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.switcher_position[0]
        self.rect.y = self.switcher_position[1]

        self.switcher_image = pg.image.load("Images/buttons/switcher.png")
        surface.blit(self.switcher_image, self.position)

    def update(self, mouse_pos: tuple, mouse_click: bool):
        if self.rect.collidepoint(*mouse_pos):
            if mouse_click:
                if self.off:
                    pg.event.post(self.on_event)
                    self.surface.blit(self.switcher_image, self.position)
                    self.rect.x += self.image.get_width()
                    self.off = not self.off
                else:
                    pg.event.post(self.off_event)
                    self.surface.blit(self.switcher_image, self.position)
                    self.rect.x -= self.image.get_width()
                    self.off = not self.off
