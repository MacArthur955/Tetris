import pygame, random
from pygame import *
from random import *
from game_engine import GameEngine


pygame.init()
game_engine = GameEngine()

running = True
while running:
    clock.tick(FPS)
    screen.fill(background)
    game_engine.draw()
    game_engine.run()
    for event in pygame.event.get():
        if event.type == QUIT: running = False
        elif event.type == USEREVENT: game_engine.run_event()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE: game_engine.fall_down()
            elif event.key == K_w or event.key == K_UP: game_engine.puzzle.update()
            elif event.key == K_s or event.key == K_DOWN: game_engine.direction = pygame.Vector2(0,1)
            elif event.key == K_a or event.key == K_LEFT: game_engine.direction = pygame.Vector2(-1,0)
            elif event.key == K_d or event.key == K_RIGHT: game_engine.direction = pygame.Vector2(1,0)

    pygame.display.update()

pygame.quit()