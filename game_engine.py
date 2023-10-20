import pygame
import random
from pygame import *
from models import puzzle_t, puzzle_i, puzzle_j, puzzle_l, puzzle_o, puzzle_z, puzzle_s
from settings import COLUMS_NUMBER, ROWS_NUMBER, CELL_SIZE


class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            size=(COLUMS_NUMBER * CELL_SIZE, ROWS_NUMBER * CELL_SIZE)
        )
        self.puzzles = [puzzle_t, puzzle_i, puzzle_j, puzzle_l, puzzle_o, puzzle_z, puzzle_s]
        self.puzzle = random.choice(self.puzzles)
        self.matrix = [(x, y) for x in range(COLUMS_NUMBER) for y in range(-5, ROWS_NUMBER)]
        self.obstacles = dict()

    def fall(self):
        if all(x + (0, 1) in self.matrix and x + (0, 1) not in sum(self.obstacles.values(),[]) for x in self.puzzle.locus):
            self.puzzle.locus[0] += (0, 1)
            self.puzzle.regroup()
            return True
        else:
            for block in self.puzzle.locus:
                if block.y not in self.obstacles:
                    self.obstacles[block.y] = [block]
                else:
                    self.obstacles[block.y].append(block)
            if any([block.y < 0 for block in sum(self.obstacles.values(),[])]):
                self.new_game()
                return None
            self.restart_puzzle()
            self.check_line()
            return False

    def print_puzzle(self):
        for vector in self.puzzle.locus:
            pygame.draw.rect(
                surface=self.screen,
                color=self.puzzle.color,
                rect=(vector.x * CELL_SIZE, vector.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )
            pygame.draw.rect(self.screen, (0,0,0), (vector.x * CELL_SIZE, vector.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)

    def print_obstacles(self):
        for vector in sum(self.obstacles.values(),[]):
            pygame.draw.rect(self.screen, (170,170,170), (vector.x * CELL_SIZE, vector.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(self.screen, (0,0,0), (vector.x * CELL_SIZE, vector.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)

    def restart_puzzle(self):
        self.puzzle.reset()
        self.puzzle = random.choice(self.puzzles)

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
        while self.fall():
            pass

    def new_game(self):
        self.obstacles = dict()
        self.puzzle = random.choice(self.puzzles)
