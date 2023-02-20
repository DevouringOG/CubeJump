import pygame as pg
import sys


#   Выключение игры
def terminate():
    pg.quit()
    sys.exit()


pg.init()
pg.display.set_caption("Doodle jump")

# Импортируется здесь, так как в этих модулях действия могут происходить только после инициализации
import Game
from MenuScreens import *

screen = pg.display.set_mode(SIZE)

#   Запуск стартового окна и начало игры
level = start_screen(screen)
Game.play(screen, level)

terminate()
