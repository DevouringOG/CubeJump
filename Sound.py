import pygame
from Config import VOL

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.music.load("Sound/Cipher2.mp3")  # Backgorund music
pygame.mixer.music.set_volume(VOL + 0.1)

# SFX
jump_sound = pygame.mixer.Sound("Sound/jump.wav")
breaking_platform_sound = pygame.mixer.Sound("Sound/break_platform.ogg")
falling_sound = pygame.mixer.Sound("Sound/falling.ogg")

SFX = [jump_sound, breaking_platform_sound, falling_sound]
for i in SFX:
    i.set_volume(VOL)


def falling_sound_play(falling):
    if falling == 1:
        falling_sound.play()
    else:
        falling += 1