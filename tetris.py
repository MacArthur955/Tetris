import pygame
from pygame.constants import *

from game_engine import GameEngine
from colors import GRAY


pygame.init()
game_engine = GameEngine(cell_size=25, columns_number=11, rows_number=20)
pygame.time.set_timer(USEREVENT, 200)
clock = pygame.time.Clock()


def tetris():
    game_engine.draw()
    game_engine.run()
    for event in pygame.event.get():
        if event.type == QUIT:
            return ...
        elif event.type == USEREVENT:
            if game_engine.run_event() is None:
                return main_menu
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                game_engine.fall_down()
            elif event.key == K_w or event.key == K_UP:
                game_engine.puzzle.update(game_engine.all_cells, game_engine.obstacles.values())
            elif event.key == K_s or event.key == K_DOWN:
                game_engine.direction = pygame.Vector2(0, 1)
            elif event.key == K_a or event.key == K_LEFT:
                game_engine.direction = pygame.Vector2(-1, 0)
            elif event.key == K_d or event.key == K_RIGHT:
                game_engine.direction = pygame.Vector2(1, 0)


def main_menu():
    for event in pygame.event.get():
        if event.type == QUIT:
            return ...
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                return tetris
    game_engine.screen.blit(source=game_engine.text_start, dest=(55, 110, 200, 200))


# Main loop
main_func = main_menu
while True:
    clock.tick(60)
    game_engine.screen.fill(GRAY)
    if feedback := main_func():
        if callable(feedback):
            main_func = feedback
        elif feedback is ...:
            break
    pygame.display.update()

# Gracefully close the game
pygame.quit()
