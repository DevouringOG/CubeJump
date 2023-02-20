import pygame as pg
SIZE = WIDTH, HEIGHT = (600, 1000)
FPS = 60
#   Шрифты
font = pg.font.Font("fonts/minecraft-1-1.otf", 36)
about_font = pg.font.Font("fonts/minecraft-1-1.otf", 25)
game_over_font = pg.font.Font("fonts/minecraft-1-1.otf", 70)
restart_font = pg.font.Font("fonts/minecraft-1-1.otf", 15)
logo_font = pg.font.Font('fonts/logo_font.ttf', 85)

GRAVITY = 0.75
volume = 0.1
volume_is_on = True
platform_y_cords = [i for i in range(100, 985, 100)]

#   Создание всех ивентов
START_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 1)
LEVEL1_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 2)
LEVEL2_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 3)
LEVEL3_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 4)
SETTING_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 5)
BACK_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 6)
ABOUT_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 7)
UP_SOUND_VALUE_EVENT = pg.event.Event(pg.USEREVENT + 8)
DOWN_SOUND_VALUE_EVENT = pg.event.Event(pg.USEREVENT + 9)
OFF_EVENT = pg.event.Event(pg.USEREVENT + 10)
ON_EVENT = pg.event.Event(pg.USEREVENT + 11)
FREE_LEVEL_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 12)
RECORDS_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 13)

#   Настройки для каждего уровня
levels_config = {1: {"message_color": (81, 73, 128), "platforms": (9, 0, 0, 0),
                     "finish_score": 1000},
                 2: {"message_color": (94, 51, 150), "platforms": (6, 3, 0, 0),
                     "finish_score": 3000},
                 3: {"message_color": (2, 69, 117), "platforms": (3, 3, 3, 0),
                     "finish_score": 5000},
                 4: {"message_color": (94, 51, 150), "platforms": (3, 3, 3, 0),
                     "finish_score": float("inf")}}

available_levels = [1]
