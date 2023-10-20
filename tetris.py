import pygame
from pygame.constants import *

from game_engine import GameEngine
from colors import GRAY, PURPLE


pygame.init()
game_engine = GameEngine()
pygame.time.set_timer(USEREVENT, 200)
clock = pygame.time.Clock()
game_font = pygame.font.Font(size=18)
text_start = game_font.render("Press enter to start", True, PURPLE)


def tetris():
    game_engine.print_puzzle()
    game_engine.print_obstacles()
    for event in pygame.event.get():
        if event.type == QUIT:
            return ...
        elif event.type == USEREVENT:
            if game_engine.fall() is None:
                return main_menu
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                game_engine.fall_down()
            elif event.key in [K_w, K_UP]:
                game_engine.puzzle.change_formation(game_engine.matrix, game_engine.obstacles.values())
            elif event.key in [K_s, K_DOWN]:
                game_engine.puzzle.move(0, 1, game_engine.matrix, game_engine.obstacles.values())
            elif event.key in [K_a, K_LEFT]:
                game_engine.puzzle.move(-1, 0, game_engine.matrix, game_engine.obstacles.values())
            elif event.key in [K_d, K_RIGHT]:
                game_engine.puzzle.move(1, 0, game_engine.matrix, game_engine.obstacles.values())


def main_menu():
    for event in pygame.event.get():
        if event.type == QUIT:
            return ...
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                return tetris
    game_engine.screen.blit(source=text_start, dest=(55, 110, 200, 200))


# Main loop
main_view = main_menu
while True:
    clock.tick(60)
    game_engine.screen.fill(GRAY)
    if feedback := main_view():
        if callable(feedback):
            main_view = feedback
        elif feedback is ...:
            break
    pygame.display.update()

# Gracefully close the game
pygame.quit()
