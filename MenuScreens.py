from GUI import *


def start_screen(surface):
    background = pg.image.load("images/menu_background.png")
    surface.blit(background, (0, 0))

    logo = logo_font.render("CUBEJUMP", True, (0, 0, 0))
    surface.blit(logo, ((WIDTH - logo.get_width()) // 2, 200))

    gui_sprites = pg.sprite.Group()
    Button(((WIDTH - 300) // 2, 450), "start", START_BUTTON_EVENT, gui_sprites)
    Button(((WIDTH - 300) // 2, 550), "settings", SETTING_BUTTON_EVENT, gui_sprites)
    Button(((WIDTH - 300) // 2, 650), "about", ABOUT_BUTTON_EVENT, gui_sprites)

    while True:
        surface.blit(background, (0, 0))
        surface.blit(logo, ((WIDTH - logo.get_width()) // 2, 200))
        mouse_click = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONUP:
                mouse_click = True
                print(1)
            if event.type == START_BUTTON_EVENT.type:
                level = levels_menu(surface)
                if level:
                    return level
            if event.type == SETTING_BUTTON_EVENT.type:
                settings_menu(surface)
                surface.blit(background, (0, 0))
                surface.blit(logo, ((WIDTH - logo.get_width()) // 2, 200))
            if event.type == ABOUT_BUTTON_EVENT.type:
                about(surface)
        gui_sprites.update(pg.mouse.get_pos(), mouse_click)
        gui_sprites.draw(surface)
        pg.display.update()


def levels_menu(surface):
    background = pg.image.load("images/levels_background.png")
    surface.blit(background, (0, 0))

    logo = logo_font.render("LEVELS", True, (0, 0, 0))
    surface.blit(logo, ((WIDTH - logo.get_width()) // 2, 200))

    gui_sprites = pg.sprite.Group()
    Button((25, 400), "1", LEVEL1_BUTTON_EVENT, gui_sprites, base_image_filename="1level.png",
           hover_image_filename="1level_hover.png")
    Button((220, 400), "2", LEVEL2_BUTTON_EVENT, gui_sprites, base_image_filename="2level.png",
           hover_image_filename="2level_hover.png", lock=True if 2 not in available_levels else False)
    Button((415, 400), "3", LEVEL3_BUTTON_EVENT, gui_sprites, base_image_filename="3level.png",
           hover_image_filename="3level_hover.png", lock=True if 3 not in available_levels else False)
    Button((20, 20), "back", BACK_BUTTON_EVENT, gui_sprites, base_image_filename="back_button.png",
           hover_image_filename="hover_back_button.png")

    while True:
        mouse_click = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONUP:
                mouse_click = True
            if event.type == LEVEL1_BUTTON_EVENT.type:
                return 1
            if event.type == LEVEL2_BUTTON_EVENT.type:
                if 2 in available_levels:
                    return 2
            if event.type == LEVEL3_BUTTON_EVENT.type:
                if 3 in available_levels:
                    return 3
            if event.type == BACK_BUTTON_EVENT.type:
                return 0

        gui_sprites.update(pg.mouse.get_pos(), mouse_click)
        gui_sprites.draw(surface)
        pg.display.update()


def settings_menu(surface):
    background = pg.image.load("images/setting_background.png")
    surface.blit(background, (0, 0))

    logo = logo_font.render("SETTINGS", True, (0, 0, 0))
    surface.blit(logo, ((WIDTH - logo.get_width()) // 2, 200))

    volume_text = font.render("volume", True, "black")
    surface.blit(volume_text, (50, 430))

    gui_sprites = pg.sprite.Group()
    Button((20, 20), "back", BACK_BUTTON_EVENT, gui_sprites, base_image_filename="back_button.png",
           hover_image_filename="hover_back_button.png")

    SpinBox(surface, (220, 400), 1, 1, 5, UP_SOUND_VALUE_EVENT, DOWN_SOUND_VALUE_EVENT, gui_sprites)

    while True:
        mouse_click = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONUP:
                mouse_click = True
            if event.type == UP_SOUND_VALUE_EVENT.type:
                print("UP")
            if event.type == DOWN_SOUND_VALUE_EVENT.type:
                print("DOWN")
            if event.type == BACK_BUTTON_EVENT.type:
                return

        gui_sprites.update(pg.mouse.get_pos(), mouse_click)
        gui_sprites.draw(surface)
        pg.display.update()


def about(surface):
    background = pg.image.load("images/about.png")
    surface.blit(background, (50, 400))

    gui_sprites = pg.sprite.Group()
    Button((55, 405), "", BACK_BUTTON_EVENT, gui_sprites, base_image_filename="about_back_button.png",
           hover_image_filename="hover_about_back_button.png")

    about_text = [(about_font.render("The main goal of the game is to", True, "black"), (80, 500)),
                  (about_font.render("get as high as possible on the", True, "black"), (80, 530)),
                  (about_font.render("platforms and score as many", True, "black"), (80, 560)),
                  (about_font.render("points as possible. The hero", True, "black"), (80, 590)),
                  (about_font.render("controlled using two buttons", True, "black"), (80, 620)),
                  (about_font.render("(left, right)", True, "black"), (80, 650)),
                  (font.render("ABOUT", True, "black"), (232, 445))]
    for i in about_text:
        print(i[0].get_width())
        surface.blit(i[0], (i[1][0], i[1][1]))

    while True:
        mouse_click = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONUP:
                mouse_click = True
            if event.type == BACK_BUTTON_EVENT.type:
                return

        gui_sprites.update(pg.mouse.get_pos(), mouse_click)
        gui_sprites.draw(surface)
        pg.display.update()
