import pygame as pg
SIZE = WIDTH, HEIGHT = (600, 1000)
FPS = 60
font = pg.font.Font("minecraft-1-1.otf", 36)
game_over_font = pg.font.Font("minecraft-1-1.otf", 70)
restart_font = pg.font.Font("minecraft-1-1.otf", 15)
logo_font = pg.font.Font('logo_font.ttf', 85)
GRAVITY = 0.75
platform_y_cords = [i for i in range(100, 985, 100)]

START_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 1)
LEVEL1_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 2)
LEVEL2_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 3)
LEVEL3_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 4)
SETTING_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 5)
BACK_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 6)
ABOUT_BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 7)
levels_config = {1: {"background": (153, 229, 80), "platforms": (9, 0, 0, 0), "finish_score": 1500},
                 2: {"background": (223, 113, 38), "platforms": (6, 3, 0, 0), "finish_score": 3000},
                 3: {"background": (91, 110, 225), "platforms": (3, 3, 3, 0), "finish_score": 5000}}
available_levels = [1, 2, 3]
