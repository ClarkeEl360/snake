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

snake_pos = [[int(config.SCREEN_WIDTH / 2), int(config.SCREEN_HEIGHT / 2)]]
snake_pos.append([int(config.SCREEN_WIDTH / 2), int(config.SCREEN_HEIGHT / 2) + CELL_SIZE])
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
            
    if update_snake > 59:
        update_snake = 0

        head_x, head_y = snake_pos[0]

        if direction == 1:
            head_y -= CELL_SIZE
        elif direction == 2:
            head_x += CELL_SIZE
        elif direction == 3:
            head_y += CELL_SIZE
        elif direction == 4:
            head_x -= CELL_SIZE
        

        snake_pos.insert(0, [head_x, head_y])
        snake_pos.pop()

        if snake_pos[0] == apple_pos:
            apple_pos = [random.randint(0, config.SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, config.SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]

            snake_pos.append(snake_pos[-1])
            score += 1

        if head_x < 0 or head_x >= config.SCREEN_WIDTH or head_y < 0 or head_y >= config.SCREEN_HEIGHT:
            running = False

    for i in range(len(snake_pos)):
        segment = snake_pos[i]
        if i == 0:
            pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, RED, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
            
        else:
            pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BODY_INNER, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        
    update_snake += 1

    pygame.display.flip()


pygame.quit()
sys.exit()