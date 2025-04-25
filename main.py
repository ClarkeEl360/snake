import pygame
import sys
import config
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

font = pygame.font.SysFont(None, 35)

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

pygame.mixer.music.load("SongThatMightPlayWhenYouFightSans.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


def snake_game(running = True, CELL_SIZE = 10, direction = 1, update_snake = 0, score = 0, speed = 0):
    apple_pos = [random.randint(0, config.SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, config.SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
    BG = (255, 200, 150)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BODY_INNER = (50, 175, 25)
    BODY_OUTER = (100, 100, 200)
    APPLE_COLOR = (255, 20, 30)
    font = pygame.font.SysFont(None, 35)
    def draw_apple():
        pygame.draw.rect(screen, APPLE_COLOR, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))

    def draw_score():
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, [10, 10])
    while running:
        screen.fill(BG)
        draw_apple()
        draw_score()
        p = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and direction != 3:
                    direction = 1
                elif event.key == pygame.K_d and direction != 4:
                    direction = 2
                elif event.key == pygame.K_s and direction != 1:
                    direction = 3
                elif event.key == pygame.K_a and direction != 2:
                    direction = 4
                if event.key == pygame.K_UP:
                    speed -= 5
                if event.key == pygame.K_DOWN:
                    speed += 5
                if event.key == pygame.K_0:
                    speed = 0
                if event.key == pygame.K_p:
                    s = 2
        if update_snake > 59 + speed:
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
                p = 2

        for i in range(len(snake_pos)):
            segment = snake_pos[i]
            if i == 0:
                pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, RED, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
                
            else:
                pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, BODY_INNER, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
            
        update_snake += 1
        if p != 1:
            running = False
            return s
        pygame.display.flip()
p = 2
s = 1
run = True
while run:
    screen.fill(BG)
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and p != 1:
                    p = 1
    score_text = font.render("Press: P to start/stop Snake Game", True, BLACK)
    screen.blit(score_text, [10, 10])
    while p == 1 or s != 1:
        running = True
        if s == 1:
            snake_game(CELL_SIZE, direction, update_snake, score, speed, running)
        p = 2

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
        
    CELL_SIZE = 10
    direction = 1
    update_snake = 0
    score = 0
    speed = 0
    pygame.display.flip()

    


pygame.quit()
sys.exit()