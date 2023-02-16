from Config import *
from GUI import Button


def start_screen(surface):
    background = pg.image.load("images/menu_background.png")
    surface.blit(background,  (0, 0))

    logo = logo_font.render("CUBEJUMP", True, (0, 0, 0))
    surface.blit(logo, ((WIDTH - logo.get_width()) // 2, 200))

    gui_sprites = pg.sprite.Group()
    start_button = Button(((WIDTH - 300) // 2, 450), "start", START_BUTTON_EVENT, gui_sprites)
    settings_button = Button(((WIDTH - 300) // 2, 550), "settings", SETTING_BUTTON_EVENT, gui_sprites)
    about_button = Button(((WIDTH - 300) // 2, 650), "about", ABOUT_BUTTON_EVENT, gui_sprites)

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
    level1_button = Button((25, 400), "1", LEVEL1_BUTTON_EVENT, gui_sprites, base_image_filename="1level.png",
                           hover_image_filename="1level_hover.png")
    level2_button = Button((220, 400), "2", LEVEL2_BUTTON_EVENT, gui_sprites, base_image_filename="2level.png",
                           hover_image_filename="2level_hover.png", lock=True if 2 not in available_levels else False)
    level3_button = Button((415, 400), "3", LEVEL3_BUTTON_EVENT, gui_sprites, base_image_filename="3level.png",
                           hover_image_filename="3level_hover.png", lock=True if 3 not in available_levels else False)
    back_button = Button((20, 20), "back", BACK_BUTTON_EVENT, gui_sprites, base_image_filename="back_button.png",
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

    logo = logo_font.render("SETTINS", True, (0, 0, 0))
    surface.blit(logo, ((WIDTH - logo.get_width()) // 2, 200))

    gui_sprites = pg.sprite.Group()
    back_button = Button((20, 20), "back", BACK_BUTTON_EVENT, gui_sprites, base_image_filename="back_button.png",
                         hover_image_filename="hover_back_button.png")

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


def about(surface):
    background = pg.image.load("images/about.png")
    surface.blit(background, (50, 400))

    gui_sprites = pg.sprite.Group()
    back_button = Button((55, 405), "", BACK_BUTTON_EVENT, gui_sprites, base_image_filename="about_back_button.png",
                         hover_image_filename="hover_about_back_button.png")

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
