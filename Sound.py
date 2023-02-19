import pygame
from Config import volume

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.music.load("Sound/Cipher2.mp3")  # Background music

# SFX
jump_sound = pygame.mixer.Sound("Sound/jump.wav")
breaking_platform_sound = pygame.mixer.Sound("Sound/break_platform.ogg")
falling_sound = pygame.mixer.Sound("Sound/falling.ogg")
button_sound = pygame.mixer.Sound("Sound/minecraft_click.ogg")
monster_sound = pygame.mixer.Sound("Sound/monster_sound.ogg")
monster_crash_sound = pygame.mixer.Sound("Sound/monster_crash.ogg")
monster_jump_sound = pygame.mixer.Sound("Sound/monster_jump.ogg")

SFX = [jump_sound, breaking_platform_sound, falling_sound, button_sound,
       monster_sound, monster_jump_sound, monster_crash_sound]


def set_volume(volume):
    for i in SFX:
        i.set_volume(volume)
    pygame.mixer.music.set_volume(volume)


def falling_sound_play(falling):
    if falling == 1:
        falling_sound.play()
    else:
        falling += 1


set_volume(volume)
