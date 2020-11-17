import sys
import pygame
from pygame.locals import QUIT

SCREEN_SIZEX = 800
SCREEN_SIZEY = 600
SCREEN_COLOR = (0,0,0)
clock = pygame.time.Clock()

pygame.init()

window_surface = pygame.display.set_mode((SCREEN_SIZEX,SCREEN_SIZEY))
window_surface.fill(SCREEN_COLOR)

pygame.display.update()


# 鼠標 鎖定 和 隱藏
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    window_surface.fill(SCREEN_COLOR)
    pygame.display.update()
    clock.tick(60)