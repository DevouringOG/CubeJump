import csv
import random
from Doodler import Doodler
from Platforms import *
from MenuScreens import start_screen
from Monster import *
from Sound import *


def message(surface, text, color):
    text1 = game_over_font.render(text[0], True, 'black')
    text2 = font.render(text[1], True, 'black')
    text3 = restart_font.render(text[2], True, 'black')
    pg.draw.rect(surface, color, (0, 350, WIDTH, 240))
    surface.blit(text1, ((WIDTH - text1.get_width()) // 2, 400))
    surface.blit(text2, ((WIDTH - text2.get_width()) // 2, 500))
    surface.blit(text3, ((WIDTH - text3.get_width()) // 2, 950))


def create_platforms(platform_group, sprites_group, platforms_config):
    platform_group.add(Platform(255, 985, sprites_group))
    random.shuffle(platform_y_cords)
    for i in range(0, platforms_config[0]):
        platform_group.add(Platform(random.randrange(0, WIDTH - 85),
                                    platform_y_cords[i], sprites_group))
    for i in range(platforms_config[0], sum(platforms_config[:2])):
        platform_group.add(HorizontalPlatform(random.randrange(0, WIDTH - 85),
                                              platform_y_cords[i], sprites_group))
    for i in range(sum(platforms_config[:2]), sum(platforms_config[:3])):
        platform_group.add(BreakingPlatform(random.randrange(0, WIDTH - 85),
                                            platform_y_cords[i], sprites_group))
    for i in range(sum(platforms_config[:3]), 9):
        platform_group.add(TeleportingPlatform(random.randrange(0, WIDTH - 85),
                                               platform_y_cords[i], sprites_group))


def restart(doodler, platforms: pg.sprite.Group):
    doodler.restart()
    for platform in platforms:
        platform.restart()
    platforms.sprites()[0].rect.x = 255
    platforms.sprites()[0].rect.y = 985
    pygame.mixer.music.play(-1)


def update_record(level, score):
    with open('records.csv', 'r') as records_file:
        reader = csv.DictReader(records_file, delimiter=';')
        s = [i for i in reader]
    if int(s[level - 1]['record']) < score:
        s[level - 1]['record'] = score
    with open('records.csv', 'w', newline='', encoding="utf8") as f:
        writer = csv.DictWriter(
            f, fieldnames=list(s[0].keys()),
            delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in s:
            writer.writerow(d)


def play(screen, level):
    level_config = levels_config[level]
    background = pg.image.load(f"images/level{level}_background.png")
    platforms_config = level_config["platforms"]
    finish_score = level_config["finish_score"]
    message_color = level_config["message_color"]
    all_sprites = pg.sprite.Group()
    platforms = pg.sprite.Group()
    doodler = Doodler((WIDTH - 70) // 2, HEIGHT - 70 - 15, all_sprites)
    monsters_group = pg.sprite.Group()
    create_platforms(platforms, all_sprites, platforms_config)
    score = max_doodler_y = game_over = finish = falling = monsters = 0
    clock = pg.time.Clock()
    pause = False
    pause_effect = pg.image.load("images/pause_effect.png")
    pygame.mixer.music.play(-1)

    # Main loop
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pause = not pause
                if pause:
                    screen.blit(pause_effect, (0, 0))
                    screen.blit(logo_font.render("PAUSE", True, "black"), ((WIDTH - 300) // 2, (HEIGHT - 119) // 2))
                    pg.display.update()
                    break
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and game_over:
                restart(doodler, platforms)
                monsters_group = pg.sprite.Group()
                score = max_doodler_y = game_over = falling = monsters = doodler.falling = 0
                pygame.mixer.music.play(-1)
                
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and finish:
                available_levels.append(level + 1)
                level = start_screen(screen, True)
                level_config = levels_config[level]
                background = pg.image.load(f"images/level{level}_background.png")
                platforms_config = level_config["platforms"]
                finish_score = level_config["finish_score"]
                message_color = level_config["message_color"]
                all_sprites = pg.sprite.Group()
                platforms = pg.sprite.Group()
                monsters_group = pg.sprite.Group()
                doodler = Doodler((WIDTH - 70) // 2, HEIGHT - 70 - 15, all_sprites)
                create_platforms(platforms, all_sprites, platforms_config)
                score = max_doodler_y = game_over = finish = monsters = doodler.falling = 0
                pygame.mixer.music.play(-1)
                pause = False

        if pause:
            continue

        screen.blit(background, (0, 0))

        platforms.draw(screen)
        platforms.update()

        doodler.move(pg.key.get_pressed())
        doodler.update(platforms, monsters_group)
        doodler.render(screen)
        monsters_group.draw(screen)
        for monster in monsters_group:
            monster.move()
            monster.change_frame()

        # Camera
        if doodler.jump_power < 0 and doodler.rect.y < HEIGHT // 3:
            while doodler.rect.y < HEIGHT // 3:
                max_doodler_y -= 1
                for sprite in all_sprites.sprites():
                    sprite.rect.y += 1

        # Update score
        if doodler.jump_power == 0 and HEIGHT - doodler.rect.y > max_doodler_y:
            score += HEIGHT - doodler.rect.y - max_doodler_y
            max_doodler_y = HEIGHT - doodler.rect.y

        # Show score
        score_label = font.render(f"Score: {score}/{finish_score}" if finish_score != float("inf")
                                  else f"Score: {score}", True, 'black')
        screen.blit(score_label, (10, 10))

        if monsters < score // 1000:
            if random.randint(0, 2):
                monster = BlackMonster(pg.image.load("images/monster-sheet.png"), 3, 1, all_sprites)
            else:
                monster = RedMonster(pg.image.load("images/monster_sheet2.png"), 4, 1, all_sprites)
            monsters_group.add(monster)
            all_sprites.add(monster)
            monsters += 1

        # Game over check
        if score >= finish_score:
            finish = True
            update_record(level, finish_score)
            message(screen, ["FINISH!", "You unlock next level!" if not level + 1 in available_levels
                    else "You finish this level again!", "Press space to menu"], message_color)
            pygame.mixer.music.stop()

        if doodler.rect.y > HEIGHT:
            game_over = True
            update_record(level, score)
            message(screen, ["GAME OVER", f"YOUR SCORE: {score}", "Press space to restart"], message_color)
            falling += 1
            pygame.mixer.music.stop()

        pg.display.update()
        clock.tick(FPS)
