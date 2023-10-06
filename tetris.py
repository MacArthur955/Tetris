import pygame
from pygame.constants import *

from game_engine import GameEngine


pygame.init()
game_engine = GameEngine()


@game_engine.fps_loop_decorator
def tetris():
    game_engine.draw()
    game_engine.run()
    for event in pygame.event.get():
        if event.type == QUIT:
            return ...
        elif event.type == USEREVENT:
            if game_engine.run_event() is None:
                return menu
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                game_engine.fall_down()
            elif event.key == K_w or event.key == K_UP:
                game_engine.puzzle.update()
            elif event.key == K_s or event.key == K_DOWN:
                game_engine.direction = pygame.Vector2(0, 1)
            elif event.key == K_a or event.key == K_LEFT:
                game_engine.direction = pygame.Vector2(-1, 0)
            elif event.key == K_d or event.key == K_RIGHT:
                game_engine.direction = pygame.Vector2(1, 0)


@game_engine.fps_loop_decorator
def menu():
    for event in pygame.event.get():
        if event.type == QUIT:
            return ...
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                return tetris
    game_engine.screen.blit(game_engine.text_start, (55, 110, 200, 200))


menu()
pygame.quit()
