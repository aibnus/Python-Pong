import pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

#size
WIDTH = 1280
HEIGHT = 720

#speed
SPEED = 5

#color
light_grey = (200,200,200)
BG = pygame.Color('grey12')

#font
FONT = pygame.font.Font("freesansbold.ttf", 32)

#sound
PONG_SOUND = pygame.mixer.Sound("sounds/pong.ogg")
SCORE_SOUND = pygame.mixer.Sound("sounds/score.ogg")