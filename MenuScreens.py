from GUI import *
import csv
from Sound import *


def start_screen(surface, levels_screen=False):
    if levels_screen:
        level = levels_menu(surface)
        if level:
            return level
    background = pg.image.load("images/menu_background.png")
    surface.blit(background, (0, 0))

    logo = logo_font.render("CUBEJUMP", True, (0, 0, 0))
    surface.blit(logo, ((WIDTH - logo.get_width()) // 2, 200))

    gui_sprites = pg.sprite.Group()
    #   Создание кнопок
    Button(((WIDTH - 300) // 2, 450), "start", START_BUTTON_EVENT, gui_sprites)
    Button(((WIDTH - 300) // 2, 550), "settings", SETTING_BUTTON_EVENT, gui_sprites)
    Button(((WIDTH - 300) // 2, 650), "about", ABOUT_BUTTON_EVENT, gui_sprites)
    Button(((WIDTH - 300) // 2, 750), "records", RECORDS_BUTTON_EVENT, gui_sprites)

    while True:
        mouse_click = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONUP:
                mouse_click = True

            if event.type == START_BUTTON_EVENT.type:
                button_sound.play()
                level = levels_menu(surface)
                if level:
                    return level
            if event.type == SETTING_BUTTON_EVENT.type:
                button_sound.play()
                settings_menu(surface)
                surface.blit(background, (0, 0))
                surface.blit(logo, ((WIDTH - logo.get_width()) // 2, 200))
            if event.type == ABOUT_BUTTON_EVENT.type:
                button_sound.play()
                about(surface)
            if event.type == RECORDS_BUTTON_EVENT.type:
                records(surface)

        surface.blit(background, (0, 0))
        surface.blit(logo, ((WIDTH - logo.get_width()) // 2, 200))
        gui_sprites.update(pg.mouse.get_pos(), mouse_click)
        gui_sprites.draw(surface)
        pg.display.update()


def levels_menu(surface):
    background = pg.image.load("images/levels_background.png")
    surface.blit(background, (0, 0))

    logo = logo_font.render("LEVELS", True, (0, 0, 0))
    surface.blit(logo, ((WIDTH - logo.get_width()) // 2, 200))

    gui_sprites = pg.sprite.Group()
    #   Создание кнопок
    Button((25, 400), "1", LEVEL1_BUTTON_EVENT, gui_sprites, base_image_filename="1level.png",
           hover_image_filename="1level_hover.png")
    Button((220, 400), "2", LEVEL2_BUTTON_EVENT, gui_sprites, base_image_filename="2level.png",
           hover_image_filename="2level_hover.png", lock=True if 2 not in available_levels else False)
    Button((415, 400), "3", LEVEL3_BUTTON_EVENT, gui_sprites, base_image_filename="3level.png",
           hover_image_filename="3level_hover.png", lock=True if 3 not in available_levels else False)
    Button((150, 600), "FREE MODE", FREE_LEVEL_BUTTON_EVENT, gui_sprites)
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
                button_sound.play()
                return 1
            if event.type == LEVEL2_BUTTON_EVENT.type:
                button_sound.play()
                if 2 in available_levels:
                    return 2
            if event.type == LEVEL3_BUTTON_EVENT.type:
                button_sound.play()
                if 3 in available_levels:
                    return 3
            if event.type == FREE_LEVEL_BUTTON_EVENT.type:
                return 4
            if event.type == BACK_BUTTON_EVENT.type:
                button_sound.play()
                return 0

        gui_sprites.update(pg.mouse.get_pos(), mouse_click)
        gui_sprites.draw(surface)
        pg.display.update()


def settings_menu(surface):
    global volume, volume_is_on

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

    Switcher(surface, (50, 500), ON_EVENT, OFF_EVENT, gui_sprites)

    while True:
        mouse_click = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONUP:
                mouse_click = True
            if event.type == UP_SOUND_VALUE_EVENT.type:
                volume += 0.1
                set_volume(volume, volume_is_on)
                button_sound.play()
            if event.type == DOWN_SOUND_VALUE_EVENT.type:
                volume -= 0.1
                set_volume(volume, volume_is_on)
                button_sound.play()
            if event.type == OFF_EVENT.type:
                volume_is_on = sound_switcher(volume_is_on)
                print("OFF")
            if event.type == ON_EVENT.type:
                volume_is_on = sound_switcher(volume_is_on)
                print("ON")
            if event.type == BACK_BUTTON_EVENT.type:
                button_sound.play()
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


def records(surface):
    background = pg.image.load("images/about.png")
    surface.blit(background, (50, 400))

    gui_sprites = pg.sprite.Group()
    Button((55, 405), "", BACK_BUTTON_EVENT, gui_sprites, base_image_filename="about_back_button.png",
           hover_image_filename="hover_about_back_button.png")

    #   Чтение рекордов из csv файла
    with open('records.csv', 'r') as f:
        data = csv.DictReader(f, delimiter=';')
        s = [i for i in data]

    text = [(about_font.render(f"LEVEL 1: {s[0]['record']}", True, "black"), (80, 500)),
            (about_font.render(f"LEVEL 2: {s[1]['record']}", True, "black"), (80, 540)),
            (about_font.render(f"LEVEL 3: {s[2]['record']}", True, "black"), (80, 580)),
            (about_font.render(f"FREE MODE: {s[3]['record']}", True, "black"), (80, 620)),
            (font.render("RECORDS", True, "black"), ((WIDTH - 189) // 2, 445))]

    for i in text:
        surface.blit(i[0], (i[1][0], i[1][1]))

    while True:
        mouse_click = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONUP:
                mouse_click = True
            if event.type == BACK_BUTTON_EVENT.type:
                button_sound.play()
                return

        gui_sprites.update(pg.mouse.get_pos(), mouse_click)
        gui_sprites.draw(surface)
        pg.display.update()
