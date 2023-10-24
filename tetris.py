import pygame
from pygame.constants import *

from constants import DARK_GRAY, DOWN, GRAY, LEFT, PURPLE, RIGHT
from game_engine import GameEngine
from settings import CELL_SIZE, COLUMNS_NUMBER, ROWS_NUMBER


pygame.init()
engine = GameEngine()

# Setup game screen
width, height = COLUMNS_NUMBER * CELL_SIZE, ROWS_NUMBER * CELL_SIZE
screen = pygame.display.set_mode(size=(width, height))

# Setup game timer
pygame.time.set_timer(USEREVENT, 200)
clock = pygame.time.Clock()

# Setup fonts and render texts
game_font = pygame.font.Font(name="standard_font", size=18)
text_start = game_font.render("Press enter to start", True, PURPLE)


def tetris():
    engine.draw_blocks(screen=screen, color=engine.puzzle.color, blocks=engine.puzzle.locus)
    engine.draw_blocks(screen=screen, color=DARK_GRAY, blocks=engine.obstacles)
    for event in pygame.event.get():
        if event.type == QUIT:
            return ...
        elif event.type == USEREVENT:
            if engine.fall() is None:
                return main_menu
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                engine.fall_down()
            elif event.key in [K_w, K_UP]:
                engine.puzzle.change_formation(engine.available_matrix)
            elif event.key in [K_s, K_DOWN]:
                engine.puzzle.move(DOWN, engine.available_matrix)
            elif event.key in [K_a, K_LEFT]:
                engine.puzzle.move(LEFT, engine.available_matrix)
            elif event.key in [K_d, K_RIGHT]:
                engine.puzzle.move(RIGHT, engine.available_matrix)


def main_menu():
    for event in pygame.event.get():
        if event.type == QUIT:
            return ...
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                return tetris
    screen.blit(source=text_start, dest=(55, 110, 200, 200))


# Main loop
main_view = main_menu
while True:
    clock.tick(60)
    screen.fill(GRAY)
    if new_view := main_view():
        if callable(new_view):
            main_view = new_view
        elif new_view is ...:
            break
    pygame.display.update()

# Gracefully close the game
pygame.quit()
