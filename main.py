import pygame
import sys
import config
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption(config.title)

CELL_SIZE = 10
direction = 1
update_snake = 0
score = 0

snake_pos = ([int(config.SCREEN_WIDTH / 2), int(config.SCREEN_HEIGHT / 2) + CELL_SIZE])
snake_pos.append([int(config.SCREEN_WIDTH / 2), int(config.SCREEN_HEIGHT / 2) + CELL_SIZE * 2])
snake_pos.append([int(config.SCREEN_WIDTH / 2), int(config.SCREEN_HEIGHT / 2) + CELL_SIZE * 3])

BG = (255, 200, 150)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BODY_INNER = (50, 175, 25)
BODY_OUTER = (100, 100, 200)
APPLE_COLOR = (255, 20, 30)

apple_pos = [random.randint(0, config.SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, config.SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]

font = pygame.font.SysFont(None, 35)

pygame.mixer.music.load("SongThatMightPlayWhenYouFightSans.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

def draw_apple():
    pygame.draw.rect(screen, APPLE_COLOR, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))

def draw_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, [10, 10])


running = True
while running:
    screen.fill(BG)
    draw_apple()
    draw_score()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != 3:
                direction = 1
            elif event.key == pygame.K_w and direction != 4:
                direction = 2
            elif event.key == pygame.K_w and direction != 1:
                direction = 3
            elif event.key == pygame.K_w and direction != 2:
                direction = 4