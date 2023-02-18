from Doodler import Doodler
from Platforms import *
from MenuScreens import start_screen
from Monster import *


def game_over_message(surface, doodler_score):
    game_over_text1 = game_over_font.render(f'GAME OVER', True, 'black')
    score_text2 = font.render(f'YOUR SCORE: {doodler_score}', True, 'black')
    press_space_text3 = restart_font.render(f'Press space to restart', True, 'black')
    pg.draw.rect(surface, (171, 194, 112), (0, 350, WIDTH, 240))
    surface.blit(game_over_text1, ((WIDTH - game_over_text1.get_width()) // 2, 400))
    surface.blit(score_text2, ((WIDTH - score_text2.get_width()) // 2, 500))
    surface.blit(press_space_text3, ((WIDTH - press_space_text3.get_width()) // 2, 950))


def finish_message(surface, level):
    game_over_text1 = game_over_font.render(f'FINISH!', True, 'black')
    score_text2 = font.render(f'You unlock next level!' if not level + 1 in available_levels
                              else "You finish this level again!", True, 'black')
    press_space_text3 = restart_font.render(f'Press space to menu', True, 'black')
    pg.draw.rect(surface, (171, 194, 112), (0, 350, WIDTH, 240))
    surface.blit(game_over_text1, ((WIDTH - game_over_text1.get_width()) // 2, 400))
    surface.blit(score_text2, ((WIDTH - score_text2.get_width()) // 2, 500))
    surface.blit(press_space_text3, ((WIDTH - press_space_text3.get_width()) // 2, 950))


def create_platforms(platform_group, sprites_group, platforms_config):
    platform_group.add(Platform(255, 985, sprites_group))
    random.shuffle(platform_y_cords)
    print(platform_y_cords)
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


def play(screen, level):
    level_config = levels_config[level]
    background_color = level_config["background"]
    platforms_config = level_config["platforms"]
    finish_score = level_config["finish_score"]
    all_sprites = pg.sprite.Group()
    platforms = pg.sprite.Group()
    monsters_group = pg.sprite.Group()
    doodler = Doodler(WIDTH // 2 - 50, HEIGHT - 115, all_sprites)
    create_platforms(platforms, all_sprites, platforms_config)
    score = max_doodler_y = game_over = finish = monsters = 0
    clock = pg.time.Clock()

    # Main loop
    while True:
        screen.fill(background_color)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and game_over:
                restart(doodler, platforms)
                score = max_doodler_y = game_over = monsters = doodler.falling = 0
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and finish:
                available_levels.append(level + 1)
                level = start_screen(screen)
                level_config = levels_config[level]
                background_color = level_config["background"]
                platforms_config = level_config["platforms"]
                finish_score = level_config["finish_score"]
                all_sprites = pg.sprite.Group()
                platforms = pg.sprite.Group()
                monsters_group = pg.sprite.Group()
                doodler = Doodler(WIDTH // 2 - 50, HEIGHT - 115, all_sprites)
                create_platforms(platforms, all_sprites, platforms_config)
                score = max_doodler_y = game_over = finish = monsters = doodler.falling = 0

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
        score_label = font.render(f"Score: {score}/{finish_score}", True, 'black')
        screen.blit(score_label, (10, 10))

        if monsters < score // 1000:
            monster = Monster(pg.image.load("images/monster-sheet.png"), 4, 1, all_sprites)
            monsters_group.add(monster)
            all_sprites.add(monster)
            monsters += 1

        # Game over check
        if score >= finish_score:
            finish = True

        if doodler.rect.y > HEIGHT:
            game_over = True

        if game_over:
            game_over_message(screen, score)

        if finish:
            finish_message(screen, level)

        pg.display.update()
        clock.tick(FPS)
