import pygame
import random
from pygame import *
from random import *
from models import puzzle_t, puzzle_i, puzzle_j, puzzle_l, puzzle_o, puzzle_z, puzzle_s




class GameEngine():
    cellSize = 25
    cell_columnNumber = 11
    cell_rowNumber = 20
    FPS = 60
    background = (200, 200, 200)

    screen = pygame.display.set_mode((cell_columnNumber * cellSize, cell_rowNumber * cellSize))
    clock = pygame.time.Clock()

    pygame.time.set_timer(USEREVENT, 200)




    def __init__(self):
        self.puzzles = [puzzle_t, puzzle_i, puzzle_j, puzzle_l, puzzle_o, puzzle_z, puzzle_s]
        self.puzzle = choice(self.puzzles)
        self.direction = pygame.Vector2(0,0)
        self.all_cells = self.download_all_cells()
        self.obstacles = dict()
        self.game_font = pygame.font.Font(None, 18)
        self.text_start = self.game_font.render('Press enter to start', True, (140, 40, 230))

    def fps_loop_decorator(self, func):
        def inner():
            while True:
                self.clock.tick(self.FPS)
                self.screen.fill(self.background)
                func()
                pygame.display.update()
        return inner

    def run_event(self):
        self.fall()

    def run(self):
        self.move()

    def draw(self):
        self.print_puzzle()

# Game
    def move(self):
        if self.direction and all(x + self.direction in self.all_cells and x + self.direction not in sum(self.obstacles.values(),[]) for x in self.puzzle.vectors):
            self.puzzle.vectors[0] += self.direction
            self.puzzle.refresh()
        self.direction = pygame.Vector2(0,0)

    def fall(self):
        if all(x + (0, 1) in self.all_cells and x + (0, 1) not in sum(self.obstacles.values(),[]) for x in self.puzzle.vectors):
            self.puzzle.vectors[0] += (0, 1)
            self.puzzle.refresh()
            return True
        else:
            for block in self.puzzle.vectors:
                if block.y not in self.obstacles: self.obstacles[block.y] = [block]
                else: self.obstacles[block.y].append(block)
            if any([block.y < 0 for block in sum(self.obstacles.values(),[])]):
                self.new_game()
                self.menu()
                return
            self.restart_puzzle()
            self.check_line()
            return False

    def print_puzzle(self):
        for vector in self.puzzle.vectors:
            pygame.draw.rect(self.screen, self.puzzle.color, (vector.x * self.cellSize, vector.y * self.cellSize, self.cellSize, self.cellSize))
            pygame.draw.rect(self.screen, (0,0,0), (vector.x * self.cellSize, vector.y * self.cellSize, self.cellSize, self.cellSize),1)
        for vector in sum(self.obstacles.values(),[]):
            pygame.draw.rect(self.screen, (170,170,170), (vector.x * self.cellSize, vector.y * self.cellSize, self.cellSize, self.cellSize))
            pygame.draw.rect(self.screen, (0,0,0), (vector.x * self.cellSize, vector.y * self.cellSize, self.cellSize, self.cellSize),1)

    def download_all_cells(self):
        all_cells = []
        for column in range(self.cell_columnNumber):
            for row in range(-5, self.cell_rowNumber):
                all_cells.append((column, row))
        return all_cells

    def restart_puzzle(self):
        self.puzzle.vectors[0] = pygame.Vector2(5, -2)
        self.puzzle.index = 0
        self.puzzle.refresh()
        self.puzzle = choice(self.puzzles)

    def check_line(self):
        delete_lines = [i for i in self.obstacles if len(self.obstacles[i]) > 10]
        for line in sorted(delete_lines):
            if len(self.obstacles) == 1: del(self.obstacles[line])
            else:
                for i in reversed(range(20-len(self.obstacles), int(line))):
                    self.obstacles[float(i + 1)] = self.obstacles[float(i)]
                    for x in self.obstacles[float(i + 1)]:
                        x.y += 1
                del(self.obstacles[20.0-float(len(self.obstacles))])

    def fall_down(self):
        while self.fall(): pass

    def new_game(self):
        self.obstacles = dict()
        self.puzzle = choice(self.puzzles)
        self.direction = pygame.Vector2(0, 0)
