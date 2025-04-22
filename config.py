import pygame
import sys
import random

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 660
title = "This is a screen"
FPS = 60


randred = random.randint(0, 255)
randgreen = random.randint(0, 255)
randblue = random.randint(0, 255)
RANDCOLOR = (randred, randgreen, randblue)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKY = (140, 180, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(title)
clock = pygame.time.Clock()